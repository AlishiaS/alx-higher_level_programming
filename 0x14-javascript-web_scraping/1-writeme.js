#!/usr/bin/node
const fs = require('fs');
if (process.argv.length < 4) { process.exit(); }
fs.writeFile(process.argv[2], process.argv[3], { encoding: 'utf' }, (error) => {
  if (error) { console.log(error);}
});
