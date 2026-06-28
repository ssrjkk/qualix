import sys, urllib.request, json, io, zipfile
sys.stdout.reconfigure(encoding="utf-8")

artifact_id = 7651423948  # e2e-debug-logs
url = f"https://api.github.com/repos/ssrjkk/qualix/actions/artifacts/{artifact_id}/zip"
req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
resp = urllib.request.urlopen(req, timeout=30)
data = resp.read()
print(f"Downloaded {len(data)} bytes")
z = zipfile.ZipFile(io.BytesIO(data))
for name in z.namelist():
    print(f"=== {name} ===")
    print(z.read(name).decode("utf-8", errors="replace"))
