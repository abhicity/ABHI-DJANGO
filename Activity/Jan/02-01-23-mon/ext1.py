#1. print the file name and extension as a table format. files:
#   1. text.txt
#   2. create.py
#   3. style.css
#   4. custom.js
#   5. intro.md
#   6. introduction
#   7. test.min.css
#   8. testing.c
#   9. chapters
#   10. temp
#Eg: File Name : Extension temporary : md profile : jpg



files = 'text.txt, create.py, style.css, custom.js, intro.md, introduction, test.min.css, testing.c, chapters, temp'

x = files.split(",")

print(x)

i = x[0].split(".")
j = x[2].split(".")
print(i, sep=":")
print(j, sep=":")
