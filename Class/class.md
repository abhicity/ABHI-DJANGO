[TOC]

# Doughts

#### 03-01-23-tue
- [x] Post
  - push messages from form.
  -  Ref Link : https://formspree.io/f/mayadege

---

- [ ] importing in CSS.
  -  @ 

---

- [ ] Dictionary Methods
  - fromkeys()

---

- [ ] String Methods.
  - string.expandtabs()
  - string.format_map()
  - string.join()
  - string.maketrans()
  - string.translate()
  - string.removeprefix()
  - string.removesuffix()
```py
# string.join() 
>>> names = "Abhi", "Chandhu", "Rahul"
>>> names.join()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'join'
>>>
>>> names.join(#)
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
```py
#string.maketrans()
>>> txt = "Hi... My name is Abhi!"
TypeError: if you give only one argument to maketrans it must be a dict
>>> op = txt.maketrans("A", "P")
>>> op
{65: 80}
```
- 
---