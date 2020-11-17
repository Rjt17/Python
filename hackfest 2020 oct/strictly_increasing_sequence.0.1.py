arr = [1,2,3,5]
length = len(arr)

"""removes all the duplicates and 
compares the list to original list"""

def counter(arr):
	arr_pure = list(dict.fromkeys(arr))
	if arr == arr_pure:
		return(True)
	else:
		return(False)

#finds out the duplicates in list
#dups = list(set(x for x in arr if arr.count(x) > 1))

if length == 1:
	print("First")
elif counter(arr) == True:
	print("First")
elif length % 2 != 0:
	print("First")
else:
	print("Second")

