#!/usr/bin/env python

number = int(input("Enter a number:"))

if (number > 17):
    print(2 * (number - 17))
elif(number < 17):
    print(17 - number)
else:
    print("Entered number is equal to 17.")
