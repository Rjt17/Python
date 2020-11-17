binary_s = input()
possible_binary = []
temp_binary = binary_s
decimals = []
value = 0
all_greatest = []

for x in range(0, len(binary_s)):
	temp_binary = temp_binary[1:] + temp_binary[0]
	possible_binary.append(temp_binary)

for x in possible_binary:
	decimals.append(int(x,2))

decimals.sort()

for x in decimals:
	if x % 2 != 0:
		decimals.remove(x)
#print(decimals)
def power_finder(value):
	all_divisors = []
	for power in range(0, len(decimals)+1):
		divisor = 2 ** power
		if value % divisor == 0:
			all_divisors.append(power)
	all_divisors.sort()
	#print(all_divisors)
	return all_divisors[-1]

for x in range(0, len(decimals)):
	value = decimals[x]
	all_greatest.append(power_finder(value))

all_greatest.sort()
#print(all_greatest)
print(all_greatest[-1])
