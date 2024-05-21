#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file.

const fs = require('fs');
const request = require('request');

// check for file path and URL args
if (process.argv.length < 4) {
  console.error('Usage: node <script-file> <URL> <output-file>');
  process.exit(1);
}

// get file path and URL
const url = process.argv[2];
const filePath = process.argv[3];

// make a GET request to API endpoint
request.get(url, (err, response, body) => {
  if (err) {
    console.error('Error making request:', err);
    process.exit(1);
  }

  // write to file using utf-8 encoding
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
