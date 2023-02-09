#!/usr/bin/node

const fs = require('fs');

const fileName = process.argv[2];
const payload = process.argv[3];

const writeToFile = function (filePath, val) {
  try {
    fs.writeFileSync(filePath, val, { encoding: 'utf-8' });
  } catch (err) {
    console.log(err);
  }
};

writeToFile(fileName, payload);
