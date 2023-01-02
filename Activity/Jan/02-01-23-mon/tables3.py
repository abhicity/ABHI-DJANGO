#3. Create table file from the number list given by the user.


for i in range(1,51):
    file_pointer = open(f"table_{i}.txt", mode='x')
    file_pointer.write(f"MULTIPLICATION TABLE FOR {i}.txt")



    
    file_pointer.close()




num = int(input("Enter the tables number to print "))

for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
