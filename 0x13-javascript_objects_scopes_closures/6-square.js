#!/usr/bin/node

const baseSquare = require('./5-square');

class Square extends baseSquare {
// constructor (size) {
// super(size, size);
// }
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'C';
        }
        console.log(row);
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
