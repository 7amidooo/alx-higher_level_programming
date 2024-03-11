#!/usr/bin/node

const ele = process.argv;

if (isNaN(parseInt(ele[2]))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(ele[2])}`);
}
