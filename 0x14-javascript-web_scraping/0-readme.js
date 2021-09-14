#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], function (err, content) {
  const data = err || content.toString('utf-8');
  console.log(data);
});
