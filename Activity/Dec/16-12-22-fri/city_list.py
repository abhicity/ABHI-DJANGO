#1. Create a list of city name with STD code from the provided string below using str.strip module.

#STRING DATA: std_code = "11 Delhi, 22 Mumbai, 33 Kolkata, 44 Chennai, 40 Hyderabad, 80 Bangalore, 20 Pune, 79 Ahmedabad"

#LIST OUTPUT: std_code_list['11 Delhi', ' 22 Mumbai', ' 33 Kolkata', ' 44 Chennai', ' 40 Hyderabad', ' 80 Bangalore', ' 20 Pune', ' 79 Ahmedabad']

def convert(string):
    li = list(string.split(","))
    return li

std_code = "11 Delhi, 22 Mumbai, 33 Kolkata, 44 Chennai, 40 Hyderabad, 80 Bangalore, 20 Pune, 79 Ahmedabad"
print(convert(std_code))
