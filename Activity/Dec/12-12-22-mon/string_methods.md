[TOC]
## Sring Methods


### 1. capitalize
- The `capitalize()` method returns a string where the first character is upper case, and the rest is lower case
- syntax: `name.capatilize()`

```
help(name.capitalize)

Help on built-in function capitalize:

capitalize() method of builtins.str instance
    Return a capitalized version of the string.

    More specifically, make the first character have upper case and the rest lower
    case.
```
Example:
```py
>>> name = "my Name IS aBHI"
>>> name
'my Name IS aBHI'
>>> name.capitalize()
'My name is abhi'
>>>
```
---
### 2. casefold
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

### 3. center
- The `center()` method will center align the string, using a specified character (space is default) as the fill character.
- syntax: `string.center(length, character)`
```
help(place.center)

Help on built-in function center:

center(width, fillchar=' ', /) method of builtins.str instance
    Return a centered string of length width.

    Padding is done using the specified fill character (default is a space).
```
Example:
```py
>>> txt = "Ponds Powder"
>>> txt
'Ponds Powder'
>>> txt.center(25)
'       Ponds Powder      '
>>>
# returns padded string by adding whitespace up to length 25
```
```py
>>> txt = "Ponds Powder"
>>> txt
'Ponds Powder'
>>> txt.center(20,"*")
'****Ponds Powder****'
# returns the centered padded string of length 20
```



4. count


5. encode


6. endswith


7. expandtabs


### 8. find
- The `find()` method finds the first occurrence of the specified value.
- The `find()` method returns `-1` if the value is not found.
- The `find()` method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.
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
---

9. format


10. format_map


11. index


12. isalnum


13. isalpha


14. isascii


15. isdecimal


16. isdigit


### 17. isidentifier
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
---




18.  islower


### 19. isnumeric

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




20.  isprintable


21. isspace


22. istitle


23. isupper


24. join
25. ljust
26. lower
27. lstrip
28. maketrans
29. partition
30. removeprefix
31. removesuffix
32. replace
33. rfind
34. rindex
35. rjust
36. rpartition
37. rsplit
38. rstrip



### 39. split
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
---



### 40.  splitlines
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


41.   startswith


42.  strip


43.  swapcase


44.  title


45.  translate


### 46. upper
- The `upper()` method returns a string where all characters are in upper case.
- Symbols and Numbers are ignored.
- syntax: `str.center()`

```
help(name.upper)
Help on built-in function upper:

upper() method of builtins.str instance
    Return a copy of the string converted to uppercase.
```

Example:
```py
>>> name = "AbhiShek"
>>> name
'AbhiShek'
>>> name.upper()
'ABHISHEK'
>>>
```

47.  zfill




















48. help(place.casefold)
Help on built-in function casefold:
```
casefold() method of builtins.str instance
    Return a version of the string suitable for caseless comparisons.
```
>>>











































| Methods | Origin | Defeat |
| ------- | ------ | ------ |
| strip   | char   | None   |
| split   | sep    | None   |
| upper   |        |        |
| lower   |        |        |
| filter  |        |        |
| capital |        |        |
| swap    |        |        |



----

| Sl No | Methods      | Origin | Defeat |
| ----- | ------------ | ------ | ------ |
| 1     | capital      |
| 2     | capitalize   |
| 3     | casefold     |
| 4     | center       |
| 5     | count        |
| 6     | encode       |
| 7     | endswith     |
| 8     | expandtabs   |
| 9     | filter       |
| 10    | find         |
| 11    | format       |
| 12    | format_map   |
| 13    | index        |
| 14    | split        |
| 15    | splitlines   |
| 16    | startswith   |
| 17    | strip        |
| 18    | swap         |
| 19    | swapcase     |
| 20    | title        |
| 21    | translate    |
| 22    | upper        |
| 22    | lower        |
| 23    | zfill        |
| 24    | maketrans    |
| 25    | partition    |
| 26    | removeprefix |
| 27    | removesuffix |
| 28    | replace      |
| 29    | join         |

| Sl No | Methods      | Origin | Defeat |
| ----- | ------------ | ------ | ------ |
| 1     | isalnum      |
| 2     | isalpha      |
| 3     | isascii      |
| 4     | isdecimal    |
| 5     | isdigit      |
| 6     | isidentifier |
| 7     | islower      |
| 8     | isnumeric    |
| 9     | isprintable  |
| 10    | isspace      |
| 11    | istitle      |
| 12    | isupper      |

| Sl No | Methods | Origin | Defeat |
| ----- | ------- | ------ | ------ |
| 1     | ljust   |
| 2     | lstrip  |


| Sl No | Methods    | Origin | Defeat |
| ----- | ---------- | ------ | ------ |
| 1     | rfind      |
| 2     | rindex     |
| 3     | rjust      |
| 4     | rpartition |
| 5     | rsplit     |
| 6     | rstrip     |


---
---
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
---
---