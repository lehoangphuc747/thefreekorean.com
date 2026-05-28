"""One-off: compare bai-04.md table order vs thth-02-bai-04.json."""
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
md_path = REPO / "src/content/vocabulary/tieng-han-tong-hop/quyen-2/thth-02-bai-04.md"
jpath = REPO / "src/content/vocabulary/tieng-han-tong-hop/quyen-2/thth-02-bai-04.json"

md = md_path.read_text(encoding="utf-8")
lines = md.splitlines()
section = None
ordered: list[tuple[str, int]] = []
for line in lines:
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

data = json.loads(jpath.read_text(encoding="utf-8"))
log: list[str] = [f"md={len(ordered)} json={len(data)}"]
for i in range(min(len(ordered), len(data))):
    if ordered[i][0] != data[i]["word"]:
        log.append(f"i={i} md={ordered[i][0]!r} json={data[i]['word']!r}")
        break
else:
    if len(ordered) != len(data):
        log.append(f"json has {len(data) - len(ordered)} extra rows")
        for j in range(len(ordered), len(data)):
            log.append(f"extra[{j}] {data[j]['word']!r} id={data[j].get('id')}")

out = REPO / "src/content/vocabulary/tieng-han-tong-hop/quyen-2/_debug_match.txt"
out.write_text("\n".join(log), encoding="utf-8")
print("\n".join(log))
