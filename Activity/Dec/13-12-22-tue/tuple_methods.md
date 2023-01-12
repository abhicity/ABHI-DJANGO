[TOC]
## Tuple Methods

### 1. count
- The `count()` method returns the number of times a specified value appears in the tuple.
- Syntax : `tuple.count(value)`
- Parameter Values
  - ___value___	(Required). 
    - The item to search for
```
help(abhi.count)
Help on built-in function count:

count(value, /) method of builtins.tuple instance
    Return number of occurrences of value.
```
Example :
```py
>>> abhi = (1, 2, 3, 4, 5, 6, 7, 8, 2)
>>> abhi
(1, 2, 3, 4, 5, 6, 7, 8, 2)
>>> shek = abhi.count(2)
>>> shek
2
>>> type(abhi)
<class 'tuple'>
>>> type(shek)
<class 'int'>
>>>
```
---

### 2. index
- The `index()` method finds the first occurrence of the specified value.
- It raises an exception if the value is not found.
- Syntax : `tuple.index(value)`
- Parameter Values : 
  - ___value___	(Required). 
    - The item to search for
```
help(x.index)
Help on built-in function index:

index(value, start=0, stop=9223372036854775807, /) method of builtins.tuple instance
    Return first index of value.

    Raises ValueError if the value is not present.
```
Example :
```py
>>> x = (1, 2, 3, 4, 5, 6, 7, 8)
>>> x
(1, 2, 3, 4, 5, 6, 7, 8)
>>> x.index(1)
0
>>> x.index(2)
1
>>> x.index(3)
2
>>> x.index(4)
3
>>> x.index(5)
4
>>> x.index(6)
5
>>> x.index(7)
6
>>> x.index(8)
7
#>>> x.index()
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: index expected at least 1 argument, got 0
#>>> x.index(9)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ValueError: tuple.index(x): x not in tuple
>>>
```
---