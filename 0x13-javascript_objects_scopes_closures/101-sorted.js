#!/usr/bin/node

const dict = require('./101-data.js').dict;

const usersDict = {};

const ids = Object.values(dict);
const nbOccurences = Object.keys(dict);

ids.forEach(id => {
  usersDict[id] = [];
});

let idx = 0;
ids.forEach(id => {
  usersDict[id].push(nbOccurences[idx]);
  idx += 1;
});

console.log(usersDict);
