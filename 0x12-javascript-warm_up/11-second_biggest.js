#!/usr/bin/node

const { argv } = require('process');

if (argv.length <= 3) {
  console.log('0');
} else {
  let numsSorted = [];
  for (let i = 2; i < argv.length; i++) {
    const curr = parseInt(argv[i]);
    numsSorted = insertSorted(curr, numsSorted);
  }
  console.log(numsSorted[numsSorted.length - 2]);
}

function insertSorted (num, arr) {
  if (!arr) {
    return [num];
  }

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= num) {
      return [...arr.slice(0, i), num, ...arr.slice(i)];
    }
  }

  return [...arr, num];
}
