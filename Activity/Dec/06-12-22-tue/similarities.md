### 1. Variables
```js
//JavaScript
var fName = 'Abhi';
let mName = 'Shek';
const lName = 'C';
```
```Py
#Python
fName = 'Abhi'
mName = 'Shek'
lName = 'C'
```

### 2. String
```js
//JavaScript
JavaScript
let name = "Abhi Shek C";
console.log(`My name is ${name}.`);
```
```Py
#Python
name = "Abhi Shek C"
print(f'My name is {name}.');
```

### 3. If-Statements
- If
```js
//JavaScript
if (1 == 1) {
   return true;
}
```
```py
#Python
if (1 == 1):
   return true
```
- Else
```js
//JavaScript
if (1 == 1)
    return true
else 
    return false
```
```py
#Python
if (1 ==1): 
   return true
else:
   return false
```
- Else-If
```js
//JavaScript
if (1 == 1)
    return true
else if (1 == 2)
    return false
else 
    return false
```
```py
#Python
if (1 ==1):
   return true
elif (1 == 2):
   return false
else:
   return false
```

### 4. For Loop
- Both languages have various ways of doing loops.
-  But the syntax between JavaScript and Python is very different.
```Js
//JavaScript
for (let i = 0; i <= 5; i++) {
  console.log(i)
}
```
```Py
#Python
for i in range(6):
  print(i)
```
In both instances, both languages print out the numbers 0–5. Python’s `in range()` syntax is comparable to JavaScript’s `<=` , as it only loops for everything less than the given argument. In our case, the argument is 6, so it loops through 0 to 5.

If we wanted to use an array, we could do something like this:
```js
//JavaScript
let fruits = ['apples', 'mangos', 'watermellon'];
for (let i = 0; i < fruits.length; i++) {
  console.log(fruit[i])
}
#apples mangos watermellon
```
```py
#Python
fruits = ['apples', 'mangos', 'watermellon']
for i in range(len(fruit)):
  print(fruit[i])
#apples mangos watermellon
```


### 5. While Loops
- While loops are similar to for loops in many ways.
- The syntax between the two is pretty similar:
```js
//JavaScript
let i = 1;
while (i < 10) {
  console.log(i)
  i++;
}
```
```py
#Python
i = 1
while i < 10:
  print(i)
  i += 1
  ```
- A few things you’ll notice here is that JavaScript increments with `i++` while Python does it with `i += 1 .` 
- This has nothing to do with while-loops; Python just does not have the `++` operator.
