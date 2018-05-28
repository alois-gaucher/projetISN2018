# -*- coding: utf-8 -*-
#Author: DRISSI Rayan, GAUCHER Aloïs

#Importation des bibliothèques nécéssaires
from PIL import Image

#Ouverture de l'image
signe = Image.open("signe.png")
signe_final = Image.new("L",(250,250))

#Conversion de l'image en noir et blanc
for x in range(250):
	for y in range(250):
		pixel= img.getpixel((x,y))
		pixelL = (pixel[0]+pixel[1]+pixel[2])/3
		signe_final.putpixel((x,y),pixelL)

#Ouverture de l'image finale
signe_final.show()
signe_final.save("signe final.png")