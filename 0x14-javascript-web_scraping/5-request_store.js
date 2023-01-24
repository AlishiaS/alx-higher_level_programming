#!/usr/bin/node
if (process.argv.length < 4) process.exit();
const fs = require('fs');
const request = require('request');

request(process.argv[2], function (error, response, body){
    if (error) { console, log(error); } else {
	fs.writeFile(process.argv[3], body, { encoding: 'utf8' }, (error) => {
	    if (error) { console.error(error); }
	});
	}
});
