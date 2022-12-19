# ___`[-]` Subtraction Operator___

### Int - Int = Int
```py
>>> x = 10
>>> y = 5
>>> z = x - y
>>> z
5
>>> type(x)
<class 'int'>
>>> type(y)
<class 'int'>
>>> type(z)
<class 'int'>
>>>
```

### Float - Float = Float
```py
>>> a = 4.5
>>> b = 2.5
>>> c = a - b
>>> c
2.0
>>> type(a)
<class 'float'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'float'>
>>>
```

### Complex - Complex = Complex
```py
>>> a1 = 8 + 2j
>>> a2 = 10 + 5j
>>> a3 = a1 - a2
>>> a3
(-2-3j)
>>> type(a1)
<class 'complex'>
>>> type(a2)
<class 'complex'>
>>> type(a3)
<class 'complex'>
>>>
```

### String - String = String
```py
>>> inst = "Skill Disk"
>>> address = "Rajaji Nagar"
>>> form = inst - address
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>>
```

### Bool - Bool = Int
```py
>>> a = True
>>> b = False
>>> c = a - b
>>> c
1
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'bool'>
>>> type(c)
<class 'int'>
>>>
>>>
>>> x = False
>>> y = True
>>> z = x - y
>>> z
-1
>>>
```

### None Type
```py
>>> n1 = None
>>> n2 = None
>>> n3 = n1 - n2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'NoneType' and 'NoneType'
>>> type(n3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n3' is not defined. Did you mean: 'a3'?
>>>
```
---

### Int - Float = Float
```py
>>> a = 7
>>> b = 5.5
>>> c = a - b
>>> c
1.5
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'float'>
>>>
```

### Int - Complex = Complex
```py
>>> d = 5
>>> e = 2 + 6j
>>> f = d - e
>>> f
(3-6j)
>>> type(d)
<class 'int'>
>>> type(e)
<class 'complex'>
>>> type(f)
<class 'complex'>
>>>
```

### Int - String = unsupported operand
```py
>>> a = 20
>>> b = "Twenty"
>>> c = a + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

### Int - Bool = Int
```py
>>> a = 8
>>> b = True
>>> c = a - b
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
>>> a = 4
>>> b = False
>>> c = a - b
>>> c
4
>>>
```

### Int - None = unsupported operand
```py
>>> a = 9
>>> b = None
>>> c = a - b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'int' and 'NoneType'
>>> type(a)
<class 'int'>
>>> type(b)
<class 'NoneType'>
```
---

### Float - Complex = Complex
```py
>>> a = 4.4
>>> b = 3 + 5j
>>> c = a - b
>>> c
(1.4000000000000004-5j)
>>>
>>> a = 5.5
>>> b = 2 + 5j
>>> c = a - b
>>> c
(3.5-5j)
>>> type(a)
<class 'float'>
>>> type(b)
<class 'complex'>
>>> type(c)
<class 'complex'>
>>>
```

### Float - String = unsupported operand
```py
>>> a = 5.5
>>> b = "Five"
>>> c = a - b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'float' and 'str'
>>> type(a)
<class 'float'>
>>> type(b)
<class 'str'>
>>>
```

### Float - Bool = Float
```py
>>> a = 5.5
>>> b = True
>>> c = a - b
>>> c
4.5
>>> type(a)
<class 'float'>
>>> type(b)
<class 'bool'>
>>> type(c)
<class 'float'>
>>>
>>> a = 4.4
>>> b = False
>>> c = a - b
>>> c
4.4
>>>
```

### Float - None = unsupported operand
```py
>>> a = 10.5
>>> b = None
>>> c = a - b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'float' and 'NoneType'
>>> type(a)
<class 'float'>
>>> type(b)
<class 'NoneType'>
>>>
```
---

### Complex - String = unsupported operand
```py
>>> a = 3 + 4j
>>> b = "abhi"
>>> c = a - b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'complex' and 'str'
>>> type(a)
<class 'complex'>
>>> type(b)
<class 'str'>
>>>
```

### Complex - Boolean = Complex
```py
>>> a = 6 + 5j
>>> b = True
>>> c = a - b
>>> c
(5+5j)
>>> type(a)
<class 'complex'>
>>> type(b)
<class 'bool'>
>>> type(c)
<class 'complex'>
>>>
>>>
>>> a = 6 + 5j
>>> b = False
>>> c = a - b
>>> c
(6+5j)
>>>
```

### Complex - None = unsupported operand
```py
>>> a = 10 + 5j
>>> b = None
>>> c = a - b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'complex' and 'NoneType'
>>> type(a)
<class 'complex'>
>>> type(b)
<class 'NoneType'>
>>>
```
---

### String - Boolean = unsupported operand
```py
>>> a ="abhi"
>>> b = True
>>> c = a - b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'bool'
>>> type(a)
<class 'str'>
>>> type(b)
<class 'bool'>
>>>
```

### String - None = unsupported operand
```py
>>> a = "abhi"
>>> b = None
>>> c = a - b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'NoneType'
>>> type(a)
<class 'str'>
>>> type(b)
<class 'NoneType'>
>>>
```
---

### Boolean - None = unsupported operand
```py
>>> a = True
>>> b = None
>>> c = a - b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'bool' and 'NoneType'
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'NoneType'>
>>>
```
---