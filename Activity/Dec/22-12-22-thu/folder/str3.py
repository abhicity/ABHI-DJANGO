### String

#3.  Ask the user for a string, and then for a number. Print out that string, that many times. 
#(For example, if the string is Python and the number is 3 you should print out PythonPythonPython.)



def multiplication():
    a = str (input ("Enter a string : "))
    b = int (input("Enter the number : "))
    return a * b

result = multiplication()
print(result)


#OP
#Enter a string : Python
#Enter the number : 3
#PythonPythonPython