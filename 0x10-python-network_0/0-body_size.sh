#!/bin/bash
# Script to take in a URL and send a request to that URL
if [ $# -lt 1 ];
then
	echo 'Usage: ./0-body_size.sh URL'
else
	curl -s $1 | wc -c
fi
