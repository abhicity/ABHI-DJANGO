const number = parseInt(prompt('Enter an integer: '));
const range = parseInt(prompt('Enter a range: '));
for (let i = 1; i <= range; i++) {
    const result = i * number;
    console.log(`${number} * ${i} = ${result}`);
}