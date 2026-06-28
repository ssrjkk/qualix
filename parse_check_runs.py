import sys, json
d = json.load(sys.stdin)
for cr in d.get("check_runs", []):
    n = cr["name"]
    c = cr.get("conclusion", "?")
    s = cr.get("status", "?")
    print(f"{n}: {s}/{c}")
    output = cr.get("output", {})
    for a in output.get("annotations", []):
        msg = a.get("message", "")[:400]
        level = a["annotation_level"]
        print(f"  [{level}] {msg}")
