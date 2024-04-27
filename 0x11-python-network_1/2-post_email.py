#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a `POST` request to
the passed URL with the email as a parameter,
and displays the body of the response (decoded in `utf-8`)
  * The email must be sent in the `email` variable
  * You must use the packages `urllib` and `sys`
  * You are not allowed to import packages other than `urllib` and `sys`
  * You don’t need to check arguments passed to the script (number or type)
  * You must use the `with` statement
"""
import sys
import urllib.request as req
import urllib.parse as par


if __name__ == "__main__":
    URL = sys.argv[1]
    EMAIL = sys.argv[2]
    vals = {'email': EMAIL}

    data = par.urlencode(vals).encode('ascii')
    _req = req.Request(url=URL, data=data)
    with req.urlopen(_req) as response:
        body = response.read()
        print(body.decode('utf-8'))
