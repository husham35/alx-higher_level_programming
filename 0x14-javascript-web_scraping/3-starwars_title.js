#!/usr/bin/node
// A script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');

// check for movie ID
if (process.argv.length < 3) {
  console.error('Usage: node <script-file> <ID>');
  process.exit(1);
}

// get the movie ID
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// make the GET request to the API
request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error('Error making request:', err);
    process.exit(1);
  }

  // Parse the JSON string to object
  try {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } catch (err) {
    console.error('Error parsing body:', err);
    process.exit(1);
  }
});
