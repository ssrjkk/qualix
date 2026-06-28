import urllib.request, json

url = "https://api.github.com/repos/ssrjkk/qualix/actions/runs?per_page=5&branch=main&status=completed"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
data = json.loads(resp.read())
for run in data["workflow_runs"][:3]:
    print(f"#{run['run_number']}: {run['conclusion']} ({run['html_url']})")
