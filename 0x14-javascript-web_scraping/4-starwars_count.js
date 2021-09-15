#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  const data = error || JSON.parse(body).results.reduce((acum, val) => {
    if (val.characters.find((character) => character.includes('18'))) {
      return acum + 1;
    }
    return acum;
  }, 0);
  console.log(data);
});
