#!/usr/bin/node
const num1 = Math.floor(parseInt(process.argv[2]))
const num2 = Math.floor(parseInt(process.argv[3]))
function add(a, b){
    if (isNaN(a) || isNaN(b) || !a || !b){
        return NaN;
    }
    return a + b;
}
const sumRes = add(num1, num2);
console.log(sumRes)
