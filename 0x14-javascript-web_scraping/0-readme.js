#!/usr/bin/node
const fs = require('fs');

const fileName = process.argv[2];

const readContent = function (filePath) {
  try {
    return fs.readFileSync(filePath, { encoding: 'utf-8' });
  } catch (err) {
    return err;
  }
};

const fileContent = readContent(fileName);
console.log(fileContent);
