#!/usr/bin/node

const args = process.argv;
const numArgs = args.length;

if (numArgs <= 2) {
  console.log('No argument');
} else if (numArgs > 2) {
  console.log('Argument found');
}
