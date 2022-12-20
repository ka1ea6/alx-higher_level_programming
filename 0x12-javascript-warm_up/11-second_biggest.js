#!/usr/bin/node
const argLen = process.argv.length;
if (argLen <= 3) console.log(0);
else {
  const numArr = process.argv
    .splice(2, argLen - 2)
    .map((el) => parseInt(el))
    .filter((el, idx, arr) => el !== Math.max(...arr));

  console.log(Math.max(...numArr));
}
