#!/bin/bash
# sends a POST request to the passed URL, and displays the body of the response
curl -s -X POST -d "email=yest@gmail.com&sybject=I will always be here for PLD" "$1"
