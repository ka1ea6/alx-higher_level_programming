#!/usr/bin/node

// const fs = require("fs/promises");
const fs = require('fs');

const [input1, input2, output] = process.argv.slice(2, 5);

if (!input1 || !input2 || !output) {
  console.log('Usage: ./102-concat.js <input file 1> <input file 2> <output file>');
}

// (async () => {
//     try{
//         const f1 = await fs.readFile(input1 ,{encoding: 'utf-8'});
//         const f2 = await fs.readFile(input2, {encoding: "utf-8"});

//         await fs.writeFile(output, `${f1}\n${f2}`, {encoding: 'utf-8'})

//     } catch(err) {
//         console.error(`Err ${err}`)
//     }

// })()

fs.readFile(input1, { encoding: 'utf-8' }, (err, input1Data) => {
  if (!err) {
    fs.readFile(input2, { encoding: 'utf-8' }, (err, input2Data) => {
      if (!err) {
        fs.writeFile(output, `${input1Data}${input2Data}`, { encoding: 'utf-8' }, (err) => {
          if (err) console.error('Error: ', err);
        });
      } else console.error('Error: ', err);
    });
  } else console.error('Error: ', err);
});
