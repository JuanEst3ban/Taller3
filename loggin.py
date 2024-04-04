import tkinter as tk 
from tkinter import*
from tkinter import messagebox
from Menu import*
from Tooltip import *

class Loggin(Menu):
   
    def verCaracteres(self,event):
        self.txtPasword.configure(show='')
        self.btnVer.configure(text="ocultar")

    def ocultarCaracteres(self,event):
        self.txtPasword.configure(show="*")
        self.btnVer.configure(text="ver")
    def validarLongitud(self,event):
        longitud=len(self.txtPasword.get()) 
        if longitud >=8:
            self.btnIngresar.configure(state="normal")
        else:
            self.btnIngresar.configure(state="disabled")
    def mostrarAyuda(self,event):
        messagebox.showinfo("ayuda","debe diligenciar todos los campos marcados con *\nluego presione el boton Registrarse")    
    def __init__(self):
        
        self.ventana=tk.Tk()
      
        self.ventana.resizable(0,0)
        self.ventana.config(width=300,height=225)

        self.lblTitulo=tk.Label(self.ventana,text="inicio sesion ")
        self.lblTitulo.place(x=125,y=25)

        self.lblUsuario=tk.Label(self.ventana,text="Usuario")
        self.lblUsuario.place(x=25,y=60)
        self.txtUsuario=tk.Entry(self.ventana,width=25)
        self.txtUsuario.place(x=90,y=60)

        self.lblPasword=tk.Label(self.ventana,text="contraseña")
        self.lblPasword.place(x=25,y=85)
        self.txtPasword=tk.Entry(self.ventana,width=25,show="*")
        self.txtPasword.place(x=90,y=85)
        self.txtPasword.bind("<KeyRelease>",self.validarLongitud)

        self.btnVer=tk.Button(self.ventana,text="ver")
        self.btnVer.place(x=25,y=110)

        self.btnVer.bind("<Enter>",self.verCaracteres)
        self.btnVer.bind("<Leave>",self.ocultarCaracteres)

        self.btnIngresar=tk.Button(self.ventana,text="ingresar",command=self.crearVentanaM,width=20,state="disabled") 
        self.btnIngresar.place(x=140, y=110)

        self.btnLimpiar=tk.Button(self.ventana,text="limpiar") 
        self.btnLimpiar.place(x=80,y=110)
        
        iconoAyuda=tk.PhotoImage(file=r"icons/help.png")
        self.btnAyuda =tk.Button(self.ventana, image=iconoAyuda)
        self.btnAyuda.place(x=220, y=25, width=25, height=25)
        Tooltip(self.btnAyuda,"presione para obtener ayuda!\nALT+a")
        self.btnAyuda.bind('<Button-1>', self.mostrarAyuda)

        self.ventana.bind('<Alt-a>', self.mostrarAyuda)
        
        
        self.ventana.mainloop()











        

