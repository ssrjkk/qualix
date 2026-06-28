import sys, urllib.request, json
sys.stdout.reconfigure(encoding="utf-8")

# Get check runs for the latest commit on main
url = "https://api.github.com/repos/ssrjkk/qualix/commits/main/check-runs"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
d = json.loads(resp.read())

for cr in d.get("check_runs", []):
    name = cr["name"]
    conclusion = cr.get("conclusion", "?")
    status = cr.get("status", "?")
    if "E2E" in name or "e2e" in name:
        print(f"{name}: {status}/{conclusion} (id={cr['id']})")
        annotations_url = cr["output"].get("annotations_url", "")
        if annotations_url:
            req2 = urllib.request.Request(annotations_url, headers={"Accept": "application/vnd.github+json"})
            resp2 = urllib.request.urlopen(req2, timeout=10)
            annotations = json.loads(resp2.read())
            print(f"  Annotations ({len(annotations)}):")
            for a in annotations:
                msg = a.get("message", "")[:300]
                path = a.get("path", "?")
                line = a.get("start_line", "?")
                level = a.get("annotation_level", "?")
                print(f"    [{level}] {path}:{line}: {msg}")
