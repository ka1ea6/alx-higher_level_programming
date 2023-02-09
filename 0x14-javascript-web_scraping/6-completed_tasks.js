#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (err, res, body) => {
  const todos = JSON.parse(body);
  const resObj = {};

  for (const todo of todos) {
    if (todo.completed) {
      if (!resObj[todo.userId]) resObj[todo.userId] = 1;
      else resObj[todo.userId] += 1;
    }
  }

  console.log(resObj);
});
