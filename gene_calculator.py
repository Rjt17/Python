#!/usr/bin/env python
#dna matching program

import re

#########################################################
def geneChecker(d,x,first,last,genes,health):
	global totalGeneHealth
	z = 0
	strand = d[x]
	firstGood = first[x]
	lastGood = last[x]
	geneValue = genes[x]
	geneLength = len(geneValue)
	strandLength = len(strand)

	for y in range(geneLength, strandLength+1):
		if geneValue == strand[z:y]:
			totalGeneHealth += 4
		z =+ 1
#######################################################

n = 6
genes = ["a", "b", "c", "aa", "d", "b"]
health = [1, 2, 3, 4, 5, 6]
s = 3
first = [1, 0, 2]
last = [5, 4, 4]
d = ["caaab", "xyz", "bcdybc"]

totalGeneHealth = 0

for x in range(0, s):
	"""strand = d[x]
	firstGood = first[x]
	lastGood = last[x]

	geneValue = "aa"
	geneLength = len(geneValue)
	strandLength = len(strand)
	z = 0
	for y in range(geneLength, strandLength+1):
		if geneValue == strand[z:y]:
			totalGeneHealth += 4 

		z += 1"""
	geneChecker(d,x,first,last,genes,health)
print(totalGeneHealth)
print()