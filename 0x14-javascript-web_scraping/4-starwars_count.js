#!/usr/bin/node

const request = require("request");

const uri = process.argv[2];

request.get(uri, (err, res, body) => {
  const movies = JSON.parse(body).results;

  let movieCount = 0;

  for (let episode of movies) {
    for (let character of episode.characters) {
      if (character.includes("18")) {
        movieCount++;
        break;
      }
    }
  }

  console.log(movieCount);
});
