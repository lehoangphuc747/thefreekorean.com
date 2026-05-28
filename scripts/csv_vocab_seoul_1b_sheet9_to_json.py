"""
Script: csv_vocab_seoul_1b_sheet9_to_json

Mục đích: Chuyển CSV từ vựng (xuất kiểu SpreadsheetImportPlus / Anki) sang JSON UTF-8.

Công cụ: pandas — cùng hướng tiếp cận như excel-analysis (đọc bảng, làm sạch, xuất).
File nguồn là .csv nên dùng pd.read_csv; nếu sau này có .xlsx có thể đổi sang pd.read_excel.

Mặc định đọc:
  src/content/vocabulary/anki-seoul_1b-dpk48hqb_2 - Sheet 9.csv

Mặc định ghi theo từng bài (quyển 1B → vol-1b; một file JSON mỗi bài):
  src/content/vocabulary/seoul-korean/vol-1b/lesson-09.json
  … lesson-10.json, lesson-11.json (và các bài khác nếu CSV có).

Định dạng đầu ra: mảng JSON gốc `[{...}, ...]` — mỗi phần tử là 1 note Anki:
`__deck__`, `__notetype__`, `__tags__` (mảng), rồi các trường nội dung
id, word, meaning, pos, transliteration, explain, image, example, example_translated,
collocation, synonym, antonym, audio_* (ô không có trong CSV → chuỗi rỗng).

`__deck__` / `__tags__`: theo từng dòng — cột **bài** (제09과, …) + **khoá** → quyển (vd. 1B cho 서울대_한국어_1B).
Tên file "Sheet 9" chỉ là sheet spreadsheet; CSV vẫn có nhiều bài trong cùng file.

Chạy (từ thư mục gốc repo):
  pip install -r scripts/requirements-tools.txt
  python scripts/csv_vocab_seoul_1b_sheet9_to_json.py

Tuỳ chọn:
  python scripts/csv_vocab_seoul_1b_sheet9_to_json.py --input "path.csv"
  python scripts/csv_vocab_seoul_1b_sheet9_to_json.py --output "mot-file.json"   # gộp 1 file thay vì tách theo bài

Tags: vocabulary, csv, json, pandas
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    print(
        "Thiếu thư viện pandas. Chạy: pip install -r scripts/requirements-tools.txt",
        file=sys.stderr,
    )
    sys.exit(1)


# Thư mục gốc repo = cha của thư mục scripts/
REPO_ROOT = Path(__file__).resolve().parent.parent

DEFAULT_INPUT_REL = Path("src/content/vocabulary/anki-seoul_1b-dpk48hqb_2 - Sheet 9.csv")

# Gốc web-safe: quyển 1B → vol-1b; từng bài → lesson-09 … (đoạn cuối __deck__ 제NN과)
DEFAULT_LESSON_ROOT_REL = Path("src/content/vocabulary/seoul-korean/vol-1b")

# Loại note Anki — cố định theo template import.
ANKI_NOTETYPE = "(Anki) Template học từ vựng của Admin Phúc [2026]"

# Mã sách (cột khoá) → đoạn quyển trong deck/tag Anki (1B = Seoul Korean 1B).
COURSE_KEY_TO_VOLUME: dict[str, str] = {
    "서울대_한국어_1B": "1B",
}

# Dòng 1: SpreadsheetImportPlus… | Dòng 2: header | Dòng 3: kiểu cột | Dòng 4: trống
SKIP_ROWS = [0, 2, 3]

# Cột CSV phải có (bảng Seoul 1B Sheet 9)
REQUIRED_COLUMNS = [
    "từ vựng",
    "nghĩa",
    "loại từ",
    "giải thích",
    "sách",
    "khoá",
    "bài",
    "id",
]


def _cell_to_str(value: object) -> str:
    """Chuẩn hoá ô pandas thành chuỗi; NaN → ''."""
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return ""
    if pd.isna(value):
        return ""
    return str(value).strip()


def _volume_for_course_key(course_key: str) -> str:
    """Lấy nhãn quyển (1B, …) từ cột khoá; không khớp thì mặc định 1B (script này cho tập 1B)."""
    k = course_key.strip()
    return COURSE_KEY_TO_VOLUME.get(k, "1B")


def _lesson_from_row(row: pd.Series) -> str:
    """Ưu tiên cột bài (제09과…); trống thì thử đoạn cuối _tags; vẫn trống → 제09과."""
    lesson = _cell_to_str(row.get("bài"))
    if lesson:
        return lesson
    tags_raw = _cell_to_str(row.get("_tags"))
    if tags_raw and "::" in tags_raw:
        parts = [p.strip() for p in tags_raw.split("::") if p.strip()]
        if parts:
            return parts[-1]
    return "제09과"


def anki_deck_and_tags(row: pd.Series) -> tuple[str, list[str]]:
    """Deck dùng dấu cách ở '서울대 한국어'; tag dùng gạch dưới — như template Anki của bạn."""
    lesson = _lesson_from_row(row)
    vol = _volume_for_course_key(_cell_to_str(row.get("khoá")))
    deck = f"서울대 한국어::{vol}::{lesson}"
    tag_line = f"서울대_한국어::{vol}::{lesson}"
    return deck, [tag_line]


def load_vocab_dataframe(csv_path: Path) -> pd.DataFrame:
    """Đọc CSV bỏ metadata SpreadsheetImportPlus, giữ header cột tiếng Việt."""
    df = pd.read_csv(
        csv_path,
        skiprows=SKIP_ROWS,
        encoding="utf-8",
        dtype=str,
        keep_default_na=False,
    )
    df.columns = [str(c).strip() for c in df.columns]
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"CSV thiếu cột bắt buộc: {missing}. Có: {list(df.columns)}")
    return df


def dataframe_to_records(df: pd.DataFrame) -> list[dict]:
    """Lọc dòng trống (không có từ vựng), xuất đúng schema thẻ từ vựng."""
    word_col = "từ vựng"
    records: list[dict] = []
    for _, row in df.iterrows():
        word = _cell_to_str(row.get(word_col))
        if not word:
            continue
        deck, tags = anki_deck_and_tags(row)
        records.append(
            {
                "__deck__": deck,
                "__notetype__": ANKI_NOTETYPE,
                "__tags__": list(tags),
                "id": _cell_to_str(row.get("id")),
                "word": word,
                "meaning": _cell_to_str(row.get("nghĩa")),
                "pos": _cell_to_str(row.get("loại từ")),
                "transliteration": "",
                "explain": _cell_to_str(row.get("giải thích")),
                "image": "",
                "example": "",
                "example_translated": "",
                "collocation": "",
                "synonym": "",
                "antonym": "",
                "audio_word": "",
                "audio_meaning": "",
                "audio_example": "",
            }
        )
    return records


def deck_to_lesson_stem(deck: str) -> str:
    """Đoạn cuối deck kiểu 제09과 → tên file lesson-09 (không đuôi .json)."""
    if not deck:
        return "lesson-00"
    tail = deck.split("::")[-1].strip()
    m = re.match(r"제(\d+)과\s*$", tail)
    if m:
        return f"lesson-{int(m.group(1)):02d}"
    return "lesson-00"


def write_records_by_lesson(
    records: list[dict], lesson_root: Path, indent: int | None
) -> None:
    """Ghi mỗi nhóm bài vào vol-1b/lesson-XX.json (không tạo subfolder)."""
    by_lesson: dict[str, list[dict]] = defaultdict(list)
    for rec in records:
        deck = str(rec.get("__deck__", "") or "")
        by_lesson[deck_to_lesson_stem(deck)].append(rec)

    lesson_root = lesson_root.resolve()
    lesson_root.mkdir(parents=True, exist_ok=True)

    for stem in sorted(by_lesson.keys()):
        items = by_lesson[stem]
        out_file = lesson_root / f"{stem}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=indent)
            if indent:
                f.write("\n")
        rel = out_file.resolve().relative_to(REPO_ROOT)
        print(f"OK: {len(items)} items -> {rel.as_posix()}")

    # Bỏ layout cũ lesson-XX/vocabulary.json nếu còn sót
    for p in list(lesson_root.iterdir()):
        if p.is_dir() and re.fullmatch(r"lesson-\d{2}", p.name):
            shutil.rmtree(p)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Chuyển CSV từ vựng Seoul 1B (Sheet 9) sang JSON bằng pandas.",
    )
    parser.add_argument(
        "--input",
        "-i",
        type=Path,
        default=REPO_ROOT / DEFAULT_INPUT_REL,
        help="Đường dẫn file CSV nguồn (mặc định: file Sheet 9 trong vocabulary).",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=None,
        help="Nếu có: gộp toàn bộ vào một file JSON. Mặc định: seoul-korean/vol-1b/lesson-XX.json",
    )
    parser.add_argument(
        "--indent",
        type=int,
        default=2,
        help="Số space thụt dòng JSON (mặc định 2). Dùng 0 để gọn một dòng.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    csv_path = args.input.resolve()
    if not csv_path.is_file():
        print(f"Không thấy file CSV: {csv_path}", file=sys.stderr)
        sys.exit(1)

    df = load_vocab_dataframe(csv_path)
    records = dataframe_to_records(df)
    indent = None if args.indent == 0 else args.indent

    if args.output is None:
        lesson_root = REPO_ROOT / DEFAULT_LESSON_ROOT_REL
        write_records_by_lesson(records, lesson_root, indent)
        print(f"OK: total {len(records)} items -> {DEFAULT_LESSON_ROOT_REL.as_posix()}/lesson-*.json")
    else:
        out_path = args.output.resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=indent)
            if indent:
                f.write("\n")
        print(f"OK: wrote {len(records)} vocabulary items -> {out_path}")


if __name__ == "__main__":
    main()
