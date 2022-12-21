#!/bin/bash
# displays the size of the body of the response
curl $1 -sw '%{size_download}\n' -o /dev/null
