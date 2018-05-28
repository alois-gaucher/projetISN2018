# -*- coding: utf-8 -*-
#Author: DRISSI Rayan, GAUCHER Aloïs

#Conversion du mot binaire en décimal
def dec_bin(list):
	resultat = 0
	for x in range(8):
		a = list[x]
		if a == 0:
			a = 0
		else:
			a = 2
		resultat = resultat + a**(7-x)
	cara = chr(resultat)
	print resultat
	return cara

liste = []
liste = input("entrer")
print liste
car = dec_bin(liste)
print car

put = input()