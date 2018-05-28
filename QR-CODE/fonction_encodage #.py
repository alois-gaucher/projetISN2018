# -*- coding: utf-8 -*-
#Author: DRISSI Rayan, GAUCHER Aloïs
resultat = 'a'
def convertisseur(nombre,list):
	if nombre == 0:
		for loop in range(8):
			list.append(0)
	else:
		while nombre!=0:
	        	a = (nombre//2)
			reste = nombre%2
	        	list.append(reste)
			nombre = a
	print list
	return list


def encodage():
	liste = []
	message = raw_input("Entrez le message à encoder: ")
	for caractere in message:
		var_temp = ord(caractere)
		print var_temp
		liste.append(var_temp)
		print liste

list = []
convertisseur(56,list)
temps = len(list)
while temps < 7:
	temps = len(list)
	list.append(0)
	
print "Votre message encodé est: ",list
put = input()