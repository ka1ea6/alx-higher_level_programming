#!/usr/bin/node

const fs = require("fs");

const [_, __, fileName, payload] = process.argv;

const writeToFile = function (filePath, val) {
  try {
    fs.writeFileSync(filePath, val, { encoding: "utf-8" });
  } catch (err) {
    console.log(err);
  }
};

writeToFile(fileName, payload);
