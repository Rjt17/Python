#!/usr/bin/env python
import re

batRegex = re.compile(r"bat(man|mobile|copter|bat)")
mo = batRegex.search("batmobile is a very good car of batman")
print(mo.group())
