#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

request.get(
  `https://swapi-api.alx-tools.com/api/films/${movieId}`,
  async (err, res, body) => {
    if (err) console.error(err);
    else {
      const film = JSON.parse(body);

      for (const character of film.characters) {
        request.get(character, (err, res, body) => {
          if (err) console.error(err);
          const char = JSON.parse(body);
          console.log(char.name);
        });
      }
    }
  }
);
