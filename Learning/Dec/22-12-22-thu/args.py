

#def addition, args(a, b, *args):
 #   print(f"args = {args}")
  #  print(f"{a} + {b} = {a+b}")

#result = addition(1, 2) + args()
#addition(2, 4, 5 ,1)

###

#def addition(*args):
 #   print(f"args = {args}")
  #  print(f"{args} + {args} = {args}")
   # return sum(args)

#result = addition(1, 2) + args()
#addition(2, 4, 5 ,1)

###

#def addition(*args):
 #   total = 0
#
 #   for i in addition:
   #     total += addition
  #      print(i)

#addition(1, 2, 3, 4, 5)
#addition(1, 2, 3, 4)
#addition(1, 2, 3)
#ddition(1, 2,)

###

#def addition(*args):
 #  result = 0
  # for i in args:
   #   result += i
   #return result


#print(addition())
#print(addition(1, 2))
#print(addition(1, 2, 3))
#print(addition(1, 2, 3, 4))
#print(addition(1, 2, 3, 4, 5))

###

def addition(a, b, *args):
   result = a + b
   print(f"{a} + {b} ",end="")
   for i in args:
      result += i
      print(f"+ {i} ",end="")
   print(f" = {result}")

addition(1, 2)
addition(1, 2, 3)
addition(1, 2, 3, 4)
addition(1, 2, 3, 4, 5)


