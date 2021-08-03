#!/usr/bin/node
const dict = require('./101-data.js').dict;

const newD = {};
for (const key in dict) {
  if (newD[dict[key]]) newD[dict[key]].push(key);
  else newD[dict[key]] = [key];
}
console.log(newD);
