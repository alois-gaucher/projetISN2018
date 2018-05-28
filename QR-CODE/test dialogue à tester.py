# -*- coding: utf-8 -*-
#Author: DRISSI Rayan, GAUCHER Aloïs

from Tkinter import *
from tkFileDialog import *
 
def fct_parcourir():
        fichier=askopenfilename(parent=fenetre1,initialdir="/",title="Selection d'un fichier")
        print fichier
     
fenetre1=Tk()
bouton1=Button(fenetre1,text="Parcourir",command=fct_parcourir)
bouton1.pack()
fenetre1.mainloop()

print "Votre fichier sélectionné est", fichier

con = input()