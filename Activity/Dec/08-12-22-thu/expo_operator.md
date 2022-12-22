# ___`[**]` Exponential Operator___


### Int ** Int = Int
```py
>>> a = 2
>>> b = 5
>>> c = a ** b
>>> c
32
>>> type(a)
<class 'int'>
>>> type(b)
<class 'int'>
>>> type(c)
<class 'int'>
>>>
```
### Float ** Float = Float
```py
>>> a = 5.5
>>> b = 4.5
>>> c = a ** b
>>> c
2146.0117856117135
>>> type(a)
<class 'float'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'float'>
>>>
```

### Complex ** Complex = Complex
```py
>>> a1 = 4 + 6j
>>> a2 = 3 + 7j
>>> a3 = a1 ** a2
>>> a3
(-0.18526233055316088-0.33829547052605513j)
>>> type(a1)
<class 'complex'>
>>> type(a2)
<class 'complex'>
>>> type(a3)
<class 'complex'>
>>>
```

### String ** String = Unsupported operand
```py
>>> inst = "Skill Disk"
>>> place = "Bengaluru"
>>> inst ** place
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'
>>> type(inst)
<class 'str'>
>>> type(place)
<class 'str'>
>>>
```

### Bool ** Bool = Int
```py
>>> a = True
>>> b = False
>>> c = a ** b
>>> c
1
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'bool'>
>>> type(c)
<class 'int'>
>>>
```

### None ** None = unsupported operand
```py
>>> n1 = None
>>> n2 =None
>>> n1 ** n2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ** or pow(): 'NoneType' and 'NoneType'
>>>
>>> type(n1)
<class 'NoneType'>
>>> type(n2)
<class 'NoneType'>
>>>
```
---


### Int ** Float = Float
```py
>>> a = 4
>>> b = 2.2
>>> c = a ** b
>>> c
21.112126572366314
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'float'>
>>>
```

### Int ** Complex = Complex
```py
>>> c1 = 3
>>> c2 = 3 + 2j
>>> c3 = c1 ** c2
>>> c3
(-15.828883225866512+21.873418933076778j)
>>> type(c1)
<class 'int'>
>>> type(c2)
<class 'complex'>
>>> type(c3)
<class 'complex'>
>>>
```

### Int ** String = Unsupported operand
```py
>>> a = 20
>>> b = "Twenty"
>>> c = a ** b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'str'
>>> type(a)
<class 'int'>
>>> type(b)
<class 'str'>
>>>
```

### Int ** Bool = Int
```py
>>> a = 7
>>> b = True
>>> c = a ** b
>>> c
7
>>> type(a)
<class 'int'>
>>> type(b)
<class 'bool'>
>>> type(c)
<class 'int'>
>>>
>>>
>>> a = 7
>>> b = False
>>> c = a ** b
>>> c
1
```

### Int ** None = Unsupported operand
```py
>>> a = 30
>>> b = None
>>> c = a ** b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'NoneType'
>>> type(a)
<class 'int'>
>>> type(b)
<class 'NoneType'>
>>>
```
---


### Float ** Complex = Complex
```py
>>> a = 5.5
>>> b = 2 + 4j
>>> c = a ** b
>>> c
(26.010670497130917+15.443688687929557j)
>>> type(a)
<class 'float'>
>>> type(b)
<class 'complex'>
>>> type(c)
<class 'complex'>
>>>
```

### Float ** String = unsupported operand
```py
>>> a = 10.5
>>> b = "Bengaluru"
>>> c = a ** b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ** or pow(): 'float' and 'str'
>>> type(a)
<class 'float'>
>>> type(b)
<class 'str'>
>>>
```

### Float ** Bool = Float
```py
>>> a = 4.5
>>> b = True
>>> c = a ** b
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
>>> c = a ** b
>>> c
1.0
>>>
```

### Float ** None = unsupported operand
```py
>>> a = 8.5
>>> b = None
>>> c = a ** b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ** or pow(): 'float' and 'NoneType'
>>> type(a)
<class 'float'>
>>> type(b)
<class 'NoneType'>
>>>
```
---

### Complex ** String = unsupported operand
```py
>>> a = 20 + 4j
>>> b = "Fair and Lovely"
>>> c = a ** b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ** or pow(): 'complex' and 'str'
>>> type(a)
<class 'complex'>
>>> type(b)
<class 'str'>
>>>
```

### Complex ** Boolean = Complex
```py
>>> a = 30 + 44j
>>> b = True
>>> c = a ** b
>>> c
(30+44j)
>>>
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
>>> c = a ** b
>>> c
(1+0j)
>>>
```

### Complex ** None = unsupported operand
```py
>>> a = 40 + 50j
>>> b = None
>>> c = a ** b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ** or pow(): 'complex' and 'NoneType'
>>> type(a)
<class 'complex'>
>>> type(b)
<class 'NoneType'>
>>>
```
---

### String ** Boolean = unsupported operand
```py
>>> a = "Abhi"
>>> b = True
>>> c = a ** b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'bool'
>>> type(a)
<class 'str'>
>>> type(b)
<class 'bool'>
>>>
>>> a = "Abhi"
>>> b = False
>>> c = a ** b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'bool'
>>>
```

### String ** None = unsupported operand
```py
>>> a = "Abhi"
>>> b = None
>>> c = a ** b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'NoneType'
>>> type(a)
<class 'str'>
>>> type(b)
<class 'NoneType'>
>>>
```
---

### Boolean ** None = unsupported operand
```py
>>> a = True
>>> b = None
>>> c = a ** b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ** or pow(): 'bool' and 'NoneType'
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'NoneType'>
>>>
>>> a = False
>>> b = None
>>> c = a ** b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ** or pow(): 'bool' and 'NoneType'
>>>
```