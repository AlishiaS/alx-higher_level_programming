#!/bin/bash
# display methods accepted by a server
curl -sI "$1" | grep "Allow:" | cut -f2- -d' '
