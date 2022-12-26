### String

# 2. Write a function called rotate_word that takes a string and an integer as parameters,
# and that function should return a new string containing the letters from the original 
#string “rotated” by the given amount. For example, “cheer” rotated by 7 is “jolly” and “melon” 
#rotated by −10 is “cubed”.

#EG:
#cheer => ROTATED 7 TIMES => jolly

#c ==> rotate by 7 ==> j
#h ==> rotate by 7 ==> o
#o ==> rotate by 7 ==> l

#count letters from c to j it is 7
#count letters from h to o it is 7


string = input("Enter a string : ")
number = int(input("Enter the rotate number : "))
result = ""
for i in string:
    i = chr(ord(i)+number)
    result += i
print("rotated_word :",result)
