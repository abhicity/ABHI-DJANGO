# ___`[/]` Division Operator___


### Int / Int = Float
```py
>>> a = 50
>>> b = 10
>>> c = a / b
>>> c
5.0
>>> type(a)
<class 'int'>
>>> type(b)
<class 'int'>
>>> type(c)
<class 'float'>
>>>
```
### Float / Float = Float
```py
>>> a = 10.5
>>> b = 5.5
>>> c = a / b
>>> c
1.9090909090909092
>>> type(a)
<class 'float'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'float'>
>>>
```

### Complex / Complex = Complex
```py
>>> a1 = 4 + 6j
>>> a2 = 3 + 7j
>>> a3 = a1 / a2
>>> a3
(0.9310344827586208-0.17241379310344832j)
>>> type(a1)
<class 'complex'>
>>> type(a2)
<class 'complex'>
>>> type(a3)
<class 'complex'>
>>>
```

### String / String =  unsupported operand
```py
>>> inst = "Skill Disk"
>>> place = "Bengaluru"
>>> inst / place
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> type(inst)
<class 'str'>
>>> type(place)
<class 'str'>
>>>
```

### Bool / Bool = division by zero
```py
>>> a = True
>>> b = False
>>> c = a / b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'bool'>
>>>
```

### None Type
```py
>>> n1 = None
>>> n2 = None
>>> n3 = n1 / n2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'NoneType' and 'NoneType'
>>> type(n1)
<class 'NoneType'>
>>> type(n2)
<class 'NoneType'>
>>>
```
---



### Int / Float = Float
```py
>>> a = 8
>>> b = 5.5
>>> c = a / b
>>> c
1.4545454545454546
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'float'>
>>>
```

### Int / Complex = Complex
```py
>>> c1 = 3
>>> c2 = 3 + 2j
>>> c3 = c1 / c2
>>> c3
(0.6923076923076924-0.46153846153846156j)
>>> type(c1)
<class 'int'>
>>> type(c2)
<class 'complex'>
>>> type(c3)
<class 'complex'>
>>>
```

### Int / String = unsupported operand
```py
>>> a = 40
>>> b = "Fourty"
>>> c = a / b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'int' and 'str'
>>> type(a)
<class 'int'>
>>> type(b)
<class 'str'>
>>>
```

### Int / Bool = Float
```py
>>> a = 7
>>> b = True
>>> c = a / b
>>> c
7.0
>>> type(a)
<class 'int'>
>>> type(b)
<class 'bool'>
>>> type(c)
<class 'float'>
>>>
>>>
>>> a = 7
>>> b = False
>>> c = a / b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
```
### Int / None = unsupported operand
```py
>>> a = 30
>>> b = None
>>> c = a / b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'int' and 'NoneType'
>>> type(a)
<class 'int'>
>>> type(b)
<class 'NoneType'>
>>>
```
---


### Float / Complex = Complex
```py
>>> a = 5.5
>>> b = 2 + 4j
>>> c = a / b
>>> c
(0.55-1.1j)
>>> type(a)
<class 'float'>
>>> type(b)
<class 'complex'>
>>> type(c)
<class 'complex'>
>>>
```

### Float / String = unsupported operand
```py
>>> a = 10.5
>>> b = "ZING"
>>> c = a / b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'float' and 'str'
>>> type(a)
<class 'float'>
>>> type(b)
<class 'str'>
>>>
```

### Float / Bool = Float
```py
>>> a = 4.5
>>> b = True
>>> c = a / b
>>> c
4.5
>>> type(a)
<class 'float'>
>>> type(b)
<class 'bool'>
>>> type(c)
<class 'float'>
>>>
>>>
>>> a = 4.5
>>> b = False
>>> c = a / b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: float division by zero
>>>
```

### Float / None = unsupported operand
```py
>>> a = 8.5
>>> b = None
>>> c = a / b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'float' and 'NoneType'
>>> type(a)
<class 'float'>
>>> type(b)
<class 'NoneType'>
>>>
```
---

### Complex / String = unsupported operand
```py
>>> a = 20 + 4j
>>> b = "BMW"
>>> c = a / b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'complex' and 'str'
>>> type(a)
<class 'complex'>
>>> type(b)
<class 'str'>
>>>
```

### Complex / Boolean = Complex
```py

>>> a = 30 + 44j
>>> b = True
>>> c = a / b
>>> c
(30+44j)
>>> type(a)
<class 'complex'>
>>> type(b)
<class 'bool'>
>>> type(c)
<class 'complex'>
>>>
>>>
>>> a = 30 + 44j
>>> b = False
>>> c = a / b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: complex division by zero
>>>
```

### Complex / None = unsupported operand
```py
>>> a = 40 + 50j
>>> b = None
>>> c = a / b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'complex' and 'NoneType'
>>> type(a)
<class 'complex'>
>>> type(b)
<class 'NoneType'>
>>>
```
---

### String / Boolean = unsupported operand
```py
>>> a = "Name"
>>> b = True
>>> c = a / b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'bool'
>>>
>>>
>>> a = "Age"
>>> b = False
>>> c = a / b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'bool'
>>> type(a)
<class 'str'>
>>> type(b)
<class 'bool'>
>>>
```

### String / None = unsupported operand
```py
>>> a = "Rahul"
>>> b = None
>>> c = a / b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'NoneType'
>>> type(a)
<class 'str'>
>>> type(b)
<class 'NoneType'>
>>>
```
---

### Boolean / None = unsupported operand
```py
>>> a = True
>>> b = None
>>> c = a / b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'bool' and 'NoneType'
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'NoneType'>
>>>
>>>
>>> a = False
>>> b = None
>>> c = a / b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'bool' and 'NoneType'
>>>
```