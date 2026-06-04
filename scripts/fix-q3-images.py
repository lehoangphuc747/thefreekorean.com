#!/usr/bin/env python3
"""Fix Q3 listening images."""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'D:\A Web\the-free-korean\public\topik2-thi-thu-35-listening.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Fix Q3 images - use page4 images
data['questions'][2]['choices'] = [
    {'type': 'image', 'text': '①', 'image': '/images/topik/35/page4-img1.jpeg'},
    {'type': 'image', 'text': '②', 'image': '/images/topik/35/page4-img2.jpeg'},
    {'type': 'image', 'text': '③', 'image': '/images/topik/35/page4-img3.jpeg'},
    {'type': 'image', 'text': '④', 'image': '/images/topik/35/page4-img4.jpeg'}
]

with open(r'D:\A Web\the-free-korean\public\topik2-thi-thu-35-listening.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Fixed Q3 images!")
for c in data['questions'][2]['choices']:
    print(f"  {c['text']}: {c['image']}")
