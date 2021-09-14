#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  const data = error || JSON.parse(body).filter((obj) => {
    return obj.completed 
  }, 0);

  task_number_completed = {}

  for (let i = 0; i < data.length; i++) {
    if (task_number_completed[data[i].userId]) {
      task_number_completed[data[i].userId] += 1;
    } else {
      task_number_completed[data[i].userId] = 1
    }
  }

  console.log(task_number_completed);
});
