#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const process = require('process');
const url = process.argv[2];

request(url, function (error, respones, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', function (error, data) {
      if (error) {
        console.log(error);
      }
    });
  }
});
