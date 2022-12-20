#!/usr/bin/node
exports.add = function (num1, num2) {
  if (
    (!num1 && typeof num1 !== 'number') ||
    (!num2 && typeof num2 !== 'number')
  ) {
    return 0;
  } else return num1 + num2;
};
