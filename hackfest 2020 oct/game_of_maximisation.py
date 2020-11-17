even = []
odd = []
greatest = 0
for x in range(0,len(arr)):
    if x%2 != 0:
        even.append(arr[x])
    else:
        odd.append(arr[x])
odd_sum = 0
even_sum = 0

for x in even:
    even_sum += x
for x in odd:
    odd_sum += x
if even_sum>odd_sum:
    greatest = odd_sum
else:
    greatest = even_sum

return greatest*2