#!/usr/bin/node
// A script that prints all characters of a Star Wars movie:

const request = require('request');

// get movie ID
const movieId = process.argv[2];
// API url
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

request(apiUrl + movieId, (err, response, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, (err, response, body) => {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
