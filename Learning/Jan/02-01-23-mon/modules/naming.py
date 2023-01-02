print(__name__)
print ("= First Line =")

from greet import greet_function

names = ['Abhi', 'Chandhan', 'Rahul']

for name in names:
    greet_function(name, "Birthday Party")