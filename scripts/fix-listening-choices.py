#!/usr/bin/env python3
"""Fix listening choices - clean up page numbers and section headers."""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load listening JSON
with open(r'D:\A Web\the-free-korean\public\topik2-thi-thu-35-listening.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Fix each question
for q in data['questions']:
    if q['choices']:
        cleaned_choices = []
        for choice in q['choices']:
            if isinstance(choice, dict):
                # Image choice - keep as is
                cleaned_choices.append(choice)
            else:
                # Text choice - split by newline and take first line
                lines = choice.split('\n')
                clean = lines[0].strip()
                cleaned_choices.append(clean)
        q['choices'] = cleaned_choices

# Save
with open(r'D:\A Web\the-free-korean\public\topik2-thi-thu-35-listening.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Fixed listening choices!")

# Verify Q6
q6 = next(q for q in data['questions'] if q['id'] == 6)
print(f"\nQ6 choices after fix:")
for i, c in enumerate(q6['choices']):
    if isinstance(c, dict):
        print(f"  [{i}]: [image] {c.get('text', '')}")
    else:
        print(f"  [{i}]: '{c}'")
