binary_s = str(input())
temp_binary = binary_s
decimals = []
greatest = 0
if "1" not in binary_s:
	print(-1)
else:
	for x in range(0, len(binary_s)):
		temp_binary = temp_binary[1:] + temp_binary[0]
		decimals.append(int(temp_binary, 2))
		decimals.sort()
	decimal = decimals[-1]
	for power in range(len(binary_s), 0, -1):
		divisor = 2 ** power
		if decimal % divisor == 0:
			greatest = power
			break
print(greatest)