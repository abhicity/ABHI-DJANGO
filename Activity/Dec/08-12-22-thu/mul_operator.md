# ___`[*]` Multiplicaton Operator___


### Int * Int = Int
```py
>>> a = 2
>>> b = 5
>>> c = a * b
>>> c
10
>>> type(a)
<class 'int'>
>>> type(b)
<class 'int'>
>>> type(c)
<class 'int'>
>>>
```
### Float * Float = Float
```py
>>> a = 5.5
>>> b = 4.5
>>> c = a * b
>>> c
24.75
>>> type(a)
<class 'float'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'float'>
>>>

```

### Complex * Complex = Complex
```py
>>> a1 = 4 + 6j
>>> a2 = 3 + 7j
>>> a3 = a1 * a2
>>> a3
(-30+46j)
>>>
>>> type(a1)
<class 'complex'>
>>> type(a2)
<class 'complex'>
>>> type(a3)
<class 'complex'>
>>>
```

### String * String =  can't multiply
```py
>>> inst = "Skill disk"
>>> place = "Bengaluru"
>>> form = inst * place
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>> type(inst)
<class 'str'>
>>> type(place)
<class 'str'>
>>>

```

### Bool * Bool = Int
```py
>>> a = True
>>> b = False
>>> c = a * b
>>> c
0
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'bool'>
>>> type(c)
<class 'int'>
>>>
```

### None Type
```py
>>> n1 = None
>>> n2 = None
>>> n3 = n1 * n2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'
>>> type(n1)
<class 'NoneType'>
>>> type(n2)
<class 'NoneType'>
>>>
```
---



### Int * Float = Float
```py
>>> a = 8
>>> b = 5.5
>>> c = a * b
>>> c
44.0
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'float'>
>>>
```

### Int * Complex = Complex
```py
>>> c1 = 3
>>> c2 = 3 + 2j
>>> c3 = c1 * c2
>>> c3
(9+6j)
>>> type(c1)
<class 'int'>
>>> type(c2)
<class 'complex'>
>>> type(c3)
<class 'complex'>
>>>
```

### Int * String = String
```py
>>> a = 55
>>> b = "Fifty Five"
>>> c = a * b
>>> c
'Fifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty FiveFifty Five'
>>> type(a)
<class 'int'>
>>> type(b)
<class 'str'>
>>> type(c)
<class 'str'>
>>>

```

### Int * Bool = Int
```py
>>> a = 7
>>> b = True
>>> c = a * b
>>> c
7
>>> type(a)
<class 'int'>
>>> type(b)
<class 'bool'>
>>> type(c)
<class 'int'>
>>>
>>> a = 7
>>> b = False
>>> c = a * b
>>> c
0
```
### Int * None = unsupported operand
```py
>>> a = 30
>>> b = None
>>> c = a * b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
>>> type(a)
<class 'int'>
>>> type(b)
<class 'NoneType'>
>>>

```
---


### Float * Complex = Complex
```py
>>> a = 5.5
>>> b = 2 + 4j
>>> c = a * b
>>> c
(11+22j)
>>> type(a)
<class 'float'>
>>> type(b)
<class 'complex'>
>>> type(c)
<class 'complex'>
>>>
```

### Float * String = can't multiply
```py
>>> a = 10.5
>>> b = "Bengaluru"
>>> c = a * b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'
>>> type(a)
<class 'float'>
>>> type(b)
<class 'str'>
>>>
```

### Float * Bool = Float
```py
>>> a = 4.5
>>> b = True
>>> c = a * b
>>> c
4.5
>>> type(a)
<class 'float'>
>>> type(b)
<class 'bool'>
>>> type(c)
<class 'float'>
>>>
>>> a = 4.5
>>> b = False
>>> c = a * b
>>> c
0.0
>>>
```

### Float * None = unsupported operand
```py
>>> a = 8.5
>>> b = None
>>> c = a * b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for *: 'float' and 'NoneType'
>>> type(a)
<class 'float'>
>>> type(b)
<class 'NoneType'>
>>>
```
---

### Complex * String = unsupported operand
```py
>>> a = 20 + 4j
>>> b = "Ponds Powder"
>>> c = a * b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'complex'
>>> type(a)
<class 'complex'>
>>> type(b)
<class 'str'>
>>>
```

### Complex * Boolean = Complex
```py
>>> a = 30 +44j
>>> b = True
>>> c = a * b
>>> c
(30+44j)
>>> type(a)
<class 'complex'>
>>> type(b)
<class 'bool'>
>>> type(c)
<class 'complex'>
>>>
>>> a = 30 +44j
>>> b = False
>>> c = a * b
>>> c
0j
>>>

```

### Complex * None = unsupported operand
```py
>>> a = 40 + 50j
>>> b = None
>>> c = a * b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for *: 'complex' and 'NoneType'
>>> type(a)
<class 'complex'>
>>> type(b)
<class 'NoneType'>
>>>
```
---

### String * Boolean = String
```py
>>> a = "Abhi"
>>> b = True
>>> c = a * b
>>> c
'Abhi'
>>> type(a)
<class 'str'>
>>> type(b)
<class 'bool'>
>>> type(c)
<class 'str'>
>>>
>>> a = "Abhi"
>>> b = False
>>> c = a * b
>>> c
''
>>>
```

### String * None = can't multiply
```py
>>> a = "Abhi"
>>> b = None
>>> c = a * b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'NoneType'
>>> type(a)
<class 'str'>
>>> type(b)
<class 'NoneType'>
>>>
```
---

### Boolean * None = unsupported operand
```py
>>> a = True
>>> b = None
>>> c = a * b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for *: 'bool' and 'NoneType'
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'NoneType'>
>>>
>>> a = False
>>> b = None
>>> c = a * b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for *: 'bool' and 'NoneType'
>>>
```