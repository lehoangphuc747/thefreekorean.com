#!/usr/bin/env python3
"""Fix reading choices - clean up page numbers and section headers."""
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load reading JSON
with open(r'D:\A Web\the-free-korean\public\topik2-thi-thu-35-reading.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Fix each question
for q in data['questions']:
    if q['choices']:
        cleaned_choices = []
        for choice in q['choices']:
            # Split by newline and take only first line (the actual choice)
            lines = choice.split('\n')
            # First line is the choice text
            clean = lines[0].strip()
            # If there are more lines, they are noise (page numbers, headers)
            cleaned_choices.append(clean)
        q['choices'] = cleaned_choices

# Save
with open(r'D:\A Web\the-free-korean\public\topik2-thi-thu-35-reading.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Fixed reading choices!")

# Verify Q10
q10 = next(q for q in data['questions'] if q['id'] == 10)
print(f"\nQ10 choices after fix:")
for i, c in enumerate(q10['choices']):
    print(f"  [{i}]: '{c}'")
