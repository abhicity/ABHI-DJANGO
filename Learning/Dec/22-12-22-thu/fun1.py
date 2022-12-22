
a = 8
print(f"value of a = {a} before executing the function.")


def addition():
    print ("Addition function")
    a = float(input("Enter the value of a :"))
    b = float(input("Enter the value of b :"))
    print(f"value of a = {a} inside the addition function")
    return a + b



def subtraction():
    print ("Subtraction function")
    a = float(input("Enter the value of a :"))
    b = float(input("Enter the value of b :"))
    print(f"value of a = {a} inside the subtraction function")
    return a - b

result = addition()
print(result)

result = subtraction()
print(result)
