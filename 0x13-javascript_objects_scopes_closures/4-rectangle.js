#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rec = '';

    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        rec += 'X';
      }
      console.log(rec);
      rec = '';
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [2 * this.width, 2 * this.height];
  }
};
