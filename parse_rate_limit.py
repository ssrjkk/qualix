import sys, json
d = json.load(sys.stdin)
r = d.get("resources", {}).get("core", {})
print(f'Remaining: {r.get("remaining", "?")}/{r.get("limit", "?")}')
reset = r.get("reset", 0)
import datetime
print(f"Resets at: {datetime.datetime.fromtimestamp(reset)}")
