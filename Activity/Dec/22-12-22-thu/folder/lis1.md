[TOC]
## List

1. Differentiate between the following :
    a. pop() and remove() methods of list.
    b. Del statement and pop() method of list.
    c. append() and insert() methods of list.


## a.)
### pop()
- The `pop()` method removes the element at the specified position.
- Syntax : `list.pop(pos)`
- Parameter : ___pos___	(Optional). 
  - A number specifying the position of the element you want to remove, default value is -1, which returns the last item
```
help(fruits.pop)
Help on built-in function pop:

pop(index=-1, /) method of builtins.list instance
    Remove and return item at index (default last).

    Raises IndexError if list is empty or index is out of range.
```
Example 1 :
```py
#if we doesnt give any position it pop's the last value from the list
>>> fruits = ["apple", "orange", "mango"]
>>> fruits.pop()
'mango'
>>> fruits
['apple', 'orange']
>>> fruits.pop()
'orange'
>>> fruits
['apple']
>>>
```
Example 2 : 
```py
>>> fruits = ["apple", "orange", "mango", "watermelon"]
>>> fruits.pop(1)
'orange'
>>> fruits
['apple', 'mango', 'watermelon']
>>>
>>> fruits.pop(2)
'watermelon'
>>> fruits
['apple', 'mango']
>>>
```


### remove()
- The `remove()` method removes the first occurrence of the element with the specified value.
- Syntax : `list.remove(elmnt)`
- Parameter : ___elmnt___	(Required). 
    - Any type (string, number, list etc.) The element you want to remove
```
help(fruits.remove)
Help on built-in function remove:

remove(value, /) method of builtins.list instance
    Remove first occurrence of value.

    Raises ValueError if the value is not present.
```
Example : 
```py
>>> fruits = ["apple", "orange", "mango", "watermelon"]
>>> fruits.remove("mango")
>>>
>>> fruits
['apple', 'orange', 'watermelon']
>>>
>>> fruits.remove("apple")
>>>
>>> fruits
['orange', 'watermelon']
>>>
```
---
---


## c.)
### append()
- The `append()` method appends an element to the end of the list.
- Syntax : `list.append(elmnt)`
- Parameter : ___elmnt___ (Required). 
    - An element of any type (string, number, object etc.)

```
help(fruits.append)
Help on built-in function append:

append(object, /) method of builtins.list instance
    Append object to the end of the list.
```
Example 1 : 
```py
>>> fruits = ["apple", "orange", "mango"]
>>> fruits
['apple', 'orange', 'mango']
>>> fruits.append("banana")
>>> fruits
['apple', 'orange', 'mango', 'banana']
>>>
>>> fruits.append("50")
>>> fruits
['apple', 'orange', 'mango', 'banana', '50']
>>>
```
Example 2 :
```
>>> fruits = ["apple", "orange", "mango"]
>>> cars = ["BENZ", "Audi", "BMW"]
>>> fruits.append(cars)
>>> fruits
['apple', 'orange', 'mango', ['BENZ', 'Audi', 'BMW']]
>>>
```


### insert()
- The `insert()` method inserts the specified value at the specified position.
- Syntax : `list.insert(pos, elmnt)`
- Parameter : 
- ___pos___	(Required).
  -  A number specifying in which position to insert the value
- ___elmnt___ (Required). 
  - An element of any type (string, number, object etc.)
```
help(fruits.insert)
Help on built-in function insert:

insert(index, object, /) method of builtins.list instance
    Insert object before index.
```
Example :
```py
>>> fruits = ["apple", "orange", "mango"]
>>> fruits.insert(1, "promegranate")
>>> fruits
['apple', 'promegranate', 'orange', 'mango']
>>>
>>>
>>> fruits.insert(0, "avacado")
>>> fruits
['avacado', 'apple', 'promegranate', 'orange', 'mango']
>>>
```
---
---