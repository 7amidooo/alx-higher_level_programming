#!/usr/bin/node

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

const ele = process.argv;

if (ele[2] === undefined || ele[3] === undefined) {
  console.log(NaN);
} else {
  add(ele[2], ele[3]);
}
