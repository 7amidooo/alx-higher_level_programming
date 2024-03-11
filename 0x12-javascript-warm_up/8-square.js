#!/usr/bin/node

const ele = process.argv;

if (isNaN(parseInt(ele[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(ele[2]); i++) {
    for (let j = 0; j < parseInt(ele[2]); j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
