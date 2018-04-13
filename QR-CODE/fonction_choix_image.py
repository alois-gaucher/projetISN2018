# -*- coding: utf-8 -*-
#Author: DRISSI Rayan, GAUCHER Aloïs

from PIL import Image
from Tkinter import *
from tkFileDialog import *

def parcourir():
	myfiletypes = [('Fichiers PNG', '*.png')]
	fenetre1.update()
	fichier=askopenfilename(parent=fenetre1,initialdir="/",title="Selection d'un fichier PNG", filetypes = myfiletypes)
	fenetre1.withdraw()

	return fichier
     
fenetre1=Tk()
bouton1=Button(fenetre1,text="Parcourir...",command=parcourir).pack()
fenetre1.mainloop()
