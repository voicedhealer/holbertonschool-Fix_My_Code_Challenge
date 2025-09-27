#!/usr/bin/node

const size = parseInt(process.argv[2], 10);

if (isNaN(size) || size < 0) {
    process.exit(0);
}

const line = '#'.repeat(size);

for (let i = 0; i < size; i++) {
    console.log(line);
}
