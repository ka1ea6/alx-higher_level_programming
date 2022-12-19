#!/usr/bin/node
const argNum = process.argv.length;
console.log(
  argNum === 2
    ? 'No argument'
    : argNum === 3
    ? 'Argument found'
    : 'Arguments found'
);
