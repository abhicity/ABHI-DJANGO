file_pointer = open("new_file_1.txt")
file_data = file_pointer.read()
print(file_data)

file_pointer.close()