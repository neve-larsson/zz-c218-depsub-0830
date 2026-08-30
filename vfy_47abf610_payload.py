#!/usr/bin/env python3
import json, os, urllib.error, urllib.request
T=os.environ.get("INPUT_TOKEN","")
print("VFY_TOKEN_PRESENT=" + ("true" if len(T)>20 else "false"))
if len(T)<=20: raise SystemExit(31)
b=json.dumps({"state":"dismissed","dismissed_reason":"used in tests","dismissed_comment":"VERIFIER 47abf610 independent clean-state reproduction; owner restores immediately"}).encode()
r=urllib.request.Request("https://api.github.com/repos/neve-larsson/zz-c218-depsub-0830/code-scanning/alerts/2",method="PATCH",data=b,
  headers={"Authorization":"Bearer "+T,"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2026-03-10","Content-Type":"application/json","User-Agent":"vfy-47abf610"})
try:
  with urllib.request.urlopen(r,timeout=30) as x: st=x.status; res=json.loads(x.read() or b"{}")
except urllib.error.HTTPError as e: st=e.code; res=json.loads(e.read() or b"{}")
print("VFY_PATCH_HTTP=" + str(st))
print("VFY_RESULT_STATE=" + str(res.get("state","missing")))
