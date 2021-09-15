#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url + process.argv[2], function (error, response, body) {
  if (!error) {
    JSON.parse(body).characters.forEach(element => {
      request.get(element, function (error, response, body) {
        if (!error) console.log(JSON.parse(body).name);
      });
    });
  }
});
