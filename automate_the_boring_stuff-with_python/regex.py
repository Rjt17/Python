#!/usr/bin/env python

import re

phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo = input("enter a phone number:")
searchResult = phoneNumRegex.search(mo)
if searchResult != None:
    print(f"The entered phone number {searchResult.group(1)}-{searchResult.group(2)}-{searchResult.group(3)} is a phone number.")
else:
    print("Entered number is not a phone number")
