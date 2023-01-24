#!/usr/bin/node
if (process.argv.length < 3) process.exit();
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) { console.log(error)} else {
    let count = 0;
    const parsedBody = JSON.parse(body);
    for (const data of parsedBody.results) {
      data.characters.forEach(character => {
        if (Number(character.split('/')[5]) == 18){
          count++;
        }
      }
      );
    }
    console.log(count);
  }
});
