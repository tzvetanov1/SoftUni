import sys

number_one = int(input())
number_two= int(input())
number_three = int(input())


current = -sys.maxsize - 1

if number_one > number_two and number_one > number_three:
    current = number_one
elif number_two > number_three and number_two > number_one:
    current = number_two
else:
    current = number_three

print(current)