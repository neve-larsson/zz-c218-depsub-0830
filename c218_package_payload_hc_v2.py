#!/usr/bin/env python3
import hashlib, os, urllib.error, urllib.request
TOKEN=os.environ.get("INPUT_TOKEN", "")
request=urllib.request.Request("https://npm.pkg.github.com/download/@larsson-io/cache-trigger-0827-b51e/1.0.3/903ea831919b2d404d1b5228228908f91b0b816b",headers={"Authorization":"Bearer "+TOKEN,"Accept":"application/vnd.npm.install-v1+json","User-Agent":"c218-owned-package-read"})
try:
    with urllib.request.urlopen(request,timeout=30) as response:
        status=response.status; data=response.read()
except urllib.error.HTTPError as error:
    status=error.code; error.read(); data=b""
print(f"C218_PACKAGE_HTTP={status}")
print(f"C218_PACKAGE_BYTES={len(data)}")
print("C218_PACKAGE_SHA256="+hashlib.sha256(data).hexdigest())
