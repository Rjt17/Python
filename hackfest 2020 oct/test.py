binary = str(input())
temp = binary
decimals = []
decimals.append(int(binary, 2))
powers = []
for x in range(0,len(binary)+1):
	number = temp[0]
	temp = temp[1:] + number
	decimals.append(int(temp, 2))

decimals.sort()

for x in range(len(decimals)):
	if decimals[x] % 2**13 == 0:
		print("yes")