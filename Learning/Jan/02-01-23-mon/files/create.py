#for i in range(5):
 #   file_pointer = open(f"new_file_{i}.txt", mode= "x")
  #  file_pointer.write(f"New File with name = new_file.{i}.txt")
   # file_pointer.close()



for i in range(5):
    print (input("Enter the numbers of files you want to create."))

    file_pointer = open(f"new_file_{i}.txt", mode= "x")

    file_pointer.write(f"New File with name = new_file.{i}.txt")
    file_pointer.close()