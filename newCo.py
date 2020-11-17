#!/usr/bin/env python

arr_count = 7
arr = [1,2,3,4,5,6,7]

def counter(arr, arr_count):
	appropriate = []
	for x in range(0, arr_count):
		number = arr[x]
		for y in range(0, arr_count):
			if number == arr[y]:
				 