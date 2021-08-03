#!/usr/bin/node
function factorial (n) {
  return isNaN(n) || n === 0 ? 1 : n * factorial(n - 1);
}

console.log(factorial(parseInt(process.argv[2])));
