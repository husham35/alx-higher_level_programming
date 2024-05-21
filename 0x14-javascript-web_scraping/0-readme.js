#!/usr/bin/node
// A script that reads and prints the content of a file.

const fs = require('fs');

// check if the file to read and print content is supplied
if (process.argv.length < 3) {
  console.error('Usage: node read-file.js <file-path>');
  process.exit(1);
}

// get the full file path
const filePath = process.argv[2];

// read and print the files content
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
