# -*- coding: utf-8 -*-
#Author: DRISSI Rayan, GAUCHER Aloïs

#Conversion décimal vers binaire
def dec_bin(a):
	liste = []
	listf = []
#Si a = 0, ne mettre que des 0 sur 8 bits
	if a == 0:
		for loop in range(8):
			list.append(0)
#Sinon effectuer la conversion vers le binaire (par division)
	else:
		while a !=0:
			resultat = a //2
			reste = a % 2
			liste.append(reste)
			a = resultat
		while len(liste)!=8:
			liste.append(0)
#Remet la liste dans l'ordre			
		y = len(liste)
		for x in range(len(liste)):
			listf.append(liste[y-1])
			y = y -1
	return listf

#Demande à l'utilisateur l'entrée à convertir
nombre = input("Entrer le nombre a convertir: ")

liste = dec_bin(nombre)
print liste

frigo_instable = input()