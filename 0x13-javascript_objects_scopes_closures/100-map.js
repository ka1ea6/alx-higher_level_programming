#!/usr/bin/node

const data = require('./100-data').list;

const newArr = data.map((el, idx) => el * idx);
console.log(data);
console.log(newArr);
