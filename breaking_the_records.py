#!/usr/bin/env python
#EASY
#HackerRank

n = 10
scores = [3,4,21,36,10,28,3,5,24,42]
maxMin = [0, 0]

def breakingRecords(scores, n):
	global maxMin
	minimum = scores[0]
	maximum = scores[0]
	for x in range(1, n):
		if scores[x] > maximum:
			maximum = scores[x]
			maxMin[0] += 1
		elif scores[x] < minimum:
			minimum = scores[x]
			maxMin[1] += 1

breakingRecords(scores, n)
print(maxMin)