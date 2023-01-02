#2. Create a tables file.
#   1. table_1.txt
#   2. table_2.txt
#   3. ...
#   4. table_50.txt
#   5. Each table file should have the table for the number specified at the last. ex: table_5.txt
#      1. 5x1=5
#      2. ...
#      3. 5x10=50



for i in range(1,51):
    file_pointer = open(f"table_{i}.txt", mode='x')
    file_pointer.write(f"MULTIPLICATION TABLE FOR {i}.txt")



    
    file_pointer.close()






