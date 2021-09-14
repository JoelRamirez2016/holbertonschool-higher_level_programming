#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url + process.argv[2], function (error, response, body) {
  const data = error || JSON.parse(body).title;
  console.log(data);
});
