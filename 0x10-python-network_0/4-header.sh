#!/usr/bin/env bash
# Bash script that takes in a URL as an argument, sends a
# GET request to the URL and displays the body of the
# response
if [ $# -lt 1 ];
then
	echo 'Usage ./4-headers.sh URL'
else
	curl -sH "X-School-User-Id: 98" $1
fi
