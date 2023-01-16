#!/bin/bash
# Bash script that takes a URL and displays all HTTP methods
# the server will accept
if [ $# -lt 1 ];
then
	echo 'Usage: ./3-method.sh URL'
else
	curl -sI $1 | grep "Allow" | cut -d " " -f 2-
fi
