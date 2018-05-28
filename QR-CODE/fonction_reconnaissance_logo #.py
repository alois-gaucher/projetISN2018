# -*- coding: utf-8 -*-
#Author: DRISSI Rayan, GAUCHER Aloïs

#Importation des bibliothèques nécéssaires
from PIL import Image

#Fonction permettant de reconnaître si l'image à décoder est bien un QR Code
def ghost_recon(pic):
	fin = True
	img = Image.open("signe final.png")
	l,h = img.size
	x,y = pic.size
#Reconnaissance par la résolution de l'image
	if ((x,y)) != (250,250):
		print "Votre image n'est pas reconnaissable comme un QR Code"
		fin = False
#Si l'image correspond en taille, vérification des pixels du bas permettant de reconnaître notre QR Code
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
#Ouverture de l'image reconnue
imag = Image.open("signe final.png")
validite = ghost_recon(imag)
print validite