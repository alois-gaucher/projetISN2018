# -*- coding: utf-8 -*-
#Author: DRISSI Rayan, GAUCHER Aloïs

from PIL import Image

def car_dec(message):
	liste = []
	for x in message:
		liste.append(ord(x))
	return liste

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
		if x > 249:
			x = 0
			y = y + 1
		else:
			x = x
	return img

def signe_instable(pic):
	img = Image.open("signe final.png")
	l,h = img.size
	for x in range(l):
		for y in range(h):
			pixel = img.getpixel((x,y))
			pic.putpixel((x,y),pixel)
	pic.save("qr_code.png")
	return img

def dec_bin(a):
	liste = []
	listf = []
	if a == 0:
		for loop in range(8):
			list.append(0)
	else:
		while a !=0:
			resultat = a //2
			reste = a % 2
			liste.append(reste)
			a = resultat
		while len(liste)!=8:
			liste.append(0)
			
		y = len(liste)
		for x in range(len(liste)):
			listf.append(liste[y-1])
			y = y -1
	return listf

nimg = Image.new("L",(250,250))
img = signe_instable(nimg)
message = raw_input("Veuillez écrire le message à encoder: ")
liste = car_dec(message)
print liste

messagebin = []
for x in range(len(liste)):
	a = liste[x]
	b = dec_bin(a)
	for loop in range(8):
		messagebin.append(b[loop])
print messagebin

imgf = choix_binaire(messagebin,img)
imgf.save("fin.png")
imgf.show()
time = input()