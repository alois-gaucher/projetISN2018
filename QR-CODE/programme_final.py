# -*- coding: utf-8 -*-
#Author: DRISSI Rayan, GAUCHER Aloïs

#Fonction menu principal
def open_world():
	print "_" * 31, "MENU PRINCIPAL", "_" * 31
	print "1. Encoder un message" #Fait appel à la fonction permettant l'encodage d'un message dans un QR Code
	print "2. Décoder un QR Code" #Fait appel à la fonction permettant le décodage d'un QR Code
	print "3. Afficher le signe distinctif" #Fait appel à la fonction permettant d'afficher le signe distinctif de notre QR Code
	print "4. Crédits" #BLA BLA BLA
	print "5. Sortie" #Sortie du programme
	print "_" * 78
boucle = True

#Fonction conversion en binaire
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

#Fonction traitement message > binaire
def encodage():
	liste = []
	message = raw_input("Entrez le message à encoder: ")
	for caractere in message:
		var_temp = ord(caractere)
		print var_temp
		liste.append(var_temp)
		print liste

list = []
convertisseur(message,list)
temps = len(list)
while temps < 7:
	temps = len(list)
	list.append(0)
	
print "Votre message encodé est: ",list

#Boucle permettant à l'utilisateur de faire son choix entre les différents menus
while boucle == True:
	open_world()
	choix = input("Faites votre choix [1-5]: ")
	if choix == 1:
		print("Vous avez choisi d'encoder un message")
		encodage()
	elif choix == 2:
		print("Vous avez choisi de décoder un message")
	elif choix == 3:
		print("Vous avez choisi d'afficher le signe distinctif")
	elif choix == 4:
		print("Vous avez choisi d'afficher les crédits")
	elif choix == 5:
		print("Aurevoir !")
		break;			
	else:
		input("Entrez un chiffre entre 1 et 5 !")

put = input()