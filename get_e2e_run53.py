import sys, json, urllib.request

d = json.load(sys.stdin)
for j in d["jobs"]:
    if "E2E" in j["name"]:
        print(f"Job: {j['name']} id={j['id']} conclusion={j['conclusion']}")
        for s in j["steps"]:
            a = s.get("conclusion", "?")
            print(f"  {s['name']}: {a}")
        cr = j.get("check_run_url", "")
        if cr:
            u = cr + "/annotations"
            r = urllib.request.Request(u, headers={"Accept": "application/vnd.github+json"})
            resp = urllib.request.urlopen(r, timeout=10)
            anns = json.loads(resp.read())
            print(f"  Annotations ({len(anns)}):")
            for a in anns:
                print(f"    [{a['annotation_level']}] {a.get('message','')[:300]}")
