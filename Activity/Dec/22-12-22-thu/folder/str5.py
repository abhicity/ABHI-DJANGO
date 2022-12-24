### String

#5.  Write a program that accepts a string from the user and display the same string after removing vowels from it.

#vowels = a, e, i, o, u.

#def string():
    #a = str (input("Enter a String : "))
    #vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    #return a.replace(a, e, i, o, u)
    #return a.replace(a, "q")


#result = string()
#print("After removing vowels :", result)
#print(result)


text = input("Enter String: ")

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for c in text:
    if c in vowels:
        text = text.replace(c, "")

print("Without Vowels =", text)