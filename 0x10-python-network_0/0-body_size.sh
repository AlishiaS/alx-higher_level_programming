#!/bin/bash
# ends a request to that URL displays the size of the response body
curl -s "$1" | wc -c
