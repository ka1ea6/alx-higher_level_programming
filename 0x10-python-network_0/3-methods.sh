#!/bin/bash
# Bash script that takes a URL and displays all HTTP methods
curl -sI $1 | grep "Allow" | cut -d " " -f 2-
