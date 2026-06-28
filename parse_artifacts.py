import sys, json
d = json.load(sys.stdin)
for a in d.get("artifacts", []):
    print(f"{a['name']}: {a['size_in_bytes']} bytes")
