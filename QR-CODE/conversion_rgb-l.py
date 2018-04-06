# -*- coding: utf-8 -*-
#Author: DRISSI Rayan, GAUCHER Aloïs

from PIL import Image

signe = Image.open("signe.png")
signe_final = Image.new("L",(250,250))

for x in range(250):
	for y in range(250):
		pixel= img.getpixel((x,y))
		pixelL = (pixel[0]+pixel[1]+pixel[2])/3
		signe_final.putpixel((x,y),pixelL)

signe_final.show()
signe_final.save("signe final.png")