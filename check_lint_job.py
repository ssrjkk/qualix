import sys, urllib.request, json
sys.stdout.reconfigure(encoding="utf-8")

# Get jobs for run #50
url = "https://api.github.com/repos/ssrjkk/qualix/actions/runs/27577424040/jobs"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
d = json.loads(resp.read())

# Find lint job id
for j in d["jobs"]:
    if "Lint" in j["name"] or "Types" in j["name"]:
        print(f"Job: {j['name']} (id={j['id']})")
        print(f"Conclusion: {j['conclusion']}")
        print(f"Steps:")
        for s in j["steps"]:
            conclusion = s.get("conclusion", "?")
            status = s["status"]
            print(f"  {s['name']}: {status}/{conclusion}")
