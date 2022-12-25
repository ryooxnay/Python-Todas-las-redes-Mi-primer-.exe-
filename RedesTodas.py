# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 23:09:44 2022

@author: USER
"""
#CMD --->nets wlan show profile
import os
from tkinter import * 
ven = Tk()
ven.title("Wifi-Password")
ven.geometry("500x700+100+30")
ven.config(bg = "black")
txtRed = StringVar()
def pws():
    ven2 = Tk()
    ven2.title("Wifi-Password")
    ven2.geometry("500x800+600+30")
    ven2.config(bg = "black")
    cmd= "netsh wlan show profile "+ txtRed.get() + " key=clear"
    resultado = os.popen(cmd)
    lblMensaje = Label(ven2, bg="black", fg = "white", text=resultado.read()).pack()
    ven2.mainloop()
def mostrar():
    cmd = "netsh wlan show profile"
    resultado = os.popen(cmd)
    lblMensaje = Label(ven, bg="black", fg = "white", text=resultado.read()).place(x=120, y = 150)
def buscar():
      #(1.0, "end-1c")
    cmd= "netsh wlan show profile "+ txtRed.get() + " key=clear"
    resultado = os.popen(cmd)
    

lbM = Label(ven,text="",bg="black", fg="white", font="Helvetica 15 bold").pack()

btnMostar = Button(ven, text="Mostrar Todas las Redes guardadas", command = mostrar).pack()

lbM2 = Label(ven,text="↧ Nombre de WIFI para obtener password ↧",bg="black", fg="white", font="Helvetica 15 bold").place(x = 50, y = 70)
txt_wifi = Entry(ven, textvariable = txtRed).place(x = 150, y = 110)

btnBuscar = Button(ven, text = "Buscar Passwort", command = pws).place(x=290, y = 105)
#boton = Button(ven,text="Aceptar", bg="green", font="Helvetica 15 bold").pack()
lbY = Label(ven, text = "©_RyOoxNaY",bg="black", fg="white").pack(side = BOTTOM)
"""
cmd = "netsh wlan show profile"
resultado = os.popen(cmd)
print(resultado.read())
#miarchivo = open("wifi.csv", "a")
red = input("Ingrese el nombre de la red : ")
cmd2 = "netsh wlan show profile ", red , " key=clear" 
resultado2 = os.popen(cmd2)
print(resultado2)
"""
ven.mainloop()
