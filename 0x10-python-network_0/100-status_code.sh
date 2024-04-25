#!/bin/bash
# Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
awk 'NR==1{printf "%s", $2}' headers "$(curl -sI "$1" -o headers)"
