with open('public/downloads/topik/TOPIK II/36/TOPIK-2-36-transcript-utf8.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
with open('scripts/debug-output.txt', 'w', encoding='utf-8') as out:
    for i in range(35, 100):
        if i < len(lines):
            line = lines[i].strip()
            out.write(f"Line {i+1}: {repr(line)}\n")
            
print("Wrote debug output successfully.")
