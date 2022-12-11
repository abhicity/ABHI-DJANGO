# Operators

### Bool


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
### Bool + Float
```py
# Bool + Float = Float
>>> a = True
>>> b = 10.5
>>> c = a + b
>>> c
11.5
>>> type (a)
<class 'bool'>
>>> type (b)
<class 'float'>
>>> type (c)
<class 'float'>
>>>
>>>
>>> x = False
>>> y = 20.5
>>> z = x + y
>>> z
20.5
>>> type(x)
<class 'bool'>
>>> type(y)
<class 'float'>
>>> type(z)
<class 'float'>
>>>
```
---

### Bool + Complex
```py
# Bool + Complex = Complex
>>> a1 = True
>>> a2 = 5 + 5j
>>> a3 = a1 + a2
>>> a3
(6+5j)
>>> type (a1)
<class 'bool'>
>>> type (a2)
<class 'complex'>
>>> type (a3)
<class 'complex'>
>>>
>>>
>>> b1 = False
>>> b2 = 5 + 5j
>>> b3 = b1 + b2
>>> b3
(5+5j)
>>> type (b1)
<class 'bool'>
>>> type (b2)
<class 'complex'>
>>> type (b3)
<class 'complex'>
>>>
```
---

### Bool + String
```py
# Bool + String
>>> s1 = True
>>> type(s1)
<class 'bool'>
>>> s2 = "5"
>>> type(s2)
<class 'str'>
>>> s3 = s1 + s2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'bool' and 'str'
>>>
>>>
>>> w1 = False
>>> w2 = "4"
>>> w1 + w2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'bool' and 'str'
>>>
```
---

### String + None
```py
#String + None
>>> n1 = True
>>> n2 = None
>>> n3 = n1 + n2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'bool' and 'NoneType'
>>>
```
---

## `-` Operator
```py
>>> q = 10
>>> w = 5
>>> e = q - w
>>> e
5>>> type(q)
<class 'int'>
>>> type(w)
<class 'int'>
>>> type(e)
<class 'int'>
>>>
>>>
```
---