#!/usr/bin/node
// A script that writes a string to a file

const fs = require('fs');

// check for the file path and string to write args are provided
if (process.argv.length < 4) {
  console.error('Usage: node <script-file> <file-path> <string-to-write>');
  process.exit(1);
}

// get the file path and string to write from args
const filePath = process.argv[2];
const strToWrite = process.argv[3];

// write the file using UTF-8 encoding
fs.writeFile(filePath, strToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
