#!/usr/bin/node

const fs = require("fs");
const request = require("request");

const [_, __, url, filePath] = process.argv;

request.get(url, (err, res, body) => {
  fs.writeFileSync(filePath, body, { encoding: "utf-8" });
});
