[TOC]

# Javascript

1. Variables.
2. Comments.
3. Control Flow statements.

### ___Variables___

- 3 Ways to Declare a JavaScript Variable :
  - Using var
  - Using let
  - Using const
- Identifiers are case-sensitive.
- Variables are containers for storing data (storing data values).


- All JavaScript variables must be identified with unique names.
- These unique names are called identifiers.
- Identifiers can be short names (like x and y) or more descriptive names (age, sum, totalVolume).
- The general rules for constructing names for variables (unique identifiers) are :

  - Names can contain letters, digits, underscores, and dollar signs.
  - Names must begin with a letter.
  - Names can also begin with `$` and `_`
  - Names are case sensitive (y and Y are different variables).
  - Reserved words (like JavaScript keywords) cannot be used as names.

```js
//var Example
//In this example a, b and c are variables declared with the var keyword :

var a = 5;
var b = 10;
var c = a+b;
console.log(c)
//15
```
```js
//let Example
//In this example x, y and z are variables declared with the let keyword :

let x = 8;
let y = 4;
let z = x + y;
console.log(z)
//12
```
```js
//const Example
const price1 = 15;
const price2 = 10;
let total = price1 + price2;
console.log(total)
//25
```
- The two variables `price1` and `price2` are declared with the `const` keyword.
- These are constant values and cannot be changed.
- The variable `total` is declared with the `let` keyword.
- This is a value that can be changed.
 
---

### ___Comments___

- JavaScript comments can be used to explain JavaScript code, and to make it more readable.
- JavaScript comments can also be used to prevent execution, when testing alternative code.
- There are 2 types of commands in javascript they are,
  - Single line commend.
  - Multi line commend.

- Single line commend.
  - Single line comments start with //.
  - Any text between // and the end of the line will be ignored by JavaScript (will not be executed).
- Multi line commend.
  - Multi-line comments start with /* and end with */.
  - Any text between /* and */ will be ignored by JavaScript.

```js
//comments Example

<script>  
//Single line comment  
JavaScript Code
</script>


<script>  
/* Multi-line comment  
This line will not execute */
JavaScript Code
</script>
```
---

### ___Control Flow statements___
- Very often when you write code, you want to perform different actions for different decisions.
  - Use `if` to specify a block of code to be executed, if a specified condition is true.
  - Use `else` to specify a block of code to be executed, if the same condition is false.
  - Use `else if` to specify a new condition to test, if the first condition is false.
- Uppercase letters (If or IF) will generate a JavaScript error. 

```js
//if, else Example
const age = 18;

if (age >= 18) {
  console.log("Harsha is an adult.");
} else {
  console.log("Harsha is a child.");
}
//Harsha is an adult.
```
```js
//if, else if, else Example
const age = 18;

if (age < 18) {
  console.log("Harsha is under 18 years old.");
} else if (age >= 18 == age <= 21) {
  console.log("Harsha is between the ages of 18 and 21.");
} else {
  console.log("Harsha is over 21 years old.");
}
//Harsha is between the ages of 18 and 21.
```
---