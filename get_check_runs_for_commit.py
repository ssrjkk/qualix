import sys, urllib.request, json
sys.stdout.reconfigure(encoding="utf-8")

# Get the commit SHA for the latest run
url = "https://api.github.com/repos/ssrjkk/qualix/actions/runs/27577728928"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
run = json.loads(resp.read())
head_sha = run["head_sha"]
print(f"Head SHA: {head_sha}")

# Get ALL check runs for this SHA
url = f"https://api.github.com/repos/ssrjkk/qualix/commits/{head_sha}/check-runs?per_page=100"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
d = json.loads(resp.read())

for cr in d.get("check_runs", []):
    n = cr["name"]
    c = cr.get("conclusion", "?")
    s = cr.get("status", "?")
    app = cr.get("app", {}).get("name", "?")
    print(f"  [{app}] {n}: {s}/{c} (id={cr['id']})")
