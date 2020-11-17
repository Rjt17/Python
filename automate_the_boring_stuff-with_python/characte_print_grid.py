#!/usr/bin/env python

from __future__  import print_function
																#To print:-
grid = [['.','.','.','.','.','.',],								#..OO.OO..
		['.','O','O','.','.','.',],								#.0000000.
		['O','O','O','O','.','.',],								#.0000000.
		['O','O','O','O','O','.',],								#..00000..
		['.','O','O','O','O','O',],								#...000...
		['O','O','O','O','O','.',],								#....0....
		['O','O','O','O','.','.',],
		['.','O','O','.','.','.',],
		['.','.','.','.','.','.',]] 

for i in range(len(grid[0])):
	for j in range(len(grid)):
		print(grid[j][i], end=" ")
	print('')