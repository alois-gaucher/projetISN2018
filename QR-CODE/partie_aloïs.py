# -*- coding: utf-8 -*-
#Author: DRISSI Rayan, GAUCHER Aloïs

#Importation des bibliothèques nécéssaires
from PIL import Image

#Fonction permettant de reconnaître si l'image à décoder est bien un QR Code
def ghost_recon(pic,img):
	fin = True
	print "Vous avez choisi le fichier image: ",img
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


def dec_bin(liste):
	listetemp = []
	listefin = []
	resultat = 0
	for loop in range(8):
		listetemp.append(liste[0])
		del liste[0]
		a = listetemp[0]
		del listetemp[0]
		if a == 0:
			a = 0
		else:
			a = 2
		resultat = resultat + a**(7-loop)
	print resultat
	for loop in range(resultat):
		vari = 0
		for x in range(8):
			a = liste[0]
			del liste[0]
			if a == 0:
				a = 0
			else:
				a = 2
			vari = vari + a**(7-x)
			print vari
		listefin.append(vari)
	return listefin

#Ouverture de l'image reconnue
pic = Image.open(raw_input("Quelle image voulez-vous ouvrir? (.png) "))
img = Image.open("signe final.png")
validite = ghost_recon(img,pic)
if validite == True:
	print "Votre image est bien un QR Code et peut être décodée!"
else:
	print "Votre image n'est pas reconnaissable comme un QR Code!"

#Lis les pixels
def lecture_pixel(img):
	liste = []
	l,h = img.size
	for y in range(h):
		for x in range(l):
			pixel = img.getpixel((x,y))
			if pixel > (127):
				liste.append(0)
			elif pixel < (127):
				liste.append(1)
	return liste
	
img = Image.open("fin.png")	
liste = []	
liste = lecture_pixel(img)


a = dec_bin(liste)
print a
resultat = ''
for loop in range(len(a)):
	var = a[loop]
	resultat = resultat + chr(var)
print resultat

put = input()