#!/usr/bin/node

function swapArrElements (list, idx1, idx2) {
  const temp = list[idx1];
  list[idx1] = list[idx2];
  list[idx2] = temp;
}

exports.esrever = function (list) {
  const revArr = [...list];

  for (let i = 0; i < list.length / 2; i++) {
    swapArrElements(revArr, i, (list.length - 1) - i);
  }

  return revArr;
};
