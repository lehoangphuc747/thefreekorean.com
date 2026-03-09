"""
ANKI FLASHCARD STANDARDIZER SKILL
==================================
Tự động chuyển đổi bất kỳ file JSON nào thành format chuẩn Anki flashcard.

Usage:
    python main.py <input_file> <output_file> [config.json]

Format output:
- Mảng JSON objects
- 18 fields bắt buộc
- HTML formatting
- Ready for Anki import
"""

import json
import re
import sys
import os
from pathlib import Path

class AnkiStandardizer:
    """Chuyển đổi JSON bất kỳ thành format Anki chuẩn"""
    
    # 18 fields bắt buộc
    REQUIRED_FIELDS = [
        'id', 'topik', 'test', 'format_type', 'question_type',
        'question_form', 'question_instruction', 'question',
        'question_image', 'question_audio', 'correct',
        'answer_a', 'answer_b', 'answer_c', 'answer_d',
        'explain', 'tag_1', 'tag_2', 'tag_3', 'tag_4'
    ]
    
    def __init__(self, config=None):
        """Khởi tạo với config tùy chỉnh"""
        self.config = config or {}
        self.errors = []
    
    def standardize(self, data):
        """Chuyển đổi data sang format chuẩn"""
        if isinstance(data, dict):
            # Nếu là object, chuyển thành mảng
            if 'questions' in data:
                items = data.get('questions', [])
            else:
                items = [data]
        elif isinstance(data, list):
            items = data
        else:
            raise ValueError("Input phải là object hoặc mảng")
        
        standardized = []
        for idx, item in enumerate(items):
            try:
                std_item = self._standardize_item(item, idx)
                standardized.append(std_item)
            except Exception as e:
                self.errors.append(f"Item {idx}: {str(e)}")
                # Skip hoặc tạo item rỗng tùy config
                if self.config.get('skip_errors', True):
                    continue
        
        return standardized
    
    def _standardize_item(self, item, index):
        """Chuyển đổi một item sang format chuẩn"""
        std = {}
        
        # ID
        std['id'] = self._get_or_generate_id(item, index)
        
        # Metadata
        std['topik'] = self._extract_field(item, 'topik', self.config.get('default_topik', ''))
        std['test'] = self._extract_field(item, 'test', self.config.get('default_test', ''))
        std['format_type'] = self.config.get('default_format_type', '')
        std['question_type'] = self.config.get('default_question_type', '')
        
        # Question fields
        std['question_form'] = self.config.get('default_question_form', '')
        std['question_instruction'] = self.config.get('default_question_instruction', '')
        std['question'] = self._extract_field(item, ['question', 'question_ko', 'q'], '')
        std['question_image'] = self._extract_field(item, ['question_image', 'image', 'img'], '')
        std['question_audio'] = self._extract_field(item, ['question_audio', 'audio'], '')
        
        # Answer fields
        answers = self._extract_answers(item)
        std['answer_a'] = answers.get('a', '')
        std['answer_b'] = answers.get('b', '')
        std['answer_c'] = answers.get('c', '')
        std['answer_d'] = answers.get('d', '')
        
        # Correct answer
        std['correct'] = self._extract_correct(item)
        
        # Explanation
        std['explain'] = self._format_explain(
            self._extract_field(item, ['explain', 'explanation', 'answer'], '')
        )
        
        # Tags
        std['tag_1'] = std['topik']
        std['tag_2'] = std['test']
        std['tag_3'] = std['format_type']
        std['tag_4'] = std['question_type']
        
        return std
    
    def _get_or_generate_id(self, item, index):
        """Lấy hoặc tạo ID"""
        if 'id' in item:
            return str(item['id'])
        prefix = self.config.get('id_prefix', f'item')
        return f"{prefix}-{str(index + 1).zfill(4)}"
    
    def _extract_field(self, item, keys, default=''):
        """Lấy field từ item với multiple keys"""
        if isinstance(keys, str):
            keys = [keys]
        
        for key in keys:
            if key in item and item[key]:
                return str(item[key])
        return default
    
    def _extract_answers(self, item):
        """Extract các đáp án A, B, C, D"""
        answers = {}
        
        # Từ choices array
        if 'choices' in item and isinstance(item['choices'], list):
            for idx, choice in enumerate(item['choices'][:4]):
                key = chr(97 + idx)  # a, b, c, d
                if isinstance(choice, dict):
                    answers[key] = choice.get('text', '')
                else:
                    answers[key] = str(choice)
        
        # Từ answer_a, answer_b, etc
        for letter in ['a', 'b', 'c', 'd']:
            key = f'answer_{letter}'
            if key in item:
                answers[letter] = str(item[key])
        
        return answers
    
    def _extract_correct(self, item):
        """Extract đáp án đúng và convert sang A/B/C/D nếu cần"""
        correct = item.get('correct', item.get('answer', ''))
        
        if isinstance(correct, int):
            if 1 <= correct <= 4:
                return chr(64 + correct)  # 1→A, 2→B, 3→C, 4→D
        elif isinstance(correct, str):
            if correct.upper() in ['A', 'B', 'C', 'D']:
                return correct.upper()
        
        return ''
    
    def _format_explain(self, text):
        """Format explain sang HTML"""
        if not text:
            return ''
        
        # Replace markdown bold
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        
        # Replace newlines
        text = text.replace('\n', '<br/>')
        
        # Remove --- separator
        text = re.sub(r'<br/>---<br/>', '', text)
        
        # Wrap trong div
        return f'<div style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">{text}</div>'
    
    def validate(self, items):
        """Kiểm tra tất cả items"""
        issues = []
        
        for idx, item in enumerate(items):
            # Check required fields
            for field in self.REQUIRED_FIELDS:
                if field not in item:
                    issues.append(f"Item {idx}: Missing field '{field}'")
            
            # Check empty fields
            for field in self.REQUIRED_FIELDS:
                if not item.get(field):
                    issues.append(f"Item {idx}: Empty field '{field}'")
            
            # Check correct format
            if item.get('correct') not in ['A', 'B', 'C', 'D']:
                issues.append(f"Item {idx}: Invalid 'correct' value: {item.get('correct')}")
        
        return issues
    
    def process_file(self, input_file, output_file):
        """Main: Xử lý file input → output"""
        print(f"📂 Đọc: {input_file}")
        
        # Đọc input
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Standardize
        print(f"🔄 Chuyển đổi sang format chuẩn...")
        standardized = self.standardize(data)
        
        # Validate
        print(f"✅ Kiểm tra...")
        issues = self.validate(standardized)
        
        if issues:
            print(f"⚠️  {len(issues)} vấn đề tìm thấy:")
            for issue in issues[:10]:
                print(f"   - {issue}")
            if len(issues) > 10:
                print(f"   ... và {len(issues) - 10} vấn đề khác")
        
        # Lưu output
        print(f"💾 Lưu: {output_file}")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(standardized, f, ensure_ascii=False, indent=2)
        
        # Summary
        print(f"\n{'='*60}")
        print(f"✅ HOÀN THÀNH")
        print(f"{'='*60}")
        print(f"Items: {len(standardized)}")
        print(f"Errors: {len(self.errors)}")
        print(f"Validation issues: {len(issues)}")


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        print("Example:")
        print("  python main.py input.json output.json")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    config_file = sys.argv[3] if len(sys.argv) > 3 else None
    
    # Load config
    config = {}
    if config_file and os.path.exists(config_file):
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
    
    # Process
    standardizer = AnkiStandardizer(config)
    standardizer.process_file(input_file, output_file)


if __name__ == '__main__':
    main()
