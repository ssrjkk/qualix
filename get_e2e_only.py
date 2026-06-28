import sys, urllib.request, json, time
sys.stdout.reconfigure(encoding="utf-8")

head_sha = "117cc6f27bf6c1af6fc362575e386fa5197aae4b"

# Get check runs for this SHA
url = f"https://api.github.com/repos/ssrjkk/qualix/commits/{head_sha}/check-runs?per_page=100"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
d = json.loads(resp.read())

for cr in d.get("check_runs", []):
    n = cr["name"]
    c = cr.get("conclusion", "?")
    s = cr.get("status", "?")
    # Skip entries where name contains specific patterns
    if "E2E" in n or "e2e" in n:
        print(f"E2E CHECK RUN: {n}: {s}/{c} (id={cr['id']})")
        annotations_url = cr.get("output", {}).get("annotations_url", "")
        if annotations_url:
            try:
                time.sleep(0.5)
                req2 = urllib.request.Request(annotations_url, headers={"Accept": "application/vnd.github+json"})
                resp2 = urllib.request.urlopen(req2, timeout=10)
                annotations = json.loads(resp2.read())
                for a in annotations:
                    msg = a.get("message", "")[:600]
                    path = a.get("path", "?")
                    line = a.get("start_line", "?")
                    level = a.get("annotation_level", "?")
                    title = a.get("title", "")
                    print(f"    [{level}] {title}: {msg}")
            except Exception as e:
                print(f"    Error: {e}")
