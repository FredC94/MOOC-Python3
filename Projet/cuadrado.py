#!/usr/bin/env python3
# coding: utf-8
from tkinter import *
 
master = Tk()
 
 
class clase:
    lista_botones=[]
    etiqueta=Label(text="Etiqueta",bg="red")
    def __init__(self):
        for b in range(10):
            self.lista_botones.append( Button(text=str(b),bg="green") )
            self.lista_botones[-1].pack()
            #self.lista_botones[-1].configure(bg="blue")
           
        #etiqueta=Label(text="Etiqueta",bg="red")
        self.etiqueta.pack()
        self.etiqueta.after(1000,self.animate)
           
    def animate(self):
        print ("Entra animate")
        #mira la lista de botones
        for b in self.lista_botones:
            if b.cget("bg")=="green":
                b.configure(bg="yellow")
            else:
                b.configure(bg="green")
               
        self.etiqueta.after(1000,self.animate)
 
 
 
botones=clase()
mainloop()