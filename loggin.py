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

    def Limpiar(self, event):
        self.txtTelefono.delete(0, END)
        self.txtapellido.delete(0, END)
        self.txtEmail.delete(0, END)
        self.txtNombre.delete(0, END)
        self.txtPasword.delete(0, END)
        self.txtUsuario.delete(0, END)
        self.txtusuario1.delete(0, END)
    
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


        iconoVer = tk.PhotoImage(file= r"Taller3\icons\eye.png")
        self.btnVer=tk.Button(self.ventana,text="ver", image=iconoVer, compound=LEFT)
        self.btnVer.place(x=10,y=110)
        Tooltip(self.btnVer, "Presione para ver la contraseña. \nAlt+L")


        self.btnVer.bind("<Enter>",self.verCaracteres)
        self.btnVer.bind("<Leave>",self.ocultarCaracteres)

        self.btnIngresar=tk.Button(self.ventana,text="ingresar",command=self.crearVentanaM,width=20,state="disabled") 
        self.btnIngresar.place(x=140, y=110)

        iconoLimpiar = tk.PhotoImage(file= r"Tercer Semestre\Place\icons\textfield_delete.png")
        self.btnLimpiar = tk.Button(self.ventana, text="limpiar", image=iconoLimpiar, compound=LEFT) 
        self.btnLimpiar.place(x=70,y=110)
        Tooltip(self.btnLimpiar, "Presione para Limpiar los campos de texto.\nAlt+l")
        
        
        
        iconoAyuda=tk.PhotoImage(file=r"Taller3\icons\help.png")
        self.btnAyuda =tk.Button(self.ventana, image=iconoAyuda)
        self.btnAyuda.place(x=220, y=25, width=25, height=25)
        Tooltip(self.btnAyuda,"presione para obtener ayuda!\nALT+a")
        self.btnAyuda.bind('<Button-1>', self.mostrarAyuda)

        self.ventana.bind('<Alt-a>', self.mostrarAyuda)
        
        
        self.ventana.mainloop()











        

