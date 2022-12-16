def split data: = "Axy3#%moQn$_5.61"
upper_case = ""
lower_case = ""
number = ""
odd_number = ""
even_number = ""
special_char = ""


for a in data:
 
    if (a.isupper())== True:
        upper_case += a

    elif (a.islower())== True:
        lower_case += a

    elif (a.isnumeric())== True:
        number += a

    elif (a % 2 == 0) == True: 
        odd_number.append(a)

    #elif (a % 2 == 0)== True: 
         #even_number.append(a) 

    #elif (a.isnumeric())== True:
        #even_number += a


    else :
        special_char +=a
        

 
print("After changing:")
print(upper_case)
print(lower_case)
print(number)
print(even_number)
print(odd_number)
print(special_char)



#data = "Axy3#%moQn$-561"


#upper_case =
#lower_case =
#number =
#special_char =