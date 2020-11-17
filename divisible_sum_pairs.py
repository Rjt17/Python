#!/usr/bin/env python
#Easy
#HackerRank

n,k = 6,3
ar = [1,3,2,6,1,2]

def divisibleSumPairs(n, k, ar):
	appropriate = 0
	sums = 0
	for x in range(0,n-1):
		for y in range(x+1,n):
			sums = ar[x]
			sums = sums + ar[y]
			if sums%k == 0:
				appropriate += 1
	return appropriate
print(divisibleSumPairs(n,k,ar))