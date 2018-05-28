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

#Boucle permettant à l'utilisateur de faire son choix entre les différents menus
while boucle == True:
	open_world()
	choix = input("Faites votre choix [1-5]: ")
	if choix == 1:
		print("Vous avez choisi d'encoder un message")
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