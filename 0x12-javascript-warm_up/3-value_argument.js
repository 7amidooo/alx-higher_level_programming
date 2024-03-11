#!/usr/bin/node

const ele = process.argv;

if (ele[2] === undefined) {
  console.log('No argument');
} else {
  console.log(ele[2]);
}
