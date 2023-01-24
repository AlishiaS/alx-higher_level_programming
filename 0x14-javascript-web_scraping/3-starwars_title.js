#!/usr/bin/node
if (process.argv, length < 3) process.exit();
const request = require('request');

request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (error, response, body)
{
  if (error) { console.log(error);} else {
    const parsedBody = JSON.parse(body);
    console.log(parsedBody.title);
  }
  
});
