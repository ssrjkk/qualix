import sys, urllib.request, json
sys.stdout.reconfigure(encoding="utf-8")

# Get ALL check runs for the latest commit
url = "https://api.github.com/repos/ssrjkk/qualix/commits/main/check-runs?per_page=100"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=10)
d = json.loads(resp.read())

for cr in d.get("check_runs", []):
    n = cr["name"]
    c = cr.get("conclusion", "?")
    s = cr.get("status", "?")
    has_annotations = len(cr.get("output", {}).get("annotations", []))
    print(f"{n}: {s}/{c} (annotations={has_annotations})")
    # Get a snippet of the summary
    summary = cr.get("output", {}).get("summary", "")
    if summary:
        print(f"  Summary: {summary[:200]}")
    text = cr.get("output", {}).get("text", "")
    if text:
        print(f"  Text: {text[:200]}")
