#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((total, element) => searchElement === element ? ++total : total, 0);
};
