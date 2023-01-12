[TOC]

# String Table.

| Sl No | Methods      | Parameter | Defeat | Syntax                        | Description                                                                                   |
| :---: | ------------ | :-------: | :----: | ----------------------------- | --------------------------------------------------------------------------------------------- |
|  1.   | capitalize   |     -     |   -    | str.capitalize()              | It Converts only the first character to upper case                                            |
|  2.   | casefold     |     -     |   -    | str.casefold()                | Converts string into lower case                                                               |
|  3.   | center       |   width   |   -    | str.center(length, character) | Returns a centered string                                                                     |
|       | fillchar     |  'space'  |        |                               |                                                                                               |
|  4.   | count        |           |        | str.count(value, start, end)  | Returns the number of times a specified value occurs in a string                              |
|  5.   | encode       |           |        | str.encode()                  | Returns an encoded version of the string                                                      |
|  6.   | endswith     |           |        | str.endswith()                | Returns true if the string ends with the specified value                                      |
|  7.   | expandtabs   |           |        | str.expandtabs()              | Sets the tab size of the string                                                               |
|  8.   | find         |           |        | str.find(value, start, end)   | Searches the string for a specified value and returns the position of where it was found      |
|  9.   | format       |           |        | str.format()                  | Formats specified values in a string                                                          |
|  10.  | format_map   |           |        | str.format_map()              | Formats specified values in a string                                                          |
|  11.  | index        |           |        | str.index()                   | Searches the string for a specified value and returns the position of where it was found      |
|  12.  | isalnum      |           |        | str.isalnum()                 | Returns True if all characters in the string are alphanumeric                                 |
|  13.  | isalpha      |           |        | str.isalpha())                | Returns True if all characters in the string are in the alphabet                              |
|  14.  | isascii      |           |        | str.isascii()                 | Returns True if all characters in the string are ascii characters                             |
|  15.  | isdecimal    |           |        | str.isdecimal()               | Returns True if all characters in the string are decimals                                     |
|  16.  | isdigit      |           |        | str.isdigit()                 | Returns True if all characters in the string are digits                                       |
|  17.  | isidentifier |     -     |   -    | str.isidentifier()            | Returns True if the string is an identifier                                                   |
|  18.  | islower      |           |        | str.islower()                 | Returns True if all characters in the string are lower case                                   |
|  19.  | isnumeric    |     -     |   -    | str.isnumeric()               | Returns True if all characters in the string are numeric                                      |
|  20.  | isprintable  |           |        | str.isprintable()             | Returns True if all characters in the string are printable                                    |
|  21.  | isspace      |           |        | str.isspace()                 | Returns True if all characters in the string are whitespaces                                  |
|  22.  | istitle      |           |        | str.istitle()                 | Returns True if the string follows the rules of a title                                       |
|  23.  | isupper      |           |        | str.isupper()                 | Returns True if all characters in the string are upper case                                   |
|  24.  | join         |           |        | str.join()                    | Converts the elements of an iterable into a string                                            |
|  25.  | ljust        |           |        | str.ljust()                   | Returns a left justified version of the string                                                |
|  26.  | lower        |           |        | str.lower()                   | Converts a string into lower case                                                             |
|  27.  | lstrip       |           |        | str.lstrip()                  | Returns a left trim version of the string                                                     |
|  28.  | maketrans    |           |        | str.maketrans()               | Returns a translation table to be used in translations                                        |
|  29.  | partition    |           |        | str.partition()               | Returns a tuple where the string is parted into three parts                                   |
|  30.  | removeprefix |           |        | str.removeprefix()            | -                                                                                             |
|  31.  | removesuffix |           |        | str.removesuffix()            | -                                                                                             |
|  32.  | replace      |           |        | str.replace()                 | Returns a string where a specified value is replaced with a specified value                   |
|  33.  | rfind        |           |        | str.rfind()                   | Searches the string for a specified value and returns the last position of where it was found |
|  34.  | rindex       |           |        | str.rindex()                  | Searches the string for a specified value and returns the last position of where it was found |
|  35.  | rjust        |           |        | str.rjust()                   | Returns a right justified version of the string                                               |
|  36.  | rpartition   |           |        | str.rpartition()              | Returns a tuple where the string is parted into three parts                                   |
|  37.  | rsplit       |           |        | str.rsplit()                  | Splits the string at the specified separator, and returns a list                              |
|  38.  | rstrip       |           |        | str.rstrip()                  | Returns a right trim version of the string                                                    |
|  39.  | split        |           |        | str.split()                   | Splits the string at the specified separator, and returns a list                              |
|  40.  | splitlines   |           |        | str.splitlines()              | Splits the string at line breaks and returns a list                                           |
|  41.  | startswith   |           |        | str.startswith()              | Returns true if the string starts with the specified value                                    |
|  42.  | strip        |           |        | str.strip()                   | Returns a trimmed version of the string                                                       |
|  43.  | swapcase     |           |        | str.swapcase()                | Swaps cases, lower case becomes upper case and vice versa                                     |
|  44.  | title        |           |        | str.title()                   | Converts the first character of each word to upper case                                       |
|  45.  | translate    |           |        | str.translate()               | Returns a translated string                                                                   |
|  46.  | upper        |     -     |   -    | str.upper()                   | Converts a string into upper case                                                             |
|  47.  | zfill        |           |        | str.zfill()                   | Fills the string with a specified number of 0 values at the beginning                         |

------

### Difference Between.

































---
---
---
---
---
---
---

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
| 1     | ljust   |        |        |
| 2     | lstrip  |        |        |



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

| Sl No | Methods | Origin | Defeat | Description                                      |
| ----- | ------- | ------ | ------ | ------------------------------------------------ |
| 1     | ljust   |        |        | Returns a left justified version of the string.  |
| 2     | rjust   |        |        | Returns a right justified version of the string. |
| 3     | strip   |        |        |                                                  |
| 4     | lstrip  |        |        |                                                  |
| 5     | rstrip  |        |        |                                                  |


---
---
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'

---
---