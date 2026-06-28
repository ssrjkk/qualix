import sys, subprocess, json, time
sys.stdout.reconfigure(encoding="utf-8")

# Use curl instead of Python urllib to avoid rate limit issues
cmd = [
    "curl", "-s", "-H", "Accept: application/vnd.github+json",
    "https://api.github.com/repos/ssrjkk/qualix/actions/runs/27578508887/jobs"
]
result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
d = json.loads(result.stdout)

for j in d["jobs"]:
    if "E2E" in j["name"]:
        print(f"E2E Job: {j['name']} (id={j['id']})")
        print(f"Conclusion: {j['conclusion']}")
        
        # Get step log for the failed step
        cr_url = j.get("check_run_url", "")
        if cr_url:
            an_url = cr_url + "/annotations"
            time.sleep(0.5)
            cmd2 = ["curl", "-s", "-H", "Accept: application/vnd.github+json", an_url]
            r2 = subprocess.run(cmd2, capture_output=True, text=True, timeout=15)
            annotations = json.loads(r2.stdout)
            for a in annotations:
                msg = a.get("message", "")[:500]
                print(f"  [{a.get('annotation_level','?')}] {msg}")
