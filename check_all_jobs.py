import sys, urllib.request, json
sys.stdout.reconfigure(encoding="utf-8")

# Get latest run ID
url = "https://api.github.com/repos/ssrjkk/qualix/actions/runs?per_page=1&branch=main"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
data = json.loads(resp.read())
run_id = data["workflow_runs"][0]["id"]
print(f"Run: #{data['workflow_runs'][0]['run_number']} (id={run_id})")
print(f"Status: {data['workflow_runs'][0]['status']}")
print(f"Conclusion: {data['workflow_runs'][0]['conclusion']}")

# Get jobs
url = f"https://api.github.com/repos/ssrjkk/qualix/actions/runs/{run_id}/jobs"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
d = json.loads(resp.read())

for j in d["jobs"]:
    print(f"  {j['name']}: {j['status']}/{j['conclusion']}  (id={j['id']})")
