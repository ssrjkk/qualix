import sys, urllib.request, json
sys.stdout.reconfigure(encoding="utf-8")

url = "https://api.github.com/repos/ssrjkk/qualix/actions/runs/27577424040/jobs"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
d = json.loads(resp.read())
for j in d["jobs"]:
    print(f"{j['name']}: {j['status']} / {j['conclusion']}")
