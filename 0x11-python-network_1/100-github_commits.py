#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
  * The first argument will be the `repository name`
  * The second argument will be the `owner name`
  * You must use the packages `requests` and `sys`
  * You are not allowed to import packages other than `requests` and `sys`
  * You don’t need to check arguments passed to the script (number or type)
"""
import sys
import requests


if __name__ == "__main__":
	REPO_NAME = sys.argv[1]
	OWNER_NAME = sys.argv[2]
	URL = f"https://api.github.com/repos/{OWNER_NAME}/{REPO_NAME}/commits"

	response = requests.get(URL, timeout=5)
	commits = response.json()
	for index, commit in enumerate(commits):
		if index == 10:
			break
		sha = commit.get("sha")
		author =commit.get("commit").get("author").get("name")
		print(f"{sha}: {author}")
