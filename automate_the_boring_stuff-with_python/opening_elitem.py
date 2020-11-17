#!/usr/bin/env python

import os
os.chdir("/root/python_scripts")
elitem_open = open("/root/python_scripts/original_elitem.py")
elitem = elitem_open.read()
print(elitem)