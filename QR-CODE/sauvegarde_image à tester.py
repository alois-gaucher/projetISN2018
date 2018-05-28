# -*- coding: utf-8 -*-
#Author: DRISSI Rayan, GAUCHER Aloïs

#Fonction permettant de sauvegarder l'image via une fenêtre de dialogue
def save_theworld():
	import tkFileDialog
	myfiletypes = [('Fichiers PNG', '*.png')]
	filename = tkFileDialog.asksaveasfilename(initialdir="/",title="Selection d'un fichier PNG", filetypes = myfiletypes)
	a = 1
	b = []
	c = {}
	f = open(filename, 'wb')
	import pickle
	pickle.dump((a,b,c), f)
	f.close()

save_theworld()
print filename
put = input()