#!/usr/bin/node
// A script that prints all characters of a Star Wars movie:

const request = require('request');

const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
// get movie ID
const movieId = process.argv[2];

request(apiUrl + movieId, function (err, response, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

// function to recursively print individual character
function printCharacters (characters, idx) {
  request(characters[idx], function (err, response, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (idx + 1 < characters.length) {
        printCharacters(characters, idx + 1);
      }
    }
  });
}
