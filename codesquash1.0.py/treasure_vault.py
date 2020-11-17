testcases = int(input())
inputs = []
temp_list = []
for x in range(0,testcases):
	ar = list(map(int, input().rstrip().split()))
	inputs.append(ar)

def changer(inputs,y,current_list,temp_list):
	if current_list.index(y) == 0:
		z = y+1
		temp_list.append(z)
	elif current_list.index(y) % 2 == 0:
		z = y+1
		temp_list.append(z)
	else:
		z = y+2
		temp_list.append(z)

for current_list in inputs:
	for y in current_list:
		changer(inputs,y,current_list,temp_list)
	for x in temp_list:
		print(str(x) + " ", end='')
	print(" ")
	temp_list = []