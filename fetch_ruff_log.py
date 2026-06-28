import sys, urllib.request, json
sys.stdout.reconfigure(encoding="utf-8")

# Download the lint job log
url = "https://api.github.com/repos/ssrjkk/qualix/actions/jobs/81529721879/logs"
req = urllib.request.Request(url, headers={
    "Accept": "application/vnd.github+json",
    "User-Agent": "Mozilla/5.0"
})
resp = urllib.request.urlopen(req, timeout=30)
log_data = resp.read().decode("utf-8", errors="replace")

# Find the Ruff lint section
lines = log_data.split("\n")
in_ruff = False
for line in lines:
    if "Ruff lint" in line or "ruff check" in line:
        in_ruff = True
    if in_ruff:
        print(line)
    if in_ruff and ("##[" in line or "Post " in line) and "Ruff" not in line:
        # Next section header
        if not any(x in line for x in ["Ruff lint", "ruff check"]):
            break
