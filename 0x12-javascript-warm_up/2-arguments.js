#!/usr/bin/node

const args = process.argv;
const numArgs = args.length;

if (numArgs <= 2) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
