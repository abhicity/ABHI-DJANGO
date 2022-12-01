[TOC]
# Javascript

## Data Types

### Number
- It is an integer data or floating point number

```js
//Number Example
5, 10.5, 15e-2 etc
```


### String
- String is used to store text.
- It represents the textuak data.
- It uses `'` or `"` to store the text data.
  - Eg :  
  - Single quotes : ('') 'Hello'
  - Double quotes : ("") Hello"
  - Backticks : (``) `Hello`

```js
//Strings Example
var name = 'Hello';
var name = "Hello";
```

### Null
- It denotes the null value.
- null is a special value that represents empty or unknown value.
- null is not the same as NULL or Null.
- The null number variable will be empty.
 
```js
//Null Example 
var number = null;
```

### Boolean
- This data type represents logical entities. 
- In boolean there are two values `true` or `false` in lower case.
- It is easier to think of it as a yes/no switch.

```js
//Boolean Example
var data_checked = true;
var value_counted = false;
console.log(value_counted) //false
```

### Undefined
- It has only one value undefined. 
- When a variable is declared but not initialized, it is assigned the value of undefined.

```js
//Undefined Example
var name;
console.log(name); // undefined
```

### Array
- Array is a collection of data.
- The array is a single variable that is used to store different elements.
- Data is defined inside `[ ]`
- Data's are seperated with `,`

```js
//Array Example
var fruits=["Apple","Mango","Orange"]
console.log(fruits)
(3) ['Apple', 'Mango', 'Orange']

0: "Apple"
1: "Mango"
2: "Orange"
length: 3

```
### Console.log()
- It outputs a message to the web console. 
- It is used to print any kind of variables.

```js
//Console Example
var a = 2;
console.log(a); //2
```


.
.
.