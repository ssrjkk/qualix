import sys, urllib.request, json
sys.stdout.reconfigure(encoding="utf-8")

# Get latest run
url = "https://api.github.com/repos/ssrjkk/qualix/actions/runs?per_page=1&branch=main"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
data = json.loads(resp.read())
run_id = data["workflow_runs"][0]["id"]
print(f"Run: #{data['workflow_runs'][0]['run_number']} (id={run_id})")

# Get E2E job
url = f"https://api.github.com/repos/ssrjkk/qualix/actions/runs/{run_id}/jobs"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
d = json.loads(resp.read())

for j in d["jobs"]:
    if "E2E" in j["name"]:
        print(f"\nE2E Job: {j['name']} (id={j['id']})")
        print(f"Conclusion: {j['conclusion']}")
        for s in j["steps"]:
            c = s.get("conclusion", "?")
            print(f"  {s['name']}: {s['status']}/{c}")

        # Get annotations
        cr_url = j.get("check_run_url", "")
        if cr_url:
            an_url = cr_url + "/annotations"
            req2 = urllib.request.Request(an_url, headers={"Accept": "application/vnd.github+json"})
            resp2 = urllib.request.urlopen(req2, timeout=10)
            annotations = json.loads(resp2.read())
            print(f"\n  Annotations ({len(annotations)}):")
            for a in annotations:
                msg = a.get("message", "")[:300]
                path = a.get("path", "?")
                line = a.get("start_line", "?")
                level = a.get("annotation_level", "?")
                print(f"    [{level}] {path}:{line}: {msg}")
