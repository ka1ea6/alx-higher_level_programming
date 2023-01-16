#!/usr/bin/env bash
# Bash script that takes in a URL sends a get request
# and displays the body of the response
if [ $# -lt 1 ];
then
	echo 'Usage ./1-body.sh URL'
else
	curl -sL -X GET $1
fi
