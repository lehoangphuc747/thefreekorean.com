"""
Một lần / tái chạy: thêm __deck__, __notetype__, __tags__, transliteration
vào thth-02-bai-04.json theo thứ tự bảng trong thth-02-bai-04.md (không đổi nội dung field cũ).

Chạy từ repo root:
  python scripts/thth_bai04_add_anki_fields.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MD_PATH = REPO_ROOT / "src/content/vocabulary/tieng-han-tong-hop/quyen-2/thth-02-bai-04.md"
JSON_PATH = REPO_ROOT / "src/content/vocabulary/tieng-han-tong-hop/quyen-2/thth-02-bai-04.json"

DECK_BASE = "Tiếng Hàn Tổng Hợp::Quyển 02::Bài 04. Bệnh viện (병원)::"

# Đúng chuỗi user cung cấp (mục 01–14)
SECTION_SUFFIX: dict[int, str] = {
    1: "01. Đầu và khuôn mặt (머리 & 얼굴)",
    2: "02. Thân người (몸통)",
    3: "03. Tay (팔 & 손)",
    4: "04. Chân (다리 & 발)",
    5: "05. Cảm cúm (감기)",
    6: "06. Tiêu hoá (소화)",
    7: "07. Vết thương và chấn thương (상처 & 부상)",
    8: "08. Cơn đau và cảm giác (통증 & 감각)",
    9: "09. Thuốc (약)",
    10: "10. Cách dùng thuốc",
    11: "11. Khoa trong bệnh viện",
    12: "12. Hoạt động tại bệnh viện",
    13: "13. Cách nói thường dùng tại bệnh viện, hiệu thuốc",
    14: "14. Liệu pháp dân gian (민간요법)",
}

ANKI_NOTETYPE = "(Anki) Template học từ vựng của Admin Phúc [2026]"


def _collapse_to_underscore(s: str) -> str:
    """Khoảng trắng và dấu phẩy → một dấu _ giữa các từ."""
    s = s.replace(",", " ").replace("  ", " ")
    return "_".join(s.split())


def _korean_in_parens_tail(rest: str) -> tuple[str, str | None]:
    """
    'Bệnh viện (병원)' -> ('Bệnh viện', '병원')
    'Tay (팔 & 손)' -> ('Tay', '팔 & 손')
    """
    rest = rest.strip()
    if "(" not in rest or not rest.endswith(")"):
        return rest, None
    idx = rest.rindex("(")
    vi = rest[:idx].strip()
    ko = rest[idx + 1 : -1].strip()
    return vi, ko


def _ko_part_to_tag(ko: str) -> str:
    """'머리 & 얼굴' / '팔 & 손' -> 머리_얼굴 / 팔_손"""
    t = ko.replace(" & ", "_").replace("&", "_")
    t = t.replace(",", " ")
    return "_".join(t.split())


def deck_to_thth_tag(deck: str) -> str:
    """
    Biến deck Anki thành một tag phân cấp (một chuỗi), ví dụ:
    Tiếng Hàn Tổng Hợp::Quyển 02::Bài 04. Bệnh viện (병원)::01. Đầu và khuôn mặt (머리 & 얼굴)
    -> THTH::Quyển_02::Bài_04_Bệnh_viện_병원::01_Đầu_và_khuôn_mặt_머리_얼굴
    """
    parts = [p.strip() for p in deck.split("::")]
    if len(parts) != 4:
        return "::".join(_collapse_to_underscore(p) for p in parts)

    series, quyen_raw, bai_raw, muc_raw = parts

    if series == "Tiếng Hàn Tổng Hợp":
        tag_series = "THTH"
    else:
        tag_series = _collapse_to_underscore(series)

    m_q = re.match(r"^Quyển\s+(\d+)$", quyen_raw)
    tag_quyen = f"Quyển_{int(m_q.group(1)):02d}" if m_q else _collapse_to_underscore(quyen_raw)

    m_b = re.match(r"^Bài\s+(\d+)\.\s*(.+)$", bai_raw)
    if m_b:
        n_bai = int(m_b.group(1))
        rest_b = m_b.group(2).strip()
        vi_b, ko_b = _korean_in_parens_tail(rest_b)
        if ko_b is not None:
            tag_bai = f"Bài_{n_bai:02d}_{_collapse_to_underscore(vi_b)}_{_ko_part_to_tag(ko_b)}"
        else:
            tag_bai = f"Bài_{n_bai:02d}_{_collapse_to_underscore(rest_b)}"
    else:
        tag_bai = _collapse_to_underscore(bai_raw)

    m_m = re.match(r"^(\d+)\.\s*(.+)$", muc_raw)
    if m_m:
        n_m = int(m_m.group(1))
        rest_m = m_m.group(2).strip()
        vi_m, ko_m = _korean_in_parens_tail(rest_m)
        if ko_m is not None:
            tag_muc = f"{n_m:02d}_{_collapse_to_underscore(vi_m)}_{_ko_part_to_tag(ko_m)}"
        else:
            tag_muc = f"{n_m:02d}_{_collapse_to_underscore(rest_m)}"
    else:
        tag_muc = _collapse_to_underscore(muc_raw)

    return "::".join([tag_series, tag_quyen, tag_bai, tag_muc])


def _parse_md_word_order(path: Path) -> list[tuple[str, int]]:
    text = path.read_text(encoding="utf-8")
    section: int | None = None
    ordered: list[tuple[str, int]] = []
    for line in text.splitlines():
        m = re.match(r"^## (\d+)\.", line)
        if m:
            section = int(m.group(1))
            continue
        s = line.strip()
        if not s.startswith("|"):
            continue
        inner = [p.strip() for p in s.strip("|").split("|")]
        if len(inner) < 5:
            continue
        w = inner[0]
        if w == "한국어":
            continue
        if set(w) <= {"-", ":"} or w.replace("-", "").replace(":", "").strip() == "":
            continue
        if section is None:
            continue
        ordered.append((w, section))
    return ordered


def _assign_sections(data: list[dict], ordered: list[tuple[str, int]]) -> list[int]:
    """
    Trả về list section (1–14) cùng độ dài data.

    Lưu ý: JSON không nhất thiết cùng thứ tự với bảng trong MD, nên không thể "khớp song song".
    Cách làm đúng là tra cứu theo word -> section.
    """
    word_to_section = _build_word_to_section_map(ordered)
    sections: list[int] = []
    for item in data:
        w = item["word"]
        sections.append(word_to_section.get(w, 14))
    return sections


def _build_word_to_section_map(ordered: list[tuple[str, int]]) -> dict[str, int]:
    """
    Build map word -> section.

    - Nếu một từ xuất hiện nhiều lần trong MD, giữ lần xuất hiện đầu tiên (ổn định hơn).
    - Các từ chỉ có trong JSON sẽ được fallback về mục 14.
    """
    m: dict[str, int] = {}
    for w, sec in ordered:
        if w not in m:
            m[w] = sec
    return m


def main() -> None:
    ordered = _parse_md_word_order(MD_PATH)
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    section_per_row = _assign_sections(data, ordered)

    # CRITICAL:
    # - KHÔNG rebuild item theo schema mới (sẽ làm rơi __guid__, audio_*, tag_*...).
    # - Chỉ update 3 field Anki routing: __deck__, __notetype__, __tags__.
    out: list[dict] = []
    for item, sec in zip(data, section_per_row, strict=True):
        suffix = SECTION_SUFFIX.get(sec, SECTION_SUFFIX[14])
        deck = DECK_BASE + suffix

        # Giữ nguyên mọi field cũ (đặc biệt __guid__), chỉ ghi đè 3 field điều hướng.
        item["__deck__"] = deck
        item["__notetype__"] = ANKI_NOTETYPE
        item["__tags__"] = [deck_to_thth_tag(deck)]
        out.append(item)

    JSON_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK: updated {len(out)} items -> {JSON_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
