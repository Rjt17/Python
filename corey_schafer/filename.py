#!/usr/bin/env python

filename = str(input(f"Enter a filename: "))
fileExt = filename.split(".")

print(fileExt[-1])
