#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
request.get(
  `https://swapi-api.alx-tools.com/api/films/${movieId}`,
  (err, res, body) => {
    const parsed = JSON.parse(body);
    console.log(parsed.title);
  }
);
