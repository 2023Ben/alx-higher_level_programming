#!/usr/bin/node

const { argv } = require('process');
const parsedInt = parseInt(argv[2], 10);

if (isNaN(parsedInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parsedInt}`);
}
