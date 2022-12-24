## List

#3. Write a program that creates a list of numbers 1–100 that are either divisible by 5 or 7.


n = []
for x in range(1, 100):
    if(x % 5 == 0) and (x % 7 == 0):
        n.append(x)
print(n, "is divisible by 5 and 7.")