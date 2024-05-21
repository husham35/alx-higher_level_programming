#!/usr/bin/node
// A script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');

// check for the API URL
if (process.argv.length < 3) {
  console.error('Usage: node <script-file> <URL>');
  process.exit(1);
}

// get URL
const apiUrl = process.argv[2];

// make a GET request to API endpoint
request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error('Error making request:', err);
    process.exit(1);
  }

  // parse the JSON string to object
  try {
    let count = 0;
    const charId = 18;
    const movies = JSON.parse(body);
    for (const movie of movies.results) {
      for (const character of movie.characters) {
        if (character.includes(charId)) {
          count++;
        }
      }
    }
    console.log(count);
  } catch (err) {
    console.error('Error parsing body:', err);
    process.exit(1);
  }
});
