#!/usr/bin/node

const Argument = process.argv[2];

if (isNaN(Argument) || Argument === undefined) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(Argument));
}
