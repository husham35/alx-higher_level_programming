#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in `utf-8`).
  * You have to manage `urllib.error.HTTPError` exceptions and
    print: `Error code:` followed by the HTTP status code
  * You must use the packages `urllib` and `sys`
  * You are not allowed to import other packages than urllib and sys
  * You don’t need to check arguments passed to the script (number or type)
  * You must use the `with` statement
"""
import sys
import urllib.request as req
import urllib.error as err


if __name__ == "__main__":
    URL = sys.argv[1]

    _req = req.Request(url=URL)
    try:
        with req.urlopen(_req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except err.HTTPError as _err:
        print(f"Error code: {_err.code}")
