#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  for (let elIdx = list.length - 1; elIdx >= 0; elIdx--) {
    reversedList.push(list[elIdx]);
  }

  return reversedList;
};
