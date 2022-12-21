#!/bin/bash
# displays the size of the body of the response
curl "$1" -s | wc -c
