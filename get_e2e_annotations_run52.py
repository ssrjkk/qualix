import sys, urllib.request, json
sys.stdout.reconfigure(encoding="utf-8")

# Get latest run commit SHA
url = "https://api.github.com/repos/ssrjkk/qualix/actions/runs?per_page=1&branch=main"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
data = json.loads(resp.read())
run_id = data["workflow_runs"][0]["id"]
head_sha = data["workflow_runs"][0]["head_sha"]
print(f"Run: #{data['workflow_runs'][0]['run_number']}, SHA: {head_sha}")

# Get ALL check runs for this SHA
url = f"https://api.github.com/repos/ssrjkk/qualix/commits/{head_sha}/check-runs?per_page=100"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
d = json.loads(resp.read())

for cr in d.get("check_runs", []):
    n = cr["name"]
    c = cr.get("conclusion", "?")
    s = cr.get("status", "?")
    print(f"  {n}: {s}/{c} (id={cr['id']})")
    # Get annotations
    annotations_url = cr.get("output", {}).get("annotations_url", "")
    if annotations_url:
        req2 = urllib.request.Request(annotations_url, headers={"Accept": "application/vnd.github+json"})
        resp2 = urllib.request.urlopen(req2, timeout=10)
        annotations = json.loads(resp2.read())
        for a in annotations:
            msg = a.get("message", "")[:400]
            path = a.get("path", "?")
            line = a.get("start_line", "?")
            level = a.get("annotation_level", "?")
            print(f"    [{level}] {path}:{line}: {msg}")
