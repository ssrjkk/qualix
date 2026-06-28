import sys, urllib.request, json
sys.stdout.reconfigure(encoding="utf-8")

# Get latest run artifacts
url = "https://api.github.com/repos/ssrjkk/qualix/actions/runs?per_page=1&branch=main"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
data = json.loads(resp.read())
run_id = data["workflow_runs"][0]["id"]
print(f"Run: #{data['workflow_runs'][0]['run_number']} (id={run_id})")

url = f"https://api.github.com/repos/ssrjkk/qualix/actions/runs/{run_id}/artifacts"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
d = json.loads(resp.read())

for a in d["artifacts"]:
    print(f"  {a['name']}: {a['size_in_bytes']} bytes, id={a['id']}, expired={a.get('expired', '?')}")
