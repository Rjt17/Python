binary = str(input())
temp = binary
decimals = []
greatest = 2
temp_list = list(binary)

if "1" not in binary:
	print(-1)
elif "0" not in binary:		
	print(0)
elif temp_list.count("1") == 1:
	print(len(binary)-1)
else:
	for x in range(len(binary)):
		number = temp[0]
		temp = temp[1:] + number
		if number != "1":
			decimals.append(int(temp, 2))
	decimals.sort()

	for x in range(len(decimals)):
		for power in range(greatest, len(binary)):
			divisor = 2 ** power
			if decimals[x] % divisor != 0:
				break
			else:
				greatest = power


	print(greatest)