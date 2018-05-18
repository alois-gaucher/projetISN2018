# -*- coding: utf-8 -*-
#Author: DRISSI Rayan, GAUCHER Aloïs

from PIL import Image

def pixel_blanc(img,x,y):
	pix = (255)
	img.putpixel((x,y),pix)

def pixel_noir(img,x,y):
	pix = (0)
	img.putpixel((x,y),pix)

def choix_binaire(list,img):
	l = len(list)
	x,y = 0,0
	for z in range(l):
		var = list[z]
		if var == 1:
			pixel_noir(img,x,y)
		else:
			pixel_blanc(img,x,y)
		x = x + 1
		if x > 24:
			x = 0
			y = y + 1
		else:
			x = x