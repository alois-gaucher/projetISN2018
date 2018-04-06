# -*- coding: utf-8 -*-
#Author: DRISSI Rayan, GAUCHER Aloïs

from PIL import Image

def signe_instable(pic):
	img = Image.open("signe final.png")
	l,h = img.size
	for x in range(l):
		for y in range(h):
			pixel = img.getpixel((x,y))
			pic.putpixel((x,y),pixel)
	pic.show()
	pic.save("qr_code.png")
	return img

nimg = Image.new("L",(250,250))
qrcode = signe_instable(nimg)

