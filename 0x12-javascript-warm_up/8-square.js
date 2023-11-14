#!/usr/bin/node

const check = process.argv[2];

if (isNaN(check) || check === undefined) {
  console.log('Missing size');
} else {
  const x = Number(process.argv[2]);
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
