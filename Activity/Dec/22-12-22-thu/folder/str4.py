### String

#4.  Write a program that parses a binary number to a decimal integer. 
#For example, 11001 (1 * 24 + 1 * 23 + 0 * 22 + 0 * 21 + 1 * 20).


binary = input('enter a number: ') 
decimal = 0 
for digit in binary: 
    decimal = decimal*2 + int(digit) 
print(decimal)