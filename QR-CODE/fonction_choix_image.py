# -*- coding: utf-8 -*-
#Author: DRISSI Rayan, GAUCHER Aloïs


from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

root = Tk(  )

def parcourir():
    fichier = askopenfilename(initialdir="/",
                           filetypes =(("Fichiers PNG", "*.png")),
                           title = "Sélectionnez un fichier à ouvrir"
                           )
    print (fichier)
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(fichier,'r') as UseFile:
            print(UseFile.read())
    except:
        print("Le fichier n'existe pas")


Title = root.title("File Opener")
label = ttk.Label(root, text ="I'm BATMAN!!!",foreground="red",font=("Helvetica", 16))
label.pack()

#Menu Bar

menu = Menu(root)
root.config(menu=menu)

file = Menu(menu)

file.add_command(label = 'Open', command = OpenFile)
file.add_command(label = 'Exit', command = lambda:exit())

menu.add_cascade(label = 'File', menu = file)





root.mainloop()
