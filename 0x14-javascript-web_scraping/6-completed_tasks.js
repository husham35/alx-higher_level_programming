#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

const request = require('request');

// define the API URL
const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

// make a GET request to the API
request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error('Error making the request:', err);
    process.exit(1);
  }

  try {
    // parse the JSON response
    const todos = JSON.parse(body);

    // store the number of completed tasks by user ID
    const completedTasksByUser = {};

    // fileter and count completed tasks
    todos.forEach((todo) => {
      if (todo.completed) {
        if (!completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId] = 1;
        } else {
          completedTasksByUser[todo.userId]++;
        }
      }
    });

    // print completed tasks by each user
    console.log(completedTasksByUser);
  } catch (parseError) {
    console.error('Error parsing JSON response:', parseError);
    process.exit(1);
  }
});
