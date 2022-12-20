#!/usr/bin/node

const data = require('./101-data').dict;

const newDict = {};
for (const i in data) {
  const currOccurance = data[i];
  if (!newDict[currOccurance]) {
    newDict[currOccurance] = [i];
  } else {
    newDict[currOccurance].push(i);
  }
}

console.log(newDict);
