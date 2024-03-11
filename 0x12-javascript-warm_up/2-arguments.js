#!/usr/bin/node

const ele = process.argv;
if (ele.length <= 2) {
  console.log('No argument');
} else if (ele.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
