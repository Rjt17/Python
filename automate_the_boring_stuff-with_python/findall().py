#!/usr/bin/env python
import re

phoneNumRegex = re.compile(r"\d{3}-\d{3}-\d{4}")
mo1 = phoneNumRegex.search("cell: 415-555-9999 work: 212-555-0000")
print(mo1[0])
