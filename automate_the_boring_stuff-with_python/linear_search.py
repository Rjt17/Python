#!/usr/bin/env python

searchList = []
i = int(input("please enter the number of values: "))
for x in range(i):
    item = int(input(f"enter the no. {x+1}: "))
    searchList.append(item)

print(searchList)
target = int(input("please enter the value to search: "))
for location in range(i):
    if (searchList[location] == target):
        print(f"value found at location {searchList[location]}")
    else:
        print(f"value not found at location {searchList[location]}")
