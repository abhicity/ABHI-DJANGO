[TOC]
## List Methods

### 1. append
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
---

### 2. clear
- The `clear()` method removes all the elements from a list.
- Syntax : `list.clear()`
```
help(fruits.clear)
Help on built-in function clear:

clear() method of builtins.list instance
    Remove all items from list.
```
Example :
```py
>>> fruits = ["apple", "orange", "mango"]
>>> fruits.clear()
>>> fruits
[]
```
---

### 3. copy
- The `copy()` method returns a copy of the specified list.
- Syntax : `list.copy()`
```
help(fruits.copy)
Help on built-in function copy:

copy() method of builtins.list instance
    Return a shallow copy of the list.
```
Example : 
```py
>>> fruits = ["apple", "orange", "mango"]
>>>
>>> fruits
['apple', 'orange', 'mango']
>>>
>>> fruits.copy()
['apple', 'orange', 'mango']
>>>
>>> c = fruits.copy()
>>>
>>> fruits
['apple', 'orange', 'mango']
>>>
>>> c
['apple', 'orange', 'mango']
>>>
```
---

### 4. count
- The `count()` method returns the number of elements with the specified value.
- Syntax : `list.count(value)`
- Parameter : ___value___	(Required).
    - Any type (string, number, list, tuple, etc.). The value to search for.
```
help(fruits.count)
Help on built-in function count:

count(value, /) method of builtins.list instance
    Return number of occurrences of value.
```
Example 1 : 
```py
>>> fruits = ["apple", "orange", "mango"]
>>> fruits.count("apple")
1
>>>
>>> fruits = ["apple", "orange", "mango", "apple"]
>>> fruits.count("apple")
2
>>>
```
Example 2 :
```
>>> num = [1, 4, 2, 8, 7, 8, 9, 3, 1]
>>> num.count(8)
2
>>>
```
---

### 5. extend
- The `extend()` method adds the specified list elements (or any iterable) to the end of the current list.
- Syntax : `list.extend(iterable)`
- Parameter : ___iterable___ (Required). 
  - Any iterable (list, set, tuple, etc.)
```
help(fruits.extend)
Help on built-in function extend:

extend(iterable, /) method of builtins.list instance
    Extend list by appending elements from the iterable.
```
Example 1 : 
```py
>>> fruits = ["apple", "orange", "mango"]
>>> cars = ["BENZ", "Audi", "BMW"]
>>> fruits.extend(cars)
>>> fruits
['apple', 'orange', 'mango', 'BENZ', 'Audi', 'BMW']
```
Example 2 :
```py
>>> fruits = ["apple", "orange", "mango"]
>>> num = [1, 2, 3, 4, 5]
>>> fruits.extend(num)
>>> fruits
['apple', 'orange', 'mango', 1, 2, 3, 4, 5]
>>>
```
---

### 6. index
- The `index()` method returns the position at the first occurrence of the specified value.
- Syntax : `list.index(elmnt)`
- Parameter : ___elmnt___	(Required.)
    - Any type (string, number, list, etc.). The element to search for
```
help(fruits.index)
Help on built-in function index:

index(value, start=0, stop=9223372036854775807, /) method of builtins.list instance    Return first index of value.

    Raises ValueError if the value is not present.
```

Example 1 :
```py
>>> fruits = ["apple", "orange", "mango"]
>>> fruits.index("apple")
0
>>> fruits.index("orange")
1
>>> fruits.index("mango")
2
>>>
```
Example 2 :
```py
>>> num = [1, 4, 2, 8, 7, 9, 3]
>>> num.index(8)
3
>>>
```
---

### 7. insert
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
### 8. pop
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
---

### 9. remove
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

### 10. reverse
- The `reverse()` method reverses the sorting order of the elements.
- Syntax : `list.reverse()`
```
help(fruits.reverse)
Help on built-in function reverse:

reverse() method of builtins.list instance
    Reverse *IN PLACE*.
```
Example 1 :
```py
>>> fruits = ["apple", "orange", "mango", "watermelon"]
>>> fruits.reverse()
>>> fruits
['watermelon', 'mango', 'orange', 'apple']
>>>
```
---

### 11. sort
- The sort() method sorts the list ascending by default.
- You can also make a function to decide the sorting criteria(s).
- Syntax : `list.sort(reverse=True|False, key=myFunc)`
Parameter : 
- ___reverse___ (Optional). 
  - reverse=True will sort the list descending. 
  - Default is reverse=False
- ___key___	(Optional). 
  - A function to specify the sorting criteria(s)
```
help(fruits.sort)
Help on built-in function sort:

sort(*, key=None, reverse=False) method of builtins.list instance
    Sort the list in ascending order and return None.

    The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
    order of two equal elements is maintained).

    If a key function is given, apply it once to each list item and sort them,
    ascending or descending, according to their function values.

    The reverse flag can be set to sort in descending order.
```
Example : 
```py
#Sort the list alphabetically
>>> fruits = ["apple", "orange", "mango", "watermelon"]
>>> fruits.sort()
>>> fruits
['apple', 'mango', 'orange', 'watermelon']
>>>
```
---