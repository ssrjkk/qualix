import sys, json
d = json.load(sys.stdin)
for cr in d.get("check_runs", []):
    n = cr["name"]
    app = cr.get("app", {}).get("name", "?")
    suite_id = cr.get("check_suite", {}).get("id", "?")
    print(f"[{app}] {n} (suite={suite_id})")
