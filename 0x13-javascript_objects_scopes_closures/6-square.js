#!/usr/bin/node

const SquareI = require('./5-square');

class Square extends SquareI {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.height; j++) {
        row = row + c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
