#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

const request = require('request');

// API URL
const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

// a GET request to the API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error making the request:', error);
    process.exit(1);
  }

  try {
    // pars the JSON response
    const todos = JSON.parse(body);

    const completedTasksByUser = {};

    // filster and count completed tasks
    todos.forEach((todo) => {
      if (todo.completed) {
        if (!completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId] = 1;
        } else {
          completedTasksByUser[todo.userId]++;
        }
      }
    });

    // Print the number of completed tasks by each user
    console.log(completedTasksByUser);
	
  } catch (parseError) {
    console.error('Error parsing JSON response:', parseError);
    process.exit(1);
  }
});
