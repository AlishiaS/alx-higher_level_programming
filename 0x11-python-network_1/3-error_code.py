#!/usr/bin/python3
import urllib.request
import sys
import urllib.error

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print("Response body:")
        print(body)

except urllib.error.HTTPError as e:
    print("Error code:", e.code)
