[TOC]
## Sring Methods
## Incomplete (10, 24, 28, 30, 31, 45)
## There are 47 String Methods.


### 1. capitalize
- The `capitalize()` method returns a string where the first character is upper case, and the rest is lower case
- syntax : `name.capatilize()`
```
help(name.capitalize)

Help on built-in function capitalize:

capitalize() method of builtins.str instance
    Return a capitalized version of the string.

    More specifically, make the first character have upper case and the rest lower
    case.
```
Example :
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
- syntax : `str.casefold()`
```
help(txt.casefold)

Help on built-in function casefold:

casefold() method of builtins.str instance
    Return a version of the string suitable for caseless comparisons.
```
Example :
```py
>>> txt = "Hello, And Welcome To My World!"
>>> txt
'Hello, And Welcome To My World!'
>>> txt.casefold()
'hello, and welcome to my world!'
>>>
```
---

### 3. center
- The `center()` method will center align the string, using a specified character (space is default) as the fill character.
- syntax : `string.center(length, character)`
- Parameter	Value :
  - ___length___ (Required). 
    - The length of the returned string.
  - ___character___ (Optional). 
    - The character to fill the missing space on each side. Default is " " (space)
```
help(place.center)

Help on built-in function center:

center(width, fillchar=' ', /) method of builtins.str instance
    Return a centered string of length width.

    Padding is done using the specified fill character (default is a space).
```
Example 1 :
```py
>>> txt = "Ponds Powder"
>>> txt
'Ponds Powder'
>>> txt.center(25)
'       Ponds Powder      '
>>>
# returns padded string by adding whitespace up to length 25
```
Example 2 :
```py
>>> txt = "Ponds Powder"
>>> txt
'Ponds Powder'
>>> txt.center(20,"*")
'****Ponds Powder****'
# returns the centered padded string of length 20
```
---

### 4. count
- The `count()` method returns the number of times a specified value appears in the string.
- Syntax : `string.count(value, start, end)`
- Parameter Values :
  - ___value___	(Required). 
    - A String. The string to value to search for.
  - ___start___	(Optional). 
    - An Integer. The position to start the search. Default is `0`.
  - ___end___	(Optional). 
    - An Integer. The position to end the search. Default is the end of the string.
```
help(info.count)
Help on built-in function count:

count(...) method of builtins.str instance
    S.count(sub[, start[, end]]) -> int

    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.
```
Example 1 :
```py
>>> info = "My name is Abhi, I am Abhi"
>>> info
'My name is Abhi, I am Abhi'
>>> info.count("Abhi")
2
>>>
>>> info = "1 My name is Abhi, I 1 am 1 Abhi"
>>> info
'1 My name is Abhi, I 1 am 1 Abhi'
>>> info.count("1")
3
>>>
```
Example 2 :
```py
>>> info = "My name is Abhi, I am Abhi"
>>> info.count("Abhi", 16, 30)
1
```
---

### 5. encode
- The `encode()` method encodes the string, using the specified encoding. 
- If no encoding is specified, UTF-8 will be used.
- Syntax : `string.encode(encoding=encoding, errors=errors)`
- Parameter Values :
  - ___encoding___	(Optional). 
    - A String specifying the encoding to use. Default is UTF-8
  - ___errors___ (Optional). 
    - A String specifying the error method. Legal values are:
    - `backslashreplace`, `ignore`, `namereplace`, `strict`, `replace`, `xmlcharrefreplace`
  
| Parameter | Description                                                                                  |
| --------- | -------------------------------------------------------------------------------------------- |
| encoding  | (Optional). A String specifying the encoding to use. Default is UTF-8                        |
| errors    | (Optional). A String specifying the error method. Legal values are:                          |
|           | `'backslashreplace'`  - uses a backslash instead of the character that could not be encoded. |
|           | `'ignore'`            - ignores the characters that cannot be encoded.                       |
|           | `'namereplace'`       - replaces the character with a text explaining the character.         |
|           | `'strict'`            - Default, raises an error on failure.                                 |
|           | `'replace'`           - replaces the character with a questionmark.                          |
|           | `'xmlcharrefreplace'` - replaces the character with an xml character.                        |
```
help(info.encode)
Help on built-in function encode:

encode(encoding='utf-8', errors='strict') method of builtins.str instance
    Encode the string using the codec registered for encoding.

    encoding
      The encoding in which to encode the string.
    errors
      The error handling scheme to use for encoding errors.
      The default is 'strict' meaning that encoding errors raise a
      UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
      'xmlcharrefreplace' as well as any other name registered with
      codecs.register_error that can handle UnicodeEncodeErrors.
```
Example 1 :
```py
>>> txt = "My name is Âbhï"
>>> e = txt.encode()
>>> e
b'My name is \xc3\x82bh\xc3\xaf'
>>>
```
Example 2 :
```py
>>> txt = "My name is Âbhï"
>>> txt
'My name is Âbhï'
>>>
>>> txt.encode(encoding="ascii",errors="backslashreplace")
b'My name is \\xc2bh\\xef'
>>> txt.encode(encoding="ascii",errors="ignore")
b'My name is bh'
>>> txt.encode(encoding="ascii",errors="namereplace")
b'My name is \\N{LATIN CAPITAL LETTER A WITH CIRCUMFLEX}bh\\N{LATIN SMALL LETTER I WITH DIAERESIS}'
>>> txt.encode(encoding="ascii",errors="replace")
b'My name is ?bh?'
>>> txt.encode(encoding="ascii",errors="xmlcharrefreplace")
b'My name is &#194;bh&#239;'
>>>
>>> txt.encode(encoding="ascii",errors="strict")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode character '\xc2' in position 11: ordinal not in range(128)
>>>
```
---

### 6. endswith
- The `endswith()` method returns True if the string ends with the specified value, otherwise False.
- Syntax : `string.endswith(value, start, end)`
- Parameter Values :
    - ___value___ (Required). 
      - The value to check if the string ends with
    - ___start___	(Optional).
      - An Integer specifying at which position to start the search
  - ___end___	(Optional). 
    - An Integer specifying at which position to end the search
```
help(txt.endswith)
Help on built-in function endswith:

endswith(...) method of builtins.str instance
    S.endswith(suffix[, start[, end]]) -> bool

    Return True if S ends with the specified suffix, False otherwise.
    With optional start, test S beginning at that position.
    With optional end, stop comparing S at that position.
    suffix can also be a tuple of strings to try.
```
Example 1 :
```py
>>> txt = "Hi..., My name is abhi."
>>> txt
'Hi..., My name is abhi.'
>>> name= txt.endswith(".")
>>> name
True
>>>
>>> name= txt.endswith("abhi.")
>>> name
True
>>>
>>>
>>> name= txt.endswith("i")
>>> name
False
>>>
```
Example 2 :
```py
>>> txt = "Hi..., My name is abhi."
>>> txt
'Hi..., My name is abhi.'
>>> name = txt.endswith(".", 1, 50)
>>> name
True
>>>
>>> name = txt.endswith(".", 5, 10)
>>> name
False
>>>
```
---

### 7. expandtabs
- The `expandtabs()` method sets the tab size to the specified number of whitespaces.
- Syntax : `string.expandtabs(tabsize)`
- Parameter Values :
  - ___tabsize___	(Optional). 
    - A number specifying the tabsize. Default tabsize is `8`.    
```
help(txt.expandtabs)
Help on built-in function expandtabs:

expandtabs(tabsize=8) method of builtins.str instance
    Return a copy where all tab characters are expanded using spaces.

    If tabsize is not given, a tab size of 8 characters is assumed.
```
Example 1 :
```py
>>> txt = "A\b\h\i\sh\ek"
>>> name = txt.expandtabs(2)
>>> name
'A\x08\\h\\i\\sh\\ek'
>>>
```
---

### 8. find
- The `find()` method finds the first occurrence of the specified value.
- The `find()` method returns `-1` if the value is not found.
- The `find()` method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.
- Syntax : `string.find(value, start, end)`
- Parameter Value :
  - ___value___ (Required). 
    - The value to search for

  - ___start___ (Optional). 
    - Where to start the search. Default is `0`

  - ___end___ (Optional). 
    - Where to end the search. Default is to the end of the string.
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

### 9. format
- The `format()` method formats the specified value(s) and insert them inside the string's placeholder.
- The placeholder is defined using curly brackets `{}`.
- The `format()` method returns the formatted string.
- Syntax : `string.format(value1, value2...)`
- Parameter Values : 
  - ___value1, value2...___	(Required). 
    - One or more values that should be formatted and inserted in the string.
    - The values are either a list of values separated by commas, a key=value list, or a combination of both.
    - The values can be of any data type.
-  The Placeholders : 
   - The placeholders can be identified using named indexes `{price}`, numbered indexes `{0}`, or even empty placeholders `{}`.
```
>>> help(txt1.format)
Help on built-in function format:

format(...) method of builtins.str instance
    S.format(*args, **kwargs) -> str

    Return a formatted version of S, using substitutions from args and kwargs.
    The substitutions are identified by braces ('{' and '}').
```
Example :
```py
>>> #named indexes:
>>> txt1 = "My name is {fname}, I'm {age}"
>>> #numbered indexes:
>>> txt2 = "My name is {0}, I'm {1}"
>>> #empty placeholders:
>>> txt3 = "My name is {}, I'm {}"
>>>
>>> txt1.format(fname = "John", age = 36)
>>> txt1
"My name is John, I'm 36"
>>>
>>> txt2.format("John",36)
"My name is John, I'm 36"
>>>
>>> txt3.format("John",36)
"My name is John, I'm 36"
>>>
>>>
>>> type(txt1)
<class 'str'>
>>>
>>> type(txt1.format)
<class 'builtin_function_or_method'>
```
---

### 10.  format_map (Incomplete)

```
type(txt1.format_map)
<class 'builtin_function_or_method'>
>>> help(txt1.format_map)
Help on built-in function format_map:

format_map(...) method of builtins.str instance
    S.format_map(mapping) -> str

    Return a formatted version of S, using substitutions from mapping.
    The substitutions are identified by braces ('{' and '}').
```
Example :
```py

```
---

### 11.  index
- The `index()` method finds the first occurrence of the specified value.
- The `index()` method raises an exception if the value is not found.
- The `index()` method is almost the same as the `find()` method, the only difference is that the `find()` method returns `-1` if the value is not found.
- Syntax : `string.index(value, start, end)`
- Parameter Values : 
  - ___value___ (Required). 
    - The value to search for.
  - ___start___ (Optional). 
    - Where to start the search. Default is `0`.
  - ___end___	(Optional). 
    - Where to end the search. Default is to the end of the string.
```
help(txt.index)
Help on built-in function index:

index(...) method of builtins.str instance
    S.index(sub[, start[, end]]) -> int

    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Raises ValueError when the substring is not found.
```
Example :
```py
>>> txt = "I love Bengaluru."
>>> x = txt.index("I")
>>> x
0
>>> x = txt.index("l")
>>> x
2
>>> x = txt.index("love")
>>> x
2
>>> x = txt.index("B")
>>> x
7
>>> x = txt.index("Bengaluru")
>>> x
7
>>>
```
Example 2 :
```py
>>> txt = "I love Bengaluru."
>>> x = txt.index("B", 5, 15)
>>> x
7
>>>
```
---

### 12. isalnum
- The `isalnum()` method returns `True` if all the characters are alphanumeric, meaning alphabet letter `(a-z)` and numbers `(0-9)`.
- Example of characters that are not alphanumeric : (space)!#%&? etc.
- Syntax : `string.isalnum()`
```
Help on built-in function isalnum:

isalnum() method of builtins.str instance
    Return True if the string is an alpha-numeric string, False otherwise.

    A string is alpha-numeric if all characters in the string are alpha-numeric and    there is at least one character in the string.
```
Example :
```py
>>> txt1 = "abhi"
>>> txt2 = "abhi8"
>>> txt3 = "@abhi8"
>>> txt4 = "abhi@8"
>>> txt5 = "abhi 8"
>>> txt6 = "abhi_8"
>>> txt7 = "@abhi_8"
>>>
>>>
>>> txt1.isalnum()
True
>>> txt2.isalnum()
True
>>> txt3.isalnum()
False
>>> txt4.isalnum()
False
>>> txt5.isalnum()
False
>>> txt6.isalnum()
False
>>> txt7.isalnum()
False
>>>
```
---

### 13. isalpha
- The `isalpha()` method returns `True` if all the characters are alphabet letters (A-Z), (a-z).
- Example of characters that are not alphabet letters: (space)!#%&? etc.
- Syntax : `string.isalpha()`
```
help(txt1.isalpha)
Help on built-in function isalpha:

isalpha() method of builtins.str instance
    Return True if the string is an alphabetic string, False otherwise.

    A string is alphabetic if all characters in the string are alphabetic and there    is at least one character in the string.
```
Example :
```py
>>> txt1 = "BigBoss"
>>> txt1.isalpha()
True
>>>
>>>
>>> txt2 = "Big Boss"
>>> txt2.isalpha()
False
>>>
>>>
>>> txt3 = "bigboss88"
>>> txt3.isalpha()
False
>>>
```
---

### 14. isascii
- The `isascii()` method returns `True` if all the characters are ascii characters `(a-z)`.
- Syntax : `string.isascii()`
```
help(txt1.isascii)
Help on built-in function isascii:

isascii() method of builtins.str instance
    Return True if all characters in the string are ASCII, False otherwise.

    ASCII characters have code points in the range U+0000-U+007F.
    Empty string is ASCII too.
```
Example :
```py
>>> txt1 = "abhishek8"
>>> txt2 = "@abhishek8"
>>>
>>> txt1.isascii()
True
>>> txt2.isascii()
True
>>> txt3 = "@abhishek 8"
>>> txt3.isascii()
True
>>>
```
---

### 15. isdecimal
- The `isdecimal()` method returns `True` if all the characters are decimals `(0-9)`.
- This method is used on unicode objects.
- Syntax : `string.isdecimal()`
```
help(x.isdecimal)
Help on built-in function isdecimal:

isdecimal() method of builtins.str instance
    Return True if the string is a decimal string, False otherwise.

    A string is a decimal string if all characters in the string are decimal and
    there is at least one character in the string.
```
Example :
```py
>>> a = "aa08"
>>> a.isdecimal()
False
>>>
>>>
>>> b = "089"
>>> b.isdecimal()
True
>>>
>>>
>>> x = "Abhi"
>>> x.isdecimal()
False
>>>
>>> y = "abhi0123"
>>> y.isdecimal()
False
>>>
>>> z = "24680"
>>> z.isdecimal()
True
>>>
```
---

### 16. isdigit
- The `isdigit()` method returns `True` if all the characters are digits, otherwise `False`.
- Exponents, like ², are also considered to be a digit.
Syntax : `string.isdigit()`
```
help(d1.isdigit)
Help on built-in function isdigit:

isdigit() method of builtins.str instance
    Return True if the string is a digit string, False otherwise.

    A string is a digit string if all characters in the string are digits and there    is at least one character in the string.
```
Example :
```py
>>> d1 = "2345"
>>> d1.isdigit()
True
>>>
>>> d2 = "name"
>>> d2.isdigit()
False
>>>
>>> d3 = "5²"
>>> d3.isdigit()
True
```
---

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

### 18.   islower
- The `islower()` method returns `True` if all the characters are in lower case, otherwise `False`.
- Numbers, symbols and spaces are not checked, only alphabet characters.
- Syntax : `string.islower()`
```
help(a.islower)
Help on built-in function islower:

islower() method of builtins.str instance
    Return True if the string is a lowercase string, False otherwise.

    A string is lowercase if all cased characters in the string are lowercase and
    there is at least one cased character in the string.
```
Example :
```py
>>> a = "My Name Is Abhishek"
>>> b = "Abhishek"
>>> c = "abhishek"
>>> d = "abhishek123"
>>>
>>> a.islower()
False
>>> b.islower()
False
>>> c.islower()
True
>>> d.islower()
True
```
---

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
---

### 20. isprintable
- The `isprintable()` method returns `True` if all the characters are printable, otherwise `False`.
- Example of none printable character can be carriage return and line feed.
- Syntax : `string.isprintable()`
```
help(p.isprintable)
Help on built-in function isprintable:

isprintable() method of builtins.str instance
    Return True if the string is printable, False otherwise.

    A string is printable if all of its characters are considered printable in
    repr() or if it is empty.
```
Example : 
```py
>>> p = "I love Bengaluru"
>>> p.isprintable()
True
>>>
>>> p1 = "I\nlove #Bengaluru"
>>> p1.isprintable()
False
>>>
```
---

### 21. isspace
- The `isspace()` method returns `True` if all the characters in a string are whitespaces, otherwise `False`.
- Syntax : `string.isspace()`
```
 help(a.isspace)
Help on built-in function isspace:

isspace() method of builtins.str instance
    Return True if the string is a whitespace string, False otherwise.

    A string is whitespace if all characters in the string are whitespace and there    is at least one character in the string.
```
Example :
```py
>>> a = "    "
>>> a.isspace()
True
>>>
>>> b = "    abhi    "
>>> b.isspace()
False
>>>
```
---

### 22. istitle
- The `istitle()` method returns `True` if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise `False`.
- Symbols and numbers are ignored.
- Syntax : `string.istitle()`
```
 help(a.istitle)
Help on built-in function istitle:

istitle() method of builtins.str instance
    Return True if the string is a title-cased string, False otherwise.

    In a title-cased string, upper- and title-case characters may only
    follow uncased characters and lowercase characters only cased ones.
```
Example :
```py
>>> a = "Hello, And Welcome To My World!"
>>> a.istitle()
True
>>>
>>> b = "HELLO, AND WELCOME TO MY WORLD"
>>> b.istitle()
False
>>>
>>> c = "Hello"
>>> c.istitle()
True
>>>
>>> d = "HELLO"
>>> d.istitle()
False
>>>
>>> e = "!@#$% Abcd ^&?*-"
>>> e.istitle()
True
>>>
```
---

### 23. isupper
- The `isupper()` method returns `True` if all the characters are in upper case, otherwise `False`.
- Numbers, symbols and spaces are not checked, only alphabet characters.
- Syntax : `string.isupper()`
```
 help(a.isupper)
Help on built-in function isupper:

isupper() method of builtins.str instance
    Return True if the string is an uppercase string, False otherwise.

    A string is uppercase if all cased characters in the string are uppercase and
    there is at least one cased character in the string.
```
Example :
```py
>>> a = "ABHISHEK"
>>> a.isupper()
True
>>> a = "Abhishek"
>>>
>>> b = "Abhishek"
>>> b.isupper()
False
>>>
>>> c = "1235846"
>>> c.isupper()
False
>>>
>>> d = "!@#$%?  UPPER  >?<&*"
>>> d.isupper()
True
>>>
```
---

### 24. join (Incomplete)
- The `join()` method takes all items in an iterable and joins them into one string.
- A string must be specified as the separator.
Syntax : `string.join(iterable)`
- Parameter Values :
  - ___iterable___ (Required). 
    - Any iterable object where all the returned values are strings
```

```
Example :
```py
>>> names = "Abhi", "Chandhu", "Rahul"
>>> names.join()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'join'
>>>
>>> names.join(#)
...
...
...
... ^Z

  File "<stdin>", line 1
    names.join(#)
              ^
SyntaxError: '(' was never closed
>>>
>>> help(names.join)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'join'
>>>
```
---

### 25. ljust
- The `ljust()` method will left align the string, using a specified character (space is default) as the fill character.
- Syntax : `string.ljust(length, character)`
- Parameter Values :
  - ___length___	(Required). 
    - The length of the returned string
  - ___character___	(Optional). 
    - A character to fill the missing space (to the right of the string). Default is " " (space).
```
help(a.ljust)
Help on built-in function ljust:

ljust(width, fillchar=' ', /) method of builtins.str instance
    Return a left-justified string of length width.

    Padding is done using the specified fill character (default is a space).
```
Example :
```py
>>> a = "Apple"
>>> x = a.ljust(25)
>>> x
'Apple                    '
>>> print(x, "is my favorite fruit.")
Apple                     is my favorite fruit.
>>>
>>> x = a.ljust(25, "#")
>>> x
'Apple####################'
>>> print(x, "is my favorite fruit.")
Apple#################### is my favorite fruit.
```
---

### 26. lower
- The `lower()` method returns a string where all characters are lower case.
- Symbols and Numbers are ignored.
- Syntax : `string.lower()`
```
   help(txt1.lower)
Help on built-in function lower:

lower() method of builtins.str instance
    Return a copy of the string converted to lowercase.
```
Example :
```py
>>> txt1 = "My name is ABHISHEK"
>>> txt1.lower()
'my name is abhishek'
>>>
```
---

### 27. lstrip
- The `lstrip()` method removes any leading characters (space is the default leading character to remove)
- Syntax : `string.lstrip(characters)`
- Parameter Values :
  - ___characters___ (Optional). 
    - A set of characters to remove as leading characters.
```
help(a.lstrip)
Help on built-in function lstrip:

lstrip(chars=None, /) method of builtins.str instance
    Return a copy of the string with leading whitespace removed.

    If chars is given and not None, remove characters in chars instead.
```
Example :
```py
>>> a = "    Apple    "
>>> a.lstrip()
'Apple    '
>>>
>>>
>>> b = "               TEXT"
>>> b.lstrip()
'TEXT'
>>> c = "### .. abbccc...Apple"
>>> z = c.lstrip("#, ., a, b, c")
>>> z
'Apple'
>>>
```
---

### 28. maketrans (Incomplete)
- The `maketrans()` method returns a mapping table that can be used with the `translate()` method to replace specified characters.
- Syntax : `string.maketrans(x, y, z)`
- Parameter Values
  - ___x___	(Required). 
    - If only one parameter is specified, this has to be a dictionary describing how to perform the replace. If two or more parameters are specified, this parameter has to be a string specifying the characters you want to replace.
  - ___y___	(Optional). 
    - A string with the same length as parameter x. Each character in the first parameter will be replaced with the corresponding character in this string.
  - ___z___	(Optional). 
    - A string describing which characters to remove from the original string.
```
help(txt.maketrans)
Help on built-in function maketrans:

maketrans(...)
    Return a translation table usable for str.translate().

    If there is only one argument, it must be a dictionary mapping Unicode
    ordinals (integers) or characters to Unicode ordinals, strings or None.
    Character keys will be then converted to ordinals.
    If there are two arguments, they must be strings of equal length, and
    in the resulting dictionary, each character in x will be mapped to the
    character at the same position in y. If there is a third argument, it
    must be a string, whose characters will be mapped to None in the result.
```
Example :
```py
>>> txt = "Hi... My name is Abhi!"
>>> op = txt.maketrans("A")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: if you give only one argument to maketrans it must be a dict
>>> op = txt.maketrans("A", "P")
>>> op
{65: 80}
```
---

### 29. partition
- The `partition()` method searches for a specified string, and splits the - string into a tuple containing three elements.
- The first element contains the part before the specified string.
- The second element contains the specified string.
- The third element contains the part after the string.
- This method searches for the first occurrence of the specified string.
- Syntax : `string.partition(value)`
- Parameter Values : 
  - ___value___	(Required). 
    - The string to search for
```
   help(txt.partition)
Help on built-in function partition:

partition(sep, /) method of builtins.str instance
    Partition the string into three parts using the given separator.

    This will search for the separator in the string.  If the separator is found,
    returns a 3-tuple containing the part before the separator, the separator
    itself, and the part after it.

    If the separator is not found, returns a 3-tuple containing the original string    and two empty strings.
```
Example :
```py
>>> txt = "I could eat bananas all day"
>>> txt.partition("bananas")
('I could eat ', 'bananas', ' all day')
>>> txt.partition("apples")
('I could eat bananas all day', '', '')
>>>
```
---

### 30. removeprefix (Incomplete)

```
help(txt.removeprefix)
Help on built-in function removeprefix:

removeprefix(prefix, /) method of builtins.str instance
    Return a str with the given prefix string removed if present.

    If the string starts with the prefix string, return string[len(prefix):].
    Otherwise, return a copy of the original string.
```
Example :
```py

```
---

### 31. removesuffix (Incomplete)

```
help(txt.removesuffix)
Help on built-in function removesuffix:

removesuffix(suffix, /) method of builtins.str instance
    Return a str with the given suffix string removed if present.

    If the string ends with the suffix string and that suffix is not empty,
    return string[:-len(suffix)]. Otherwise, return a copy of the original
    string.
```
Example :
```py

```
---

### 32. replace
- The `replace()` method replaces a specified phrase with another specified phrase.
- All occurrences of the specified phrase will be replaced, if nothing else is specified.
- Syntax : `string.replace(oldvalue, newvalue, count)`
- Parameter Values :
  - ___oldvalue___	(Required). 
    - The string to search for
  - ___newvalue___ (Required). 
    - The string to replace the old value with
  - ___count___ (Optional). 
    - A number specifying how many occurrences of the old value you want to replace. Default is all occurrences
```
help(txt.replace)
Help on built-in function replace:

replace(old, new, count=-1, /) method of builtins.str instance
    Return a copy with all occurrences of substring old replaced by new.

      count
        Maximum number of occurrences to replace.
        -1 (the default value) means replace all occurrences.

    If the optional argument count is given, only the first count occurrences are
    replaced.
```
Example 1 :
```py
>>> txt = "I love Bengaluru"
>>> txt
'I love Bengaluru'
>>> txt.replace("Bengaluru", "GOA")
'I love GOA'
>>>
>>> txt.replace("Bengaluru", "GOA", 2)
'I love GOA'
>>>
```
Example 2 :
```py
# Arguments should be String not Int
>>> txt = "My favourite number is = 2, 4, 8, 8"
>>> txt
'My favourite number is = 2, 4, 8, 8'
>>> txt.replace(8, 5, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: replace() argument 1 must be str, not int

>>> txt = "one one and two two."
>>> txt.replace(two, five, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'two' is not defined
>>> txt.replace("two", "five", 2)
'one one and five five.'
```
---

### 33. rfind
- The `rfind()` method finds the last occurrence of the specified value.
- The `rfind()` method returns `-1` if the value is not found.
- The `rfind()` method is almost the same as the `rindex()` method.
- Syntax : `string.rfind(value, start, end)`
- Parameter Values : 
  - ___value___ (Required). 
    - The value to search for
  - ___start___	(Optional). 
    - Where to start the search. Default is 0
  - ___end___	(Optional). 
    - Where to end the search. Default is to the end of the string
```
   help(txt1.rfind)
Help on built-in function rfind:

rfind(...) method of builtins.str instance
    S.rfind(sub[, start[, end]]) -> int

    Return the highest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Return -1 on failure.
```
Example :
```py
>>> txt1 = "I love Biriyani"
>>> txt1.rfind("love")
2
>>> txt1.rfind("n")
13
>>> txt1.rfind("i", 5, 9)
8
>>> txt1.rfind("z")
-1
>>>
>>> txt1.rfind("q")
-1
>>>
```
---

### 34. rindex
- The `rindex()` method finds the last occurrence of the specified value.
- The `rindex()` method raises an exception if the value is not found.
- The `rindex()` method is almost the same as the `rfind()` method.
- Syntax : `string.rindex(value, start, end)`
- Parameter Values
  - ___Value___	(Required). 
    - The value to search for
  - ___start___	Optional). 
    - Where to start the search. Default is 0
  - ___end___	(Optional). 
    - Where to end the search. Default is to the end of the string
```
   help(txt1.rindex)
Help on built-in function rindex:

rindex(...) method of builtins.str instance
    S.rindex(sub[, start[, end]]) -> int

    Return the highest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Raises ValueError when the substring is not found.
```
Example :
```py
>>> txt1 = "I love Chicken"
>>> txt1.rindex("love")
2
>>> txt1.rindex("k")
11
>>> txt1.rindex("i")
9
>>> txt1.rindex("i", 5, 10)
9
>>> txt1.index("e", 1, 6)
5
>>> txt1.index("z")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
>>>
```
---

### 35. rjust
- The `rjust()` method will right align the string, using a specified character (space is default) as the fill character.
- Syntax : `string.rjust(length, character)`
- Parameter Values :
  - ___length___ (Required). 
    - The length of the returned string.
  - ___character___	(Optional). 
    - A character to fill the missing space (to the left of the string).
    - Default is " " (space).
```
help(a.rjust)
Help on built-in function rjust:

rjust(width, fillchar=' ', /) method of builtins.str instance
    Return a right-justified string of length width.

    Padding is done using the specified fill character (default is a space).
```
Example :
```py
>>> a = "Apple"
>>> x = a.rjust(25)
>>> x
'                    Apple'
>>> x = a.rjust(25, "@")
>>> x
'@@@@@@@@@@@@@@@@@@@@Apple'
>>>
>>> print(x, "is my favorite fruit.")
@@@@@@@@@@@@@@@@@@@@Apple is my favorite fruit.
>>>
```
---

### 36. rpartition
- The `rpartition()` method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.
- The first element contains the part before the specified string.
- The second element contains the specified string.
- The third element contains the part after the string.
- Syntax : `string.rpartition(value)`
- Parameter Values :
  - ___value___ (Required). 
    - The string to search for.
```
help(txt.rpartition)
Help on built-in function rpartition:

rpartition(sep, /) method of builtins.str instance
    Partition the string into three parts using the given separator.

    This will search for the separator in the string, starting at the end. If
    the separator is found, returns a 3-tuple containing the part before the
    separator, the separator itself, and the part after it.

    If the separator is not found, returns a 3-tuple containing two empty strings
    and the original string.
```
Example :
```py
>>> txt = "I could eat bananas all day, bananas are my favorite fruit"
>>> txt.rpartition("bananas")
('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')
>>>
>>> txt.rpartition("apples")
('', '', 'I could eat bananas all day, bananas are my favorite fruit')
>>>
```
---

### 37. rsplit
- The `rsplit()` method splits a string into a list, starting from the right.
- If no "max" is specified, this method will return the same as the `split()` method.
- When maxsplit is specified, the list will contain the specified number of elements plus one.
- Syntax : `string.rsplit(separator, maxsplit)`
- Parameter Values : 
  - ___separator___	(Optional). 
    - Specifies the separator to use when splitting the string. By default any whitespace is a separator.
  - ___maxsplit___ (Optional). 
    - Specifies how many splits to do. Default value is `-1`, which is "all occurrences"

```
help(txt.rsplit)
Help on built-in function rsplit:

rsplit(sep=None, maxsplit=-1) method of builtins.str instance
    Return a list of the substrings in the string, using sep as the separator string.

      sep
        The separator used to split the string.

        When set to None (the default value), will split on any whitespace
        character (including \\n \\r \\t \\f and spaces) and will discard
        empty strings from the result.
      maxsplit
        Maximum number of splits (starting from the left).
        -1 (the default value) means no limit.

    Splitting starts at the end of the string and works to the front.
```
Example :
```py
>>> txt = "Apple Mango Banana"
>>> txt.rsplit()
['Apple', 'Mango', 'Banana']
```
---

### 38. rstrip
- The `rstrip()` method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
- Syntax : `string.rstrip(characters)`
- Parameter Values :
  - ___characters___ (Optional). 
    - A set of characters to remove as trailing characters.
```
help(a.rstrip)
Help on built-in function rstrip:

rstrip(chars=None, /) method of builtins.str instance
    Return a copy of the string with trailing whitespace removed.

    If chars is given and not None, remove characters in chars instead.
```
Example :
```py
>>> a = "    Apple    "
>>> a.rstrip()
'    Apple'
>>>
>>> b = "               TEXT"
>>> b.rstrip()
'               TEXT'
>>>
>>>
>>> c = "### .. abbccc...Apple"
>>> c.lstrip("#, ., a, b, c")
'Apple'
```
---

### 39. split
- The `split()` method splits a string into a list.
- You can specify the separator, default separator is any whitespace.
- Note: When maxsplit is specified, the list will contain the specified number of elements plus one.
- Syntax : `str.split(separator, maxsplit)`
- Parameter Values :
  - ___separator___ (Optional). 
    - Specifies the separator to use when splitting the string.
    - By default any whitespace is a separator
  -  ___maxsplit___ (Optional). 
     -  Specifies how many splits to do.
     -  Default value is -1, which is "all occurrences"
```
help(t.split)
Help on built-in function split:

split(sep=None, maxsplit=-1) method of builtins.str instance
    Return a list of the substrings in the string, using sep as the separator string.

      sep
        The separator used to split the string.

        When set to None (the default value), will split on any whitespace
        character (including \\n \\r \\t \\f and spaces) and will discard
        empty strings from the result.
      maxsplit
        Maximum number of splits (starting from the left).
        -1 (the default value) means no limit.

    Note, str.split() is mainly useful for data that has been intentionally
    delimited.  With natural text that includes punctuation, consider using
    the regular expression module.
```
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

### 41. startswith
- The `startswith()` method returns `True` if the string starts with the specified value, otherwise `False`.
- Syntax : `string.startswith(value, start, end)`
- Parameter Values :
  - ___val___ (Required). 
    - The value to check if the string starts with.
  - ___sta___ (Optional). 
    - An Integer specifying at which position to start the search.
  - ___end___ (Optional). 
    - An Integer specifying at which position to end the search.
```
help(txt.startswith)
Help on built-in function startswith:

startswith(...) method of builtins.str instance
    S.startswith(prefix[, start[, end]]) -> bool

    Return True if S starts with the specified prefix, False otherwise.
    With optional start, test S beginning at that position.
    With optional end, stop comparing S at that position.
    prefix can also be a tuple of strings to try.
```
Example 1 :
```py
>>> txt = "Hello, welcome to my world."
>>> txt.startswith("Hello")
True
>>>
```
Example 2 :
```py
>>> txt = "Hello, welcome to my world."
>>> txt.startswith("wel", 7, 20)
True
>>>
```
---

### 42. strip
- The `strip()` method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
Syntax : `string.strip(characters)`
- Parameter Values :
  - ___characters___ (Optional). 
    - A set of characters to remove as leading/trailing characters.
```
   help(a.strip)
Help on built-in function strip:

strip(chars=None, /) method of builtins.str instance
    Return a copy of the string with leading and trailing whitespace removed.

    If chars is given and not None, remove characters in chars instead.
```
Example :
```py
>>> a = "    Apple    "
>>> a.strip()
'Apple'
>>>
>>> b = "               TEXT"
>>> b.strip()
'TEXT'
>>>
>>> c = "### .. abbccc...Apple"
>>> c.strip("#, ., a, b, c")
'Apple'
>>>
```
---

### 43. swapcase
- The `swapcase()` method returns a string where all the upper case letters are lower case and vice versa.
- Syntax :`string.swapcase()`
```
   help(txt.swapcase)
Help on built-in function swapcase:

swapcase() method of builtins.str instance
    Convert uppercase characters to lowercase and lowercase characters to uppercase.
>>>
```
Example :
```py
>>> txt = " HELLO my NaMe is ABHIshek"
>>> txt.swapcase()
' hello MY nAmE IS abhiSHEK'
>>>
```
---

### 44. title
- The `title()` method returns a string where the first character in every word is upper case. Like a header, or a title.
- If the word contains a number or a symbol, the first letter after that will be converted to upper case.
- Syntax : `string.title()`
```
   help(txt.title)
Help on built-in function title:

title() method of builtins.str instance
    Return a version of the string where each word is titlecased.

    More specifically, words start with uppercased characters and all remaining
    cased characters have lower case.
```
Example1  :
```py
>>> txt = "Welcome to my world"
>>> txt.title()
'Welcome To My World'
>>>
```
Example 2 :
```py
>>> txt = "Welcome to my 2nd world"
>>> txt.title()
'Welcome To My 2Nd World'
>>>
```
Example 3 : 
```py
>>> txt = "hello b2b2b2 and 3g3g3g"
>>> txt.title()
'Hello B2B2B2 And 3G3G3G'
>>>
```
---

### 45. translate (Incomplete)
- The `translate()` method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.
- Use the `maketrans()` method to create a mapping table.
- If a character is not specified in the dictionary/table, the character will not be replaced.
- If you use a dictionary, you must use ascii codes instead of characters.
- Syntax : `string.translate(table)`
- Parameter Values :
  - ___table___	(Required). 
    - Either a dictionary, or a mapping table describing how to perform the replace.
```

```
Example :
```py

```
---

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
---

### 47. zfill
- The `zfill()` method adds zeros (`0`) at the beginning of the string, until it reaches the specified length.
- If the value of the len parameter is less than the length of the string, no filling is done.
- Syntax : `string.zfill(len)`
Parameter Values :
  - ___len___	(Required). 
    - A number specifying the desired length of the string.
```
help(txt.zfill)
Help on built-in function zfill:

zfill(width, /) method of builtins.str instance
    Pad a numeric string with zeros on the left, to fill a field of the given width.

    The string is never truncated.
```
Example :
```py
>>> txt = "ABHI"
>>> txt.zfill(10)
'000000ABHI'
>>>
>>> txt = "44"
>>> txt.zfill(10)
'0000000044'
>>>
>>> txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
>>> txt.zfill(20)
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>>
>>> txt.zfill(30)
'0000ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>>
```
---
