#!/bin/bash

if [ -z "$1" ]; then
  echo "Error: URL argument is missing."
  exit 1
fi

response_file=$(mktemp)
curl -s -o "$response_file" "$1"

if [ $? -ne 0 ]; then
  echo "Error: Failed to retrieve the response."
  rm "$response_file"
  exit 1
fi

size=$(wc -c < "$response_file")

echo "Size of the response body: $size bytes"

rm "$response_file"

