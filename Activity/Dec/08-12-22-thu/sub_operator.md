# [-] Subtraction Operators














# Operators
### Int + Int = Int
```py
>>> a = 8
>>> b = 2
>>>
>>> c = a + b
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
### Float + Float = Float
```py
>>> a = 2.5
>>> b = 2.5
>>> c = a + b
>>> c
5.0
>>> type(a)
<class 'float'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'float'>
>>>
```

### Complex + Complex = Complex
```py
>>> a = 5 + 2j
>>> a1 = 5 + 2j
>>> a2 = 2 + 5j
>>> a3 = a1 + a2
>>> a3
(7+7j)
>>>
>>> a1 = 5 + 4j
>>> a2 = 2 + 5j
>>> a3 = a1 + a2
>>> a3
(7+9j)
>>> type(a1)
<class 'complex'>
>>> type(a2)
<class 'complex'>
>>> type(a3)
<class 'complex'>
>>>
```

### String + String = String
```py
>>> inst = "Skill Disk"
>>> place = "Bengaluru"
>>> form = inst + place
>>> form
'Skill DiskBengaluru'
>>> type(inst)
<class 'str'>
>>> type(place)
<class 'str'>
>>> type(form)
<class 'str'>
>>>
```

### Bool + Bool = Int
```py
# Bool + Bool = int
>>> b = True
>>> c = False
>>>
>>> d = b + c
>>> d
1
>>>
>>> type (b)
<class 'bool'>
>>> type (c)
<class 'bool'>
>>>
>>> type (d)
<class 'int'>
>>>
```

### None Type
```py
>>> n1 = None
>>> n2 = None
>>> n3 = n1 + n2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
>>>
>>> type(n1)
<class 'NoneType'>
>>> type(n2)
<class 'NoneType'>
>>>
```
---



### Int + Float = Float
```py
>>> a = 10
>>> b = 3.3
>>> c = a + b
>>> c
13.3
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'float'>
>>>
```

### Int + Complex = Complex
```py
>>> s1 = 5
>>> s2 = 8 + 2j
>>> s3 = s1 + s2
>>> s3
(13+2j)
>>> type(s1)
<class 'int'>
>>> type(s2)
<class 'complex'>
>>> type(s3)
<class 'complex'>
>>>
```

### Int + String = unsupported operand
```py
>>> a = 8
>>> b = "abhi"
>>> c = a + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

### Int + Bool = Int
```py
>>> a = 5
>>> b = True
>>> c = a + b
>>> c
6
>>> type(a)
<class 'int'>
>>> type(b)
<class 'bool'>
>>> type(c)
<class 'int'>
>>>
```
### Int + None = unsupported operand
```py
>>> a = 2
>>> b = None
>>> c = a + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
>>> type(a)
<class 'int'>
>>> type(b)
<class 'NoneType'>
>>>
```
---


### Float + Complex = Complex
```py
>>> a = 5.5
>>> b = 2 + 4j
>>> c = a + b
>>> c
(7.5+4j)
>>> type(a)
<class 'float'>
>>> type(b)
<class 'complex'>
>>> type(c)
<class 'complex'>
>>>
```

### Float + String = unsupported operand
```py
>>> a = 10.5
>>> b = "abhi"
>>> c = a + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'float' and 'str'
>>> type(a)
<class 'float'>
>>> type(b)
<class 'str'>
```

### Float + Bool = Float
```py
>>> q = 2.2
>>> w = True
>>> e = q + w
>>> e
3.2
>>> type(q)
<class 'float'>
>>> type(w)
<class 'bool'>
>>> type(e)
<class 'float'>
>>>
```

### Float + None = unsupported operand
```py
>>> a = 3.3
>>> b = None
>>> c = a + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'float' and 'NoneType'
>>> type(a)
<class 'float'>
>>> type(b)
<class 'NoneType'>
>>>
```

### Complex + String = unsupported operand
```py
>>> a = 5+5j
>>> b = "abhi"
>>> c = a + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'complex' and 'str'
>>> type(a)
<class 'complex'>
>>> type(b)
<class 'str'>
>>>
```

### Complex + Boolean = Complex
```py
>>> a = 2+4j
>>> b = True
>>> c = a + b
>>> c
(3+4j)
>>> type(a)
<class 'complex'>
>>> type(b)
<class 'bool'>
>>> type(c)
<class 'complex'>
>>>
>>>
>>> x =2+4j
>>> y = False
>>> z = x + y
>>> z
(2+4j)
```

### Complex + None = unsupported operand
```py
>>> a = 5+5j
>>> b = None
>>> c = a + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'complex' and 'NoneType'
>>> type(a)
<class 'complex'>
>>> type(b)
<class 'NoneType'>
>>>
```

### String + Boolean = unsupported operand
```py
>>> a = "abhi"
>>> b = True
>>> c = a + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "bool") to str
>>> type(a)
<class 'str'>
>>> type(b)
<class 'bool'>
>>>
```

### String + None = unsupported operand
```py
>>> a = "abhi"
>>> b = None
>>> c = a + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "NoneType") to str
>>> type(a)
<class 'str'>
>>> type(b)
<class 'NoneType'>
>>>
```

### Boolean + None = unsupported operand
```py
>>> a = True
>>> b = None
>>> c = a + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'bool' and 'NoneType'
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'NoneType'>
>>>
>>>
>>> a = False
>>> b = None
>>> c = a + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'bool' and 'NoneType'
>>>
>>>
```
---