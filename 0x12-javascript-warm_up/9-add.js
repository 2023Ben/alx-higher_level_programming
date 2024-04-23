#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const { argv } = require('process');
const firstArg = parseInt(argv[2], 10);
const secondArg = parseInt(argv[3], 10);

if (isNaN(firstArg) || isNaN(secondArg)) {
  console.log('NaN');
} else {
  console.log(add(firstArg, secondArg));
}
