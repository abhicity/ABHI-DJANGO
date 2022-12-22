### Exercise Questions

# 1. Write a program that calculates the number of seconds in a day.


def seconds_per_day(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    return seconds
print(seconds_per_day(1))