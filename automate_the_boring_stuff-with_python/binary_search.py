#!/usr/bin/env python

searchList = []
rangeList = int(input("enter the number of values of the list: "))
if (rangeList <= 0):
    print("your entered length of list is less than or equal to zero")
else:
    for values in range(rangeList):
        searchList.append(values + 1)
    print(searchList)

    target = int(input("enter the value you want to search under or equal to {}: ".format(rangeList)))
    if (target > rangeList):
        print("you entered a value larger than {}".format(rangeList))
    elif (target == 0):
        print("you entered a number to search which is equal to 0")
    elif (target < 0):
        print("you entered a number to search which is less than 0")
    else:
        lastTemp = rangeList
        first = 0
        last = lastTemp
        middle = int((first + last) / 2)

        while (first <= last):
            if (searchList[middle] < target):
                first = middle + 1
            elif (searchList[middle] == target):
                print("search value found at location {}".format(searchList[middle]))
                break
            else:
                lastTemp = last
                last = middle - 1

            middle = int((first + last) / 2)

        if (first > last):
            print("value not found")