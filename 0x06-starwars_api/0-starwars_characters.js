#!/usr/bin/node
const request = require('request');

const reqChar = (character) => {
  const url = character.shift();
  request.get(url, (err, res, body) => {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (character.length) reqChar(character);
    }
  });
};

request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`, (err, res, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    reqChar(characters);
  }
});
