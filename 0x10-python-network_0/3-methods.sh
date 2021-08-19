#!/bin/bash
# displays all HTTP methods the server will accept
curl -X OPTIONS "$1" -i | grep Allow | cut -d " " -f 2-
