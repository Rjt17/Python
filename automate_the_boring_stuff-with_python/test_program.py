#!/usr/bin/env python

s = input("enter the new string to encrypt")
s_length = len(s)
texts = s.split(" ")
texts.reverse()
encryptedString = ""
lowercaseLessM = {'b':2, 'c':3, 'd':4, 'f':6, 'g':7, 'h':8, 'j':10, 'k':11, 'l':12}
lowercaseMoreM = {'n':14, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
uppercaseLessM = {'B':2, 'C':3, 'D':4, 'F':6, 'G':7, 'H':8, 'J':10, 'K':11, 'L':12}
uppercaseMoreM = {'N':14, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
lowercaseVowels = {"a":1, "e":5, "i":9, "o":15, "u":21}
uppercaseVowels = {'A':1, 'E':5, 'I':9, 'O':15, 'U':21}
numbers = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
symbols = {}

for x in range(0, int(len(texts))):
	word = texts[x]
	for y in range(0, int(len(word))):
		if word[y] in lowercaseLessM:
			encryptedString += 
