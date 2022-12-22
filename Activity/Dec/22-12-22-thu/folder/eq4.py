### Exercise Questions

# 4. Write a program to read two integers and perform arithmetic operations on them
#(addition, subtraction, multiplication, division, Modules, floor division ).


num1 = input("Enter first number: ") 
num2 = input("Enter second number: ")
  
# Addition two numbers  
add = float(num1) + float(num2)

# Subtract two numbers  
sub = float(num1) - float(num2)

# Multiply two numbers  
mul = float(num1) * float(num2)

#Divide two numbers  
div = float(num1) / float(num2)

#Modules two numbers  
mod = float(num1) % float(num2)

#Floor Division two numbers  
fdiv = float(num1) // float(num2)




# Display the addition 
print('The addition of {0} and {1} is {2}'.format(num1, num2, add))
  
# Display the subtraction  
print('The subtraction of {0} and {1} is {2}'.format(num1, num2, sub))

# Display the multiplication  
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))

# Display the division  
print('The division of {0} and {1} is {2}'.format(num1, num2, div))

# Display the Modulus
print('The Modulus of {0} and {1} is {2}'.format(num1, num2, mod))

# Display the Floor Division  
print('The Floor Division of {0} and {1} is {2}'.format(num1, num2, fdiv))