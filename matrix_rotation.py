#!/usr/bin/env python
###this is a program to print the resultant matrix after "r" anticlockwise rotations

m, n, r = 4, 4, 1
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


def rotator(matrix, m, n):
	a,b = 0,0
	while b != n:
		matrix[a][b],matrix[a][b+1] = matrix[a][b+1],matrix[a][b]
		b += 1
	while a != m:
		matrix
		



def same_rotator(matrix, m, n):
	#prints the same matrix again cause r = 4
	for x in range(0,m):
		for y in range(0,n):			
			print(matrix[x][y], "", end="")
		print()

if r%4 == 0:
	same_rotator(matrix, m, n)
elif r%3 == 0:
	rotator(matrix, m, n)
	rotator(matrix, m, n)
	rotator(matrix, m, n)
elif r%2 == 0:
	rotator(matrix, m, n)
	rotator(matrix, m, n)
else:
	rotator(matrix, m, n)