binary_s = str(input())
temp_binary_list = list(binary_s)
temp_binary = binary_s
length = len(binary_s)
decimals = []
decimal = 0
greatest_pow = 0
powers = []

for x in range(len(binary_s)):
	temp_binary = temp_binary[1:] + temp_binary[0]
	decimals.append(int(temp_binary, 2))
	decimals.sort()
print(len(decimals))
decimal = decimals[-1]
print(decimal)

if "1" not in binary_s:
	print(-1)
elif temp_binary_list.count("1") == 1:
	print(length - 1)
else:
	for power in reversed(range(length)):
		divisor = 2 ** power
		if decimal % divisor == 0:
			greatest_pow = power
			break
	print(greatest_pow)