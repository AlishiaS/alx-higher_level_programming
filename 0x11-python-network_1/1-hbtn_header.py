#!/usr/bin/python3
import urllib.request
import sys

url = sys.argv[1]

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    headers = response.info()
    request_id = headers.get('X-Request-Id')

print("X-Request-Id:", request_id)
