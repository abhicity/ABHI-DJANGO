[TOC]

## Different Types of Errors in Python.


### 1. TypeError
```py
#int + string = unsupported operand
>>> a = 8
>>> b = "abhi"
>>> c = a + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
```py
#String * String =  can't multiply
>>> inst = "Skill disk"
>>> place = "Bengaluru"
>>> form = inst * place
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
```
---

### 2. ZeroDivisionError
```py
>>> a = 5
>>> b = 0
>>> c = a / b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
```
---

### 3. SyntaxError
```py
>>> name = "Abhishek"
>>> print "name"
  File "<stdin>", line 1
    print "name"
    ^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>>
```
---

### 4. IndexError
```py
>>> list = [1,2,3]
>>> list
[1, 2, 3]
>>> list[0]
1
>>> list[1]
2
>>> list[2]
3
>>> list[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
```
---

### 5. TypeError
```py
>>> a = "pepsi" + 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>>
```
---

### 6. ValueError
```py
>>> int("Skill Disk")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'Skill Disk'
>>>
```
---

### 7. NameError
```py
>>> Abhishek
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Abhishek' is not defined
>>>
```
---

### 8. KeyboardInterrupt
```py
#when we press ctrl+c
>>> name = input("Enter your Name")
Enter your NameTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyboardInterrupt
>>>
```
---

### 9. ModuleNotFoundError
```py
>>> import skill
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'skill'
>>>
```
---

### 10. ImportError
```py
>>> from math import circle
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'circle' from 'math' (unknown location)
>>>
```
---

### 11. IndentationError
```py
>>> def addition(a, b):
... result = a + b
  File "<stdin>", line 2
    result = a + b
    ^
IndentationError: expected an indented block after function definition on line 1
>>>
```
---



