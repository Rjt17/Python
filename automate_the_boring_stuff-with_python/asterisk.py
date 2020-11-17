#!/usr/bin/env python
import re
batRegex = re.compile(r"bat(wo)*man")
mo1 = batRegex.search("the adventures of batwowowoman")
print(mo1.group())

mo2 = batRegex.search("the adventures of batman")
print(mo2.group())

mo3 = batRegex.search("the adventures of batwoman")
print(mo3.group())
