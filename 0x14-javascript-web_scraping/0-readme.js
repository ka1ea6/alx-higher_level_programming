#!/usr/bin/node
const fs = require("fs");

const fileName = process.argv[2];

const readContent = function (filePath) {
  try {
    return fs.readFileSync(filePath, { encoding: "utf-8" });
  } catch (err) {
    return err;
    // return {
    //   Error: err.ENOENT,
    //   errno: err.errno,
    //   code: err.code,
    //   syscall: err.syscall,
    //   path: err.path,
    // };
  }
};

const fileContent = readContent(fileName);
console.log(fileContent);
