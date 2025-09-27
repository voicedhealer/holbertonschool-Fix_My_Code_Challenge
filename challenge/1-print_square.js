#!/usr/bin/node

if (process.argv.length !== 3) {
    console.log('Usage: ./1-print_square.js <size>');
    process.exit(1);
}

const size = parseInt(process.argv[2]);
if (isNaN(size) || size < 1) {
    console.log('Please provide a positive integer');
    process.exit(1);
}

// Construire une ligne du carré
const line = '#'.repeat(size);
// Afficher la ligne n fois
for (let i = 0; i < size; i++) {
    console.log(line);
}
