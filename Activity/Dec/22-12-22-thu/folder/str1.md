[TOC]

### String

1. Differentiate between the following.
    a. isidintifier() and isnumeric()
    b. find() and casefold()
    c. split() and splitlines()




## a.)
### isidentifier()
- The `isidentifier()` method returns `True` if the string is a valid identifier, otherwise `False`.
- A string is considered a valid identifier if it only contains alphanumeric letters (`a-z`) and (`0-9`), or underscores (`_`).
- A valid identifier cannot start with a number, or contain any spaces.
- syntax : `str.isidentifier()`

```
help(a.isidentifier)
Help on built-in function isidentifier:

isidentifier() method of builtins.str instance
    Return True if the string is a valid Python identifier, False otherwise.

    Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
    such as "def" or "class".
```

Example :
```py
>>> a = "Abhishek"
>>> b = "abhi08"
>>> c = "20five"
>>> d = "Wel come"
>>> e = "Manoj_o5"
>>>
>>> print(a.isidentifier())
True
>>> print(b.isidentifier())
True
>>> print(c.isidentifier())
False
>>> print(d.isidentifier())
False
>>> print(e.isidentifier())
True
```

### isnumeric()

- The `isnumeric()` method returns `True` if all the characters are numeric `(0-9)`, otherwise `False`.
- Exponents, like `²` and `¾` are also considered to be numeric values.
- `"-1"` and `"1.5"` are NOT considered numeric values, because all the characters in the string must be numeric, and the `-` and the `.` are not.
- syntax : `str.isnumeric()`
```
>>> help(b.isnumeric)
Help on built-in function isnumeric:

isnumeric() method of builtins.str instance
    Return True if the string is a numeric string, False otherwise.

    A string is numeric if all characters in the string are numeric and there is at least one character in the string.

```
Example :
```py
>>> a = 12345
>>> b = "2343"
>>> c = "abcd1234"
>>> d = "-34"
>>> e = "8.5"
>>>
>>> print(a.isnumeric())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'isnumeric'
>>> print(b.isnumeric())
True
>>> print(c.isnumeric())
False
>>> print(d.isnumeric())
False
>>> print(e.isnumeric())
False
>>>
```
---
---

## b.)
### find()

- The `find()` method finds the first occurrence of the specified value.
- The `find()` method returns `-1` if the value is not found.
- The `find()` method is almost the same as the `index()` method, the only difference is that the `index()` method raises an exception if the value is not found.
- Syntax : `string.find(value, start, end)`

> `value` Required. The value to search for

> `start` Optional. Where to start the search. Default is `0`

> `end`	Optional. Where to end the search. Default is to the end of the string


```
help(a.find)
Help on built-in function find:

find(...) method of builtins.str instance
    S.find(sub[, start[, end]]) -> int

    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Return -1 on failure.
```

Example :
```py
>>> a = "Hello Everyone, How are you?"
>>> a
'Hello Everyone, How are you?'
>>> a.find("Hello")
0
>>> a.find("Everyone")
6
>>> a.find("o")
4
>>> a.find("v", 5, 10)
7
>>> a.find("z")
-1
>>>
```


### casefold()
- The `casefold()` method returns a string where all the characters are lower case.
- This method is similar to the `lower()` method, but the `casefold()` method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the `casefold()` method.
- syntax: `str.casefold()`
```
help(txt.casefold)

Help on built-in function casefold:

casefold() method of builtins.str instance
    Return a version of the string suitable for caseless comparisons.
```
Example:
```py
>>> txt = "Hello, And Welcome To My World!"
>>> txt
'Hello, And Welcome To My World!'
>>> txt.casefold()
'hello, and welcome to my world!'
>>>
```
---
---


## c.)
### split()
- The `split()` method splits a string into a list.
- You can specify the separator, default separator is any whitespace.
- Note: When maxsplit is specified, the list will contain the specified number of elements plus one.
- Syntax : `str.split(separator, maxsplit)`

> ___separator___ Optional. Specifies the separator to use when splitting the string.
> By default any whitespace is a separator

> ___maxsplit___ Optional. Specifies how many splits to do.
> Default value is -1, which is "all occurrences"


Example 1 :
```py
>>> t = "Why this kolaveri kolaveri kolaveri di"
>>> t.split()
['Why', 'this', 'kolaveri', 'kolaveri', 'kolaveri', 'di']
>>>
```
Example 2 :
```py
>>> s = "Why this, kolaveri kolaveri kolaveri, di"
>>> s.split(",")
['Why this', ' kolaveri kolaveri kolaveri', ' di']
>>>
```
Example 3 :
```py
>>> g = "Why#this#kolaveri#kolaveri#kolaveri#di"
>>> g.split("#" , 1)
['Why', 'this#kolaveri#kolaveri#kolaveri#di']
>>>
>>> g.split("#" , 2)
['Why', 'this', 'kolaveri#kolaveri#kolaveri#di']
>>>
>>> g.split("#" , 3)
['Why', 'this', 'kolaveri', 'kolaveri#kolaveri#di']
>>>
>>> g.split("#" , 4)
['Why', 'this', 'kolaveri', 'kolaveri', 'kolaveri#di']
>>>
>>> g.split("#" , 5)
['Why', 'this', 'kolaveri', 'kolaveri', 'kolaveri', 'di']
>>>
```


### splitlines()

- The `splitlines()` method splits a string into a list.
- The splitting is done at line breaks.
- Syntax : `str.splitlines(keeplinebreaks)`

> ___keeplinebreaks___	Optional. 
> Specifies if the line breaks should be included (`True`), or not (`False`).
> Default value is `False`

```
help(ab.splitlines)
Help on built-in function splitlines:

splitlines(keepends=False) method of builtins.str instance
    Return a list of the lines in the string, breaking at line boundaries.

    Line breaks are not included in the resulting list unless keepends is given and    true.
```

Example 1 :
```py
>>> ab = "My name i Abhishek\nI stay in Bengaluru"
>>> ab.splitlines()
['My name i Abhishek', 'I stay in Bengaluru']
>>>
```
Example 2 :
```py
>>> ab = "My name i Abhishek\nI stay in Bengaluru"
>>> ab.splitlines(True)
['My name i Abhishek\n', 'I stay in Bengaluru']
>>>
>>> ab.splitlines(False)
['My name i Abhishek', 'I stay in Bengaluru']
>>>
```
---