#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url, function (error, response, body) {
  const data = error || JSON.parse(body).results.reduce((acum, val) => {
    if (val.characters.find((character) => character.includes('18'))) {
      return acum + 1;
    }
    return acum;
  }, 0);
  console.log(data);
});
