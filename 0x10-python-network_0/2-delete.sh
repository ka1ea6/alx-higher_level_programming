#!/usr/bin/env bash
# Bash script that sends DELETE request to the
# URL passed as the first argument
if [ $# -lt 1 ];
then
	echo 'Usage: ./2-delete.sh URL'
else
	curl -s -X DELETE $1
fi
