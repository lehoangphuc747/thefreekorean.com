# ANKI FLASHCARD STANDARDIZER SKILL

## Mô tả
Chuyển đổi **bất kỳ file JSON nào** thành **format chuẩn Anki flashcard** với 18 fields bắt buộc và HTML formatting.

## Cách sử dụng

### 1. **Basic usage** (với config mặc định)
```bash
python anki_standardizer.py input.json output.json
```

### 2. **Với config tùy chỉnh**
```bash
python anki_standardizer.py input.json output.json config.json
```

### 3. **Ví dụ thực tế**
```bash
python anki_standardizer.py id-13-82.json id-13-82-standardized.json anki_config.json
```

## Input Format
Có thể là bất kỳ format nào:

### Format 1: Mảng objects
```json
[
  {
    "id": "1",
    "question": "Câu hỏi 1",
    "answer": 1,
    "choices": [{"text": "A"}, {"text": "B"}],
    "explain": "Giải thích"
  }
]
```

### Format 2: Object với questions nested
```json
{
  "meta": {"title": "..."},
  "questions": [
    {...},
    {...}
  ]
}
```

### Format 3: Bất kỳ structure nào
Skill sẽ cố gắng extract từ các field keywords.

## Output Format
**Luôn là:** Mảng JSON objects với 18 fields

```json
[
  {
    "id": "string",
    "topik": "string",
    "test": "string",
    "format_type": "string",
    "question_type": "string",
    "question_form": "string (HTML)",
    "question_instruction": "string (HTML)",
    "question": "string",
    "question_image": "string (URL)",
    "question_audio": "string (URL)",
    "correct": "A/B/C/D",
    "answer_a": "string",
    "answer_b": "string",
    "answer_c": "string",
    "answer_d": "string",
    "explain": "string (HTML)",
    "tag_1": "string",
    "tag_2": "string",
    "tag_3": "string",
    "tag_4": "string"
  }
]
```

## Config File (anki_config.json)

```json
{
  "default_topik": "TOPIK II",
  "default_format_type": "ĐỌC",
  "default_question_type": "DẠNG 01",
  "default_question_form": "( )에 들어갈 가장 알맞은 것을 고르십시오.",
  "default_question_instruction": "<h3>Hướng dẫn</h3>...",
  "default_test": "",
  "id_prefix": "topik-reading-dang-01-id",
  "skip_errors": true
}
```

## Features

✅ **Flexible Input**
- Nhận bất kỳ format JSON nào
- Tự động detect và extract fields

✅ **Smart Mapping**
- Auto convert số (1-4) → A/B/C/D
- Extract từ multiple field names
- Fallback to defaults

✅ **HTML Formatting**
- Replace markdown bold → `<strong>`
- Newlines → `<br/>`
- Remove separators (`---`)
- Wrap trong styled `<div>`

✅ **Validation**
- Check tất cả 18 required fields
- Detect empty fields
- Report errors chi tiết

✅ **Customizable**
- Config file cho defaults
- Tùy chỉnh ID prefix
- Error handling options

## Advanced: Python API

```python
from anki_standardizer import AnkiStandardizer

# Load config
config = {
    "default_topik": "TOPIK II",
    "id_prefix": "my-card-id"
}

# Create standardizer
standardizer = AnkiStandardizer(config)

# Process
standardizer.process_file('input.json', 'output.json')

# Or manual
data = [
    {"question": "Q1", "answer": 1, "choices": [...]},
    {"question": "Q2", "answer": 2, "choices": [...]}
]
standardized = standardizer.standardize(data)

# Validate
issues = standardizer.validate(standardized)
print(f"Issues: {len(issues)}")
```

## Workflow

```
Input JSON (any format)
        ↓
Standardize (extract + convert)
        ↓
Format HTML
        ↓
Validate
        ↓
Output JSON (18 fields, ready for Anki)
```

## Troubleshooting

**Problem:** "Missing field 'answer_a'"
- **Solution:** Chắc chắn input có đáp án A, hoặc thêm vào config mặc định

**Problem:** "Invalid 'correct' value"
- **Solution:** `correct` phải là 1/2/3/4 (auto convert) hoặc A/B/C/D

**Problem:** HTML không render đúng
- **Solution:** Check `explain` hoặc `question_instruction` có valid HTML tags không

## License
MIT - Sử dụng tự do cho mục đích học tập

