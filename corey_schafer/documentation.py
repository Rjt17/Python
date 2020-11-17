#!/usr/bin/env python

function = str(input("Enter a function: "))
function = f"{function}()"
print(function)

print(f"Documentation for function {function} is: ")

print(function.__doc__)
