#!/usr/bin/node
const request = require('request');
let count = 0;
const url = process.argv[2];

request(url, function (error, respones, body) {
  if (error) {
    console.log(error);
  } else {
    const info = JSON.parse(body);
    const infres = info.results;
    for (let i = 0; i < infores.length; i++) {
      if (infres[i].characters) {
        for (const j of infres[i].characters) {
          if (j.includes('18')) {
            count++;
          }
        }
      }
    }
    console.log(count);
  }
});
