import sys, urllib.request, json
sys.stdout.reconfigure(encoding="utf-8")

# Try to get annotations for the run
url = "https://api.github.com/repos/ssrjkk/qualix/check-runs?check_name=E2E%20Tests%20(Playwright)"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
d = json.loads(resp.read())
print(json.dumps(d, indent=2)[:2000])
