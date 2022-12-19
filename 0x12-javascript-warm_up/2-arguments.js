#!/usr/bin/node
const argNum = process.argv.length - 2;
console.log(
  argNum <= 0
    ? 'No argument'
    : argNum === 1
    ? 'Argument found'
    : 'Arguments found'
);
