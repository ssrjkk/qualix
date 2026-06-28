import sys, urllib.request, json
sys.stdout.reconfigure(encoding="utf-8")

# Try to get check run annotations for the E2E job
url = "https://api.github.com/repos/ssrjkk/qualix/actions/jobs/81530709735"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
job = json.loads(resp.read())

# Get the check run ID
if job.get("check_run_url"):
    print(f"Check run URL: {job['check_run_url']}")
    cr_url = job["check_run_url"]
    
    # Get annotations
    annotations_url = cr_url + "/annotations"
    req2 = urllib.request.Request(annotations_url, headers={"Accept": "application/vnd.github+json"})
    try:
        resp2 = urllib.request.urlopen(req2, timeout=10)
        annotations = json.loads(resp2.read())
        print(f"Found {len(annotations)} annotations")
        for a in annotations:
            print(f"  {a.get('path')}:{a.get('start_line')} - {a.get('message', '')[:200]}")
    except Exception as e:
        print(f"No annotations: {e}")
else:
    print(f"No check_run_url in job data. Keys: {list(job.keys())}")
