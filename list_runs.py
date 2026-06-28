import sys, json
d = json.load(sys.stdin)
for r in d["workflow_runs"]:
    print(f"#{r['run_number']}: id={r['id']} status={r['status']} event={r['event']} name={r.get('name','?')}")
