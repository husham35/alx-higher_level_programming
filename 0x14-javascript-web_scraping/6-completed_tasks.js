#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

const request = require('request');

// a GET request to the API
const apiUrl = process.argv[2];

request(apiUrl, (err, response, body) => {
  if (!err) {
    const todos = JSON.parse(body);
    const completedTasks = {};
    for (const todo of todos) {
      if (todo.completed) {
        if (!completedTasks[todo.userId]) {
          completedTasks[todo.userId] = 1;
        } else {
          completedTasks[todo.userId]++;
        }
      }
    }
    console.log(completedTasks);
  }
});
