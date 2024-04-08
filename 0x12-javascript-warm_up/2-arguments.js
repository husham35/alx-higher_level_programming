#!/usr/bin/node

const { argv } = require('process');
const argsLen = argv.length;

if (argsLen === 2) {
  console.log('No argument');
} else if (argsLen === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
