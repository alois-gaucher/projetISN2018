# -*- coding: utf-8 -*-
#Author: DRISSI Rayan, GAUCHER Aloïs

#Importation des bibliothèques nécéssaires
from PIL import Image

def lecture_pixel(img):
	liste = []
	l,h = img.size
	for y in range(h):
		for x in range(l):
			pixel = img.getpixel((x,y))
			if pixel == (255):
				liste.append(0)
			elif pixel == (0):
				liste.append(1)
	print liste
	
img = Image.open("fin.png")		
lecture_pixel(img)