# -*- coding: utf-8 -*-
#Author: DRISSI Rayan, GAUCHER Aloïs

from PIL import Image

def ghost_recon(pic):
	fin = True
	img = Image.open("signe final.png")
	l,h = img.size
	x,y = pic.size
	if ((x,y)) != (250,250):
		print "Votre image n'est pas reconnaissable comme un QR Code"
		fin = False
	else:
		for a in range(226,250):
			for b in range(226,250):
				pixela = img.getpixel((a,b))
				pixelb = pic.getpixel((a,b))
				if pixela == pixelb:
					random = 1
				else:
					fin = False
	return fin
imag = Image.open("signe final.png")
validite = ghost_recon(imag)
print validite