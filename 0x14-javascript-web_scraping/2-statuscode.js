#!/usr/bin/node
// A script that display the status code of a GET request.

const request = require('request');

// check for file path and URL args is provided
if (process.argv.length < 3) {
  console.error('Usage: node <script-file> <URL>');
  process.exit(1);
}

// get `URL` from command line args
const url = process.argv[2];

// make `GET` request to provided `URL`
request.get(url, (err, response) => {
  if (err) {
    console.error('Error making request:', err);
    process.exit(1);
  }

  // print the status code
  console.log(`code: ${response.statusCode}`);
});
