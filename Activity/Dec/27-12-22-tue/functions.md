[TOC]

## Different ways of calling a function.

### 1. without any parameter and return value
Example : 1
```py
>>> def inst():
...     print('Skill_Disk')
...
>>> inst()
Skill_Disk
```
Example : 2
```py
>>> def add():
...     a = 4 + 3
...     print('add = ', a)
...
>>> add()
add =  7
```
---

### 2. with positional argument and no return value
Example : 1
```py
>>> def add(a, b):
...     sum = a + b
...     print('sum = ', sum)
...
>>> add(3, 8)
sum =  11
```
Example : 2
```py
>>> def cer(name):
...     print(f'My name is {name}.')
...
>>> cer('Abhishek')
My name is Abhishek.
```
---

### 3. with positional argument and return value
Example : 1
```py
>>> def increment(value):
...     return value + 1.0
...
>>> increment(9)
10.0
```
Example : 2
```py
>>> def certificate(name, prize, comp_name):
...     return f'This certificate is proudly given to {name} who has won {prize} prize in {comp_name}.'
...
>>> certificate('Ram', '2nd', 'javlin_throw')
'This certificate is proudly given to Ram who has won 2nd prize in javlin_throw.'
```
---

### 4. without positional argument and with a return value
Example : 1
```py
>>> def sub():
...     sub = 10 - 2
...     return sub
...
>>> sub()
8
```
Example : 2
```py
>>> def div():
...     div = 98 / 2
...     return div
...
>>> div()
49.0
```
---

### 5. with position argument + n number of arguments(*args)
Example : 1
```py
>>> def cert(name, *args):
...     print(f'My name is {name}.')
...
>>> cert('Raju', 2, 'seven', 'bengaluru')
My name is Raju.
```
Example : 2
```py
>>> def multiply(a, b, *args):
...     multiply = a * b
...     return multiply
...
>>> multiply(3, 9, 1, 4, 5, 7, 0)
27
```
---

### 6. with position argument + keyword argument.
Example : 1
```py
>>> def add(a=4, b=9):
...     add = a + b
...     return add
...
>>> add()
13
```
Example : 2
```py
>>> def sub(a=None, b=5, *args):
...     sub = a - b
...     return sub
...
>>> sub(9)
4
```
---

### 7. with position argument + n number of arguments(*args) + keyword argument.
Example:1
```py
>>> def address(city='Benagluru', *args, pincode=None):
...     print(f'{city}-{pincode}')
...
>>> address()
Benagluru-None
>>>
>>> address('Mysore',660012)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: address() takes from 0 to 1 positional arguments but 2 were given
>>>
>>> address('Mysore',pincode=660012)
Mysore-660012
```
Example:2
```py
>>> def sum(a, *args, b):
...     add = a + b
...     return add
...
>>> sum(2, 6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sum() missing 1 required keyword-only argument: 'b'
>>> sum(2, b=6)
8
```
---

### 8. only keyword argument. (def func_name(*, keywords))
Example : 1
```py
>>> def add(*args, a, b):
...     sum = a + b
...     return sum
...
>>> add()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add() missing 2 required keyword-only arguments: 'a' and 'b'
>>>
>>> add(5, 7)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add() missing 2 required keyword-only arguments: 'a' and 'b'
>>>
>>> add(a=5, b=9)
14
```
Example : 2
```py
>>> def div(*, x, y):
...     division = x / y
...     return division
...
>>> div(10, 20)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: div() takes 0 positional arguments but 2 were given
>>>
>>> div(x=10, y=2)
5.0
```
---

### 9. n number of keyword argument. (def func_name(*, **kwargs))
Example : 1
```py
>>> def city(*args, **kwargs):
...     print(f'Bengaluru - 560001')
...
>>> city('mysore', name='ram', pincode=560007, a=5)
Bengaluru - 560001
```
Example : 2
```py
>>> def sub(*args, **kwargs):
...     sub = 125 - 23
...     return sub
...
>>> sub(9, 0, a=2, b=8, x=10, y=100)
102
```
---

### 10. keyword argument + n number of keyword argument. (def func_name(*,name, age, **kwargs))
Example : 1
```py
>>> def add(*args, a, b, c, **kwargs):
...     add = a + b + c
...     return add
...
>>> add(21, 78, 12, a=10, b=20, c=30, x=70)
60
>>>
>>> add(21, 40, 91)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add() missing 3 required keyword-only arguments: 'a', 'b', and 'c'
```
Example : 2
```py
>>> def address(*args, city=None, pincode=None, **kwargs):
...     print(f'{city} - {pincode}')
...
>>> address('mysore', 'bengaluru', city='kolar', pincode=890012, pincode=902190)
  File "<stdin>", line 1
SyntaxError: keyword argument repeated: pincode
>>>
>>> address('mysore', 'bengaluru', city='kolar', pincode=890018, z=123456)
kolar - 890018
```
---

### 11.  argument + n number of argument + keyword argument + n number of keyword argument. (def func_name(a, b, c,*arg,name, age, **kwargs))
Example : 1
```py
>>> def function(a, b, c, *args, name, inst=None, **kwargs):
...     add = a + b + c
...     print(f'{name} - {inst}')
...     print(add)
...
>>> function(2, 20, 2000, 10000, name='Rahul', inst='Skill_disk', pincode=235210)
Rahul - Skill_disk
2022
```
Example : 2
```py
>>> def func(x, y, z, *args, a, b, c=None, **kwargs):
...     add = x + y + z
...     sub = a - b - c
...     print(add)
...     return sub
...
>>> func(20, 40, 60, 80, 100, a=100, b=50, c=20, k=90, j=20)
120
30
>>> func(20, 40, 80, 100, a=100, b=50, k=90, j=80)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in func
TypeError: unsupported operand type(s) for -: 'int' and 'NoneType'
```
---


