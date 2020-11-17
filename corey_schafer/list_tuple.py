#!/usr/bin/env python
list1 = []

for index in range(4):
    numbers = int(input(f"Enter number:"))
    list1.append(numbers)

tuple1 = tuple(list1)

print(list1)
print(tuple1)
