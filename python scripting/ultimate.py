#!/usr/bin/env python
#2732x768

import pyautogui as gui
gui.FAILSAFE = True

hot = 0
vet = 767

#to x = 767, y = 60

while True:
	gui.moveTo(hot, vet)
	hot += 10.084865629
	vet -= 10
	if (hot == 767 and vet == 60):
		break