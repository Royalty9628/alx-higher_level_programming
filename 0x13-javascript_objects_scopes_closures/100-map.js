#!/usr/bin/node

const originalList = require('./100-data').list;

console.log(originalList);

const mappList = originalList.map (function (y, index) {
    return (y * index);
});
console.log(mappList);
