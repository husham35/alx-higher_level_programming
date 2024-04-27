#!/usr/bin/python3
"""
Python script that fetches `https://alx-intranet.hbtn.io/status`
  * You must use the package `urllib`
  * You are not allowed to import any packages other than `urllib`
  * The body of the response must be displayed like
    the following example (tabulation before -)
  * You must use a `with` statement
"""
import urllib.request as req

if __name__ == "__main__":
    _req = req.Request("https://alx-intranet.hbtn.io/status")
    with req.urlopen(_req) as response:
        html_body = response.read()
        print("Body response:")
        print(f"\t- type: {type(html_body)}")
        print(f"\t- content: {html_body}")
        print(f"\t-  utf8 content: {html_body.decode('utf-8')}")
