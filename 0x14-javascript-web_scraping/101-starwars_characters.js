#!/usr/bin/node

const request = require('request');
const util = require('node:util');

const req = util.promisify(request.get);

const movieId = process.argv[2];

(async () => {
  const movie = await req(
    `https://swapi-api.alx-tools.com/api/films/${movieId}`
  );
  const characters = JSON.parse(movie.body).characters;
  const charAndName = {};
  for (const char of characters) {
    const character = await req(char);
    const parsedChar = JSON.parse(character.body);
    charAndName[parsedChar.url] = parsedChar.name;
  }

  for (const char of characters) {
    console.log(charAndName[char]);
  }
})();
