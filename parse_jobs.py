import sys, json
d = json.load(sys.stdin)
for j in d["jobs"]:
    c = j.get("conclusion", "?")
    print(f"{j['name']}: {c}")
