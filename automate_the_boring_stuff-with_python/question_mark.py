#!/usr/bin/env python
import re

batRegex = re.compile(r"Bat(wo)?man")
mo1 = batRegex.search("the adventure of Batwoman")
print(mo1.group())

mo2 = batRegex.search("the adventures of Batman")
print(mo2.group())
