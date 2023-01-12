[TOC]
## Dict Methods

### 1. clear
- The `clear()` method removes all the elements from a dictionary.
- Syntax : `dict.clear()`
```
help(cars.clear)
Help on built-in function clear:

clear(...) method of builtins.dict instance
    D.clear() -> None.  Remove all items from D.
```

Example:
```py
>>> cars ={
...   "brand": "Ford",
...   "model": "Mustang",
...   "year": 1964
... }
>>> cars
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> cars.clear()
>>> cars
{}
>>>
```
---

### 2. copy
- The copy() method returns a copy of the specified dictionary.
- Syntax : `dict.copy()`
```
help(cart1.copy)
Help on built-in function copy:

copy(...) method of builtins.dict instance
    D.copy() -> a shallow copy of D
```
Example :
```py
>>> cart1 = { "liquid" : "water", "vegetables" : "ladiesfinger", "fruits" : "apple" }
>>> cart1
{'liquid': 'water', 'vegetables': 'ladiesfinger', 'fruits': 'apple'}
>>> cart2 = cart1.copy()
>>> cart2
{'liquid': 'water', 'vegetables': 'ladiesfinger', 'fruits': 'apple'}
>>>
```
---

### 3. fromkeys
- The `fromkeys()` method returns a dictionary with the specified keys and the specified value.
- Syntax : dict.fromkeys(keys, value)
- Parameter :
  - ___keys___(Required). 
    - An iterable specifying the keys of the new dictionary
  - ___value___(Optional). 
    - The value for all keys. Default value is None
```
help(thisdict.fromkeys)
Help on built-in function fromkeys:

fromkeys(iterable, value=None, /) method of builtins.type instance
    Create a new dictionary with keys from iterable and values set to value.
```
Example : 
```py
>>> x = ('key1', 'key2', 'key3')
>>> x
('key1', 'key2', 'key3')
>>>
>>> thisdict = x.fromkeys()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'fromkeys'
>>>
>>> thisdict = dict.fromkeys(x)
>>> thisdict
{'key1': None, 'key2': None, 'key3': None}
```
---

### 4. get
- The `get()` method returns the value of the item with the specified key.
- Syntax : `dict.get(keyname, value)`
- Parameter : 
  - ___keyname___ (Required). 
    - The keyname of the item you want to return the value from
  - ___value___	(Optional). 
    - A value to return if the specified key does not exist. Default value None
```
help(car.get)
Help on built-in function get:

get(key, default=None, /) method of builtins.dict instance
    Return the value for key if key is in the dictionary, else default.
```
Example 1 :
```py
>>> car = {
...   "brand": "Ford",
...   "model": "Mustang",
...   "year": 1964
... }
>>>
#model shd b in quotation ("model")
#>>> x = car.get(model)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'model' is not defined
>>> x = car.get("model")
>>> x
'Mustang'
>>>
```
Example 2 :
```py
>>> car = {
...   "brand": "Ford",
...   "model": "Mustang",
...   "year": 1964
... }
>>>
>>> x = car.get("price", 15000)
>>>
>>> x
15000
>>> car
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>>
```
---

### 5. items
- The `items()` method returns a view object. 
- The view object contains the key-value pairs of the dictionary, as tuples in a list.
- Syntax : `dict.items()`
```
help(a.items)
Help on built-in function items:

items(...) method of builtins.dict instance
    D.items() -> a set-like object providing a view on D's items
```
Example 1 :
```py
>>> a = {
...     "fruit" : "apple",
...     "vegetable" : "carrot",
...     "year" : 2022
... }
>>> a
{'fruit': 'apple', 'vegetable': 'carrot', 'year': 2022}
>>>
>>> a.items()
dict_items([('fruit', 'apple'), ('vegetable', 'carrot'), ('year', 2022)])
>>>
>>> b = a.items()
>>> b
dict_items([('fruit', 'apple'), ('vegetable', 'carrot'), ('year', 2022)])
>>>
```
Example 2 :
```py
>>> a = {
...     "fruit" : "apple",
...     "vegetable" : "carrot",
...     "year" : 2022
... }
>>>
>>> b = a.items()
>>> a["year"] = 2023
>>> b
dict_items([('fruit', 'apple'), ('vegetable', 'carrot'), ('year', 2023)])
>>>
```
---

### 6. keys
- The `keys()` method returns a view object. 
- The view object contains the keys of the dictionary, as a list.
- The view object will reflect any changes done to the dictionary.
- Syntax : `dict.keys()`
```
help(car.keys)
Help on built-in function keys:

keys(...) method of builtins.dict instance
    D.keys() -> a set-like object providing a view on D's keys
```
Example 1 :
```py
>>> car = {
...   "brand": "Ford",
...   "model": "Mustang",
...   "year": 1964
... }
>>> car
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>>
>>> x = car.keys()
>>> x
dict_keys(['brand', 'model', 'year'])
```
Example 2 :
```py
>>> car = {
...   "brand": "Maruthi Suzuki",
...   "model": "Alto",
...   "year": 198
... }
>>>
>>> car
{'brand': 'Maruthi Suzuki', 'model': 'Alto', 'year': 198}
>>>
>>> x = car.keys()
>>> x
dict_keys(['brand', 'model', 'year'])
>>>
>>> car["color"] = "red"
>>> x
dict_keys(['brand', 'model', 'year', 'color'])
>>> car
{'brand': 'Maruthi Suzuki', 'model': 'Alto', 'year': 198, 'color': 'red'}
>>>
```
---
### 7. pop
- The `pop()` method removes the specified item from the dictionary.
- The value of the removed item is the return value of the `pop()` method.
- Syntax : `dict.pop(keyname, defaultvalue)`
- Parameter Values : 
  - ___keyname___ (Required). 
    - The keyname of the item you want to remove.
  - ___defaultvalue___ (Optional). 
    - A value to return if the specified key do not exist.
    - If this parameter is not specified, and the no item with the specified key is found, an error is raised.

```
help(car.pop)
Help on built-in function pop:

pop(...) method of builtins.dict instance
    D.pop(k[,d]) -> v, remove specified key and return the corresponding value.

    If the key is not found, return the default if given; otherwise,
    raise a KeyError.
```
Example :
```py
>>> car = {
...   "brand": "Maruthi Suzuki",
...   "model": "Alto",
...   "year": 198
... }
>>>
>>> car.pop("brand")
'Maruthi Suzuki'
>>> car
{'model': 'Alto', 'year': 198}
>>>
```
---

### 8. popitem
- The `popitem()` method removes the item that was last inserted into the dictionary.
- The removed item is the return value of the popitem() method, as a tuple.
- Syntax : `dict.popitem()`
```
help(car.popitem)
Help on built-in function popitem:

popitem() method of builtins.dict instance
    Remove and return a (key, value) pair as a 2-tuple.

    Pairs are returned in LIFO (last-in, first-out) order.
    Raises KeyError if the dict is empty.
```
Example :
```py
>>> car = {
...   "brand": "Maruthi Suzuki",
...   "model": "Alto",
...   "year": 198
... }
>>> car.popitem()
('year', 198)
>>> car
{'brand': 'Maruthi Suzuki', 'model': 'Alto'}
>>>
>>> car.popitem()
('model', 'Alto')
>>> car
{'brand': 'Maruthi Suzuki'}
>>>
>>> car.popitem()
('brand', 'Maruthi Suzuki')
>>> car
{}
>>>
>>> car.popitem()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'popitem(): dictionary is empty'
>>> car
{}
>>>
```
---

### 9. setdefault
- The `setdefault()` method returns the value of the item with the specified key.
- If the key does not exist, insert the key, with the specified value.
- Syntax : `dict.setdefault(keyname, value)`
- Parameter Values :
  - ___keyname___	(Required). 
    - The keyname of the item you want to return the value from
  - __value___ (Optional).
    - If the key exist, this parameter has no effect.
    - If the key does not exist, this value becomes the key's value
    - Default value None
```
help(car.setdefault)
Help on built-in function setdefault:

setdefault(key, default=None, /) method of builtins.dict instance
    Insert key with a value of default if key is not in the dictionary.

    Return the value for key if key is in the dictionary, else default.
```
Example 1 :
```py
>>> car = {
...   "brand": "Maruthi Suzuki",
...   "model": "Alto",
...   "year": 198
... }
>>>
>>> car.setdefault("model", "swift")
'Alto'
>>> car
{'brand': 'Maruthi Suzuki', 'model': 'Alto', 'year': 198}
>>>
```
Example 2 :
```py
>>> car = {
...   "brand": "Maruthi Suzuki",
...   "model": "Alto",
...   "year": 198
... }
>>>
>>> x = car.setdefault("color", "red")
>>> x
'red'
>>> car
{'brand': 'Maruthi Suzuki', 'model': 'Alto', 'year': 198, 'color': 'red'}
>>>
```
---

### 10. update
- The `update()` method inserts the specified items to the dictionary.
- The specified items can be a dictionary, or an iterable object with key value pairs.
- Syntax : `dict.update(iterable)`
- Parameter Values :
  - ___iterable___	
    - A dictionary or an iterable object with key value pairs, that will be inserted to the dictionary.

```
 help(car.update)
Help on built-in function update:

update(...) method of builtins.dict instance
    D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
    If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v    In either case, this is followed by: for k in F:  D[k] = F[k]
```
Example :
```py
>>> car = {
...   "brand": "Ford",
...   "model": "Mustang",
...   "year": 1964
... }
>>>
>>> car.update({"color" : "red"})
>>> car
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
>>>
```
---

### 11. values
- The `values()` method returns a view object. 
- The view object contains the values of the dictionary, as a list.
- The view object will reflect any changes done to the dictionary.
- Syntax : `dict.values()`
```
help(car.values)
Help on built-in function values:

values(...) method of builtins.dict instance
    D.values() -> an object providing a view on D's values
```
Example :
```py
>>> car = {
...   "brand": "Maruthi Suzuki",
...   "model": "Alto",
...   "year": 198
... }
>>>
>>> z = car.values()
>>> z
dict_values(['Maruthi Suzuki', 'Alto', 198])
>>>
```
---

