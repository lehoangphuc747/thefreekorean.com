#!/usr/bin/env python3
"""Split TOPIK 35 exam JSON into 3 separate files."""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load source
with open(r'D:\A Web\the-free-korean\src\content\topik\thi-thu\topik2-thi-thu-35.json', 'r', encoding='utf-8') as f:
    exam = json.load(f)

meta = exam['meta']
sections = exam['sections']

# Find each section
listening = next((s for s in sections if s['type'] == 'listening'), None)
reading = next((s for s in sections if s['type'] == 'reading'), None)
writing = next((s for s in sections if s['type'] == 'writing'), None)

# Create separate files
files = {
    'listening': {
        'meta': {
            'title': meta['title'],
            'level': meta['level'],
            'duration': listening['duration'] if listening else 60,
            'totalQuestions': len(listening['questions']) if listening else 0,
        },
        'type': 'listening',
        'audio': listening.get('audio', '') if listening else '',
        'questions': listening['questions'] if listening else []
    },
    'reading': {
        'meta': {
            'title': meta['title'],
            'level': meta['level'],
            'duration': reading['duration'] if reading else 50,
            'totalQuestions': len(reading['questions']) if reading else 0,
        },
        'type': 'reading',
        'questions': reading['questions'] if reading else []
    },
    'writing': {
        'meta': {
            'title': meta['title'],
            'level': meta['level'],
            'duration': writing['duration'] if writing else 50,
            'totalQuestions': len(writing['questions']) if writing else 0,
        },
        'type': 'writing',
        'questions': writing['questions'] if writing else []
    }
}

# Save files
public_dir = r'D:\A Web\the-free-korean\public'
for section_type, data in files.items():
    filename = f'topik2-thi-thu-35-{section_type}.json'
    filepath = f'{public_dir}\\{filename}'
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'✅ Created {filename} ({data["meta"]["totalQuestions"]} questions)')

print('\nDone!')
