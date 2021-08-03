#!/usr/bin/node
const args = process.argv.map(Number).slice(2, process.argv.length).sort((a, b) => b - a);
console.log(args.length > 1 ? args[1] : 0);
