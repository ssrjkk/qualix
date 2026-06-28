import sys, urllib.request, json
sys.stdout.reconfigure(encoding="utf-8")

# Get artifacts for latest run
url = "https://api.github.com/repos/ssrjkk/qualix/actions/runs/27577728928/artifacts"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
d = json.loads(resp.read())

for a in d["artifacts"]:
    print(f"  {a['name']}: {a['size_in_bytes']} bytes, id={a['id']}")
