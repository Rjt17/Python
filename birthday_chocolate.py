#!/usr/bin/env python
#EASY
#HackerRank

n = 19
s = [2,5,1,3,4,4,3,5,1,1,2,1,4,1,3,3,4,2,1]
d,m = 18, 7

def birthday(n, s, d, m):
	approprite = 0
	sums = 0
	if m>=n:
		if m == n:
			for x in range(0,n):
				sums = sums + s[x]
			if sums == d:
				return 1
		else:
			return 0
	else:	
		for x in range(0, n-m+(1)):
			for y in range(0, m):
				sums = sums + s[x+y]
			if sums == d:
				approprite += 1
			sums = 0
		return approprite

result = birthday(n,s,d,m)
print(result)