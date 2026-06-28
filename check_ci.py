import urllib.request, json

url = "https://api.github.com/repos/ssrjkk/qualix/actions/runs?per_page=1&branch=main"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
data = json.loads(resp.read())
run = data["workflow_runs"][0]
print(f"Run #{run['run_number']}: {run['status']} / {run['conclusion']}")
print(f"URL: {run['html_url']}")
