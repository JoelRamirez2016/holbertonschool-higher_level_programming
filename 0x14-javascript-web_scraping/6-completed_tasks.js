#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  const taskNumberCompleted = {};

  const data = error || JSON.parse(body).filter((obj) => {
    return obj.completed;
  }, 0);

  for (let i = 0; i < data.length; i++) {
    if (taskNumberCompleted[data[i].userId]) {
      taskNumberCompleted[data[i].userId] += 1;
    } else {
      taskNumberCompleted[data[i].userId] = 1;
    }
  }

  console.log(taskNumberCompleted);
});
