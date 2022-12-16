#3. Find the Sum of Digits in a Number.

 #Eg: number = 256
 #Solution = 2+5+6 = 13

num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)

#def getsum(n):

    #sum = 0
    #for digit in str(n):
        #sum += int(digit)
    #return sum

#n = input("Enter the Number : ")
#print(getsum(n))


#num = input("Enter Number: ")
#sum = 0
