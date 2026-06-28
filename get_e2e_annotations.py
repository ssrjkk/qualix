import sys, urllib.request, json
sys.stdout.reconfigure(encoding="utf-8")

# Get all annotations for the E2E check run
url = "https://api.github.com/repos/ssrjkk/qualix/check-runs/81530709735/annotations"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
annotations = json.loads(resp.read())
print(json.dumps(annotations, indent=2))
