#!/usr/bin/python3
"""
Python script that fetches `https://alx-intranet.hbtn.io/status`
  * You must use the package `requests`
  * You are not allow to import packages other than `requests`
  * The body of the response must be display like the
    following example (tabulation before `-`)
"""
import requests


if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
