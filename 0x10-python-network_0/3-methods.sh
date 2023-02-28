#!/bin/bash
# display methods accepted by a server
curl -s -I "${1}" | grep "^Allow: .*" | cut -d " " -f 2-
