#!/usr/bin/node

const originalList = require('./100-data').list;

console.log(originalList);

const newList = originalList.map (function (y, index) {
    return (y * index);
});
console.log(newList);
