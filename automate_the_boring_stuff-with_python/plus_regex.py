#!/usr/bin/env python
import re

batRegex = re.compile(r"bat(wo)+man")
mo1 = batRegex.search("the adventures of batwoman")
print(mo1.group())
