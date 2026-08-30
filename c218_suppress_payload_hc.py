#!/usr/bin/env python3
import json, os, urllib.error, urllib.request
TOKEN=os.environ.get("INPUT_TOKEN", "")
print("C218_SUPPRESS_TOKEN_PRESENT=" + ("true" if len(TOKEN)>20 else "false"))
if len(TOKEN)<=20: raise SystemExit(31)
body=json.dumps({"state":"dismissed","dismissed_reason":"used in tests","dismissed_comment":"Owned C218 generated-token suppression proof; owner restores immediately"}).encode()
req=urllib.request.Request("https://api.github.com/repos/neve-larsson/zz-c218-depsub-0830/code-scanning/alerts/1",method="PATCH",data=body,headers={"Authorization":"Bearer "+TOKEN,"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2026-03-10","Content-Type":"application/json","User-Agent":"c218-owned-suppression"})
try:
  with urllib.request.urlopen(req,timeout=30) as r: status=r.status; result=json.loads(r.read() or b"{}")
except urllib.error.HTTPError as e: status=e.code; result=json.loads(e.read() or b"{}")
print(f"C218_SUPPRESS_PATCH_HTTP={status}")
print("C218_SUPPRESS_RESULT_STATE="+str(result.get("state","missing")))
raise SystemExit(0 if status==200 and result.get("state")=="dismissed" else 32)
