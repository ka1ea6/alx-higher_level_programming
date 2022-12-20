#!/usr/bin/node
const xTimes = Math.floor(parseInt(process.argv[2]));
if (isNaN(xTimes)) console.log('Missing number of occurrences');
else {
  for (let i = 0; i < xTimes; i++) {
    console.log('C is fun');
  }
}
