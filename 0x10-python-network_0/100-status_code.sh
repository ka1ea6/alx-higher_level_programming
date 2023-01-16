#!/bin/bash
# Bash script that sends a request and displas status code
curl -so /dev/null -w "%{http_code}\n" "$1"
