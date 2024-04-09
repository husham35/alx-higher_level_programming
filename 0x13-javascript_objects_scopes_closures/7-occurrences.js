#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let elementCount = 0;
  list.forEach(element => {
    if (element === searchElement) {
      elementCount += 1;
    }
  });

  return elementCount;
};
