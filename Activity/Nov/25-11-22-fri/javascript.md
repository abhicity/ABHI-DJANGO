## Loops



- Loops are used in JavaScript to perform repeated tasks based on a condition.
- Conditions typically return `true` or `false`.
A loop will continue running until the defined condition returns `false`.

```js
//Syntax
for (initialization; condition; finalExpression) {
  // code
}
```

The for loop consists of three optional expressions, followed by a code block :

- `initialization` 
  - This expression runs before the execution of the first loop, and is usually used to create a counter.
- `condition` 
  - This expression is checked each time before the loop runs. 
  - If it evaluates to `true`, the `statement` or code in the loop is executed. If it evaluates to `false`, the loop stops. 
  - And if this expression is omitted, it automatically evaluates to `true`.
- `finalExpression` 
  - This expression is executed after each iteration of the loop. 
  - This is usually used to increment a counter, but can be used to decrement a counter instead.

```js
const array = [1, 2, 3];

for (const i in array) {
  console.log(i);
}

// 0
// 1
// 2
```

```js
const arr = [ "Abhi", "Chandhu", "Rahul" ];

for (let i of arr) {
  console.log(i);
}

// Output:
// Abhi
// Chandhan
// Rahul
```

```js
//Loop Example
//Iterate through integers from 0-8:

for (let i = 0; i < 9; i++) {
  console.log(i);
}

// Output:
// 0
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
```

```js
const capitals = {
  a: "Athens",
  b: "Belgrade",
  c: "Cairo"
};

for (let key in capitals) {
  console.log(key + ": " + capitals[key]);
}

// Output:
// a: Athens
// b: Belgrade
// c: Cairo
```

```js
//Loop Example
//Using Loop, the statement needs to be written only once and the loop will be executed 10 times as shown below :
for(i=1; i<=10; i++)
{
    console.log(i, "Django");
}
```