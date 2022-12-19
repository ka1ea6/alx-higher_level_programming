#!/usr/bin/node
const xTimes = Math.floor(parseInt(process.argv[2]));
if (isNaN(xTimes)) console.log('Missing size');
else {
  for (let i = 0; i < xTimes; i++) {
    console.log('X'.repeat(xTimes));
  }
}
