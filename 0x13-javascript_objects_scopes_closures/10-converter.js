#!/usr/bin/node

exports.converter = function (base) {
  return function (y) {
    return num.toString(base);
  };
};
