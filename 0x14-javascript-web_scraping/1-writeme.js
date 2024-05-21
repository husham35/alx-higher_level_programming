#!/usr/bin/node
/**
 * A script that writes a string to a file.
 *  - The first argument is the file path
 *  - The second argument is the string to write
 *  - The content of the file must be written in utf-8
 *  - If an error occurred during while writing, print the error object
 */

const fs = require('fs');

// check for the file path and string to write args are provided 
if (process.argv.length < 4) {
  console.error('Usage: node <script-file> <file-path> <string-to-write>');
  process.exit(1);
}

// get the file path and string to write from args
const file_path = process.argv[2];
const str_to_write = process.argv[3];

// write the file using UTF-8 encoding
fs.writeFile(file_path, str_to_write, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});