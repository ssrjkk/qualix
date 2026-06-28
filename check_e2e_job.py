import sys, urllib.request, json
sys.stdout.reconfigure(encoding="utf-8")

job_id = 81530709735
url = f"https://api.github.com/repos/ssrjkk/qualix/actions/jobs/{job_id}"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
d = json.loads(resp.read())

print(f"Job: {d['name']}")
print(f"Conclusion: {d['conclusion']}")
for s in d["steps"]:
    c = s.get("conclusion", "?")
    print(f"  {s['name']}: {s['status']}/{c}")
