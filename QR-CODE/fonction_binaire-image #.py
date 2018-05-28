# -*- coding: utf-8 -*-
#Author: DRISSI Rayan, GAUCHER Aloïs

#Importation des bibliothèques nécéssaires
from PIL import Image

#Ajoute un pixel blanc
def pixel_blanc(img,x,y):
	pix = (255)
	img.putpixel((x,y),pix)

#Ajoute un pixel noir
def pixel_noir(img,x,y):
	pix = (0)
	img.putpixel((x,y),pix)

#Code le mot binaire de 8 bits dans l'image
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

choix_binaire()