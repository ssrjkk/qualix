import sys, json
d = json.load(sys.stdin)
r = d["workflow_runs"][0]
print(f"#{r['run_number']}: {r['status']} / {r['conclusion']}")
