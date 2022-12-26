## List

#2. Write a program that prints the maximum value of the second half of the list.



#list = [10, 20, 30, 40, 50, 60]

#list1 = list [0:3]
#list2 = list [3:6]


#print ("First Half: ",list1)
#print ("Second Half: ",list2)


def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

number = input("Enter the number :")
b, c = split_list(number)
print(max(c))
