#!/usr/bin/node

const Sqa = Number(process.argv[2]);

if (Number(process.argv[2])) {

  for (let i = 0; i < Sqa; i++) {
    console.log('X'.repeat(Sqa));
  }
} else {
  console.log('Missing size');
}
