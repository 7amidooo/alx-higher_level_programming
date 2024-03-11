#!/usr/bin/node

const ele = process.argv;

if (isNaN(parseInt(ele[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(ele[2]); i++) {
    console.log('C is fun');
  }
}
