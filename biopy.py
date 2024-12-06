import csv
import sys
import os
import subprocess
import tkinter
from tkinter import messagebox
import random

ventanaprincipal = "ventana1"
nombre = ""
apellido = ""
edad = ""
genero = ""
hemoglobina = ""
plaquetas = ""
bilirrubina = ""
globulosrojos = ""
globulosblancos = ""
glucosa = ""
creatinina = ""
colesterol = ""
sodio = ""
potasio = ""
calcio = ""
estadohemoglobina = ""
estadoplaquetas = ""
estadobilirrubina = ""
estadoglobulosrojos = ""
estadoglobulosblancos = ""
estadoglucosa = ""
estadocreatinina = ""
estadocolesterol = ""
estadosodio = ""
estadopotasio = ""
estadocalcio = ""
nombres = ["ERWIN", "MARIO", "ESTEBAN", "JOAQUÍN", "ALEX", "MARCO", "ANTONIO", "VALERIA", "NICOLE", "SOFÍA", "VALENTINA", "ROSA", "LUCIANA", "CAMILA", "MARCELA", "VIANKA",
           "ISABELA", "MIGUEL", "AZUL", "KEYLA", "EMILIANO", "FABRICIO", "MAURICIO", "FERNANDA", "ALEJANDRO", "RODRIGO", "GABRIEL", "FRANCO", "ULISES", "FABIÁN"]
apellidos = ["SOLANO", "PADILLA", "ROCHA", "ORELLANA", "ROJAS", "BASSWERNER", "ORTIZ", "LEMA", "CHIRINOS", "MARTÍNEZ", "LÓPEZ", "PACHECO", "TAMARES",
             "RIVAS", "RIVERO", "MOLINA", "VERA", "GARECA", "DUARTE", "AMAS", "MONTALVO", "CHOSCO"]
genero = [""]

paciente_contador = 0  


# Cambiar Imagen:

def resource_path(relative_path):
    """Obtiene la ruta absoluta para los recursos empaquetados."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def cambiarimagen():
    global ventanaprincipal
    if ventanaprincipal == "ventana1":
        imagen1 = tkinter.PhotoImage(file=resource_path("IBIO.png"))
        labelinicio.config(image=imagen1)
        labelinicio.image = imagen1
    elif ventanaprincipal == "ventana2":
        imagen2 = tkinter.PhotoImage(file=resource_path("DATOSP.png"))
        labelventana2.config(image=imagen2)
        labelventana2.image = imagen2
    elif ventanaprincipal == "ventana3":
        imagen3 = tkinter.PhotoImage(file=resource_path("DATOSH.png"))
        labelventana3.config(image=imagen3)
        labelventana3.image = imagen3
    elif ventanaprincipal == "ventana4":
        imagen4 = tkinter.PhotoImage(file=resource_path("DATOSB.png"))
        labelventana4.config(image=imagen4)
        labelventana4.image = imagen4
    elif ventanaprincipal == "ventana5":
        imagen5 = tkinter.PhotoImage(file=resource_path("RESULTADOS1.png"))
        labelventana5.config(image=imagen5)
        labelventana5.image = imagen5
    elif ventanaprincipal == "ventana6":
        imagen6 = tkinter.PhotoImage(file=resource_path("RESULTADOS2.png"))
        labelventana6.config(image=imagen6)
        labelventana6.image = imagen6
    elif ventanaprincipal == "ventana7":
        imagen7 = tkinter.PhotoImage(file=resource_path("RESULTADOS3.png"))
        labelventana7.config(image=imagen7)
        labelventana7.image = imagen7
        
# Ingresar a Ventanas:

def irventana2():
    global ventanaprincipal
    usuarioc = "0"
    contraseñac = "0"
    respuesta = messagebox.askquestion("CONFIRMACIÓN", "¿DESEAS INICIAR SESIÓN?")
    if respuesta == "yes":
        usuario = entry1.get().strip()
        contraseña = entry2.get().strip()
        if usuario == usuarioc and contraseña == contraseñac:
            messagebox.showinfo("AUTENTICACIÓN", "¡BIENVENIDO AL SISTEMA!")
            entry1.delete(0, tkinter.END)
            entry2.delete(0, tkinter.END)
            
            ventanaprincipal = "ventana2"
            cambiarimagen()
            ventana1.withdraw()
            ventana2.deiconify()
            
        else:
            messagebox.showerror("ERROR!", "CREDENCIALES INVÁLIDAS")
            entry1.delete(0, tkinter.END)
            entry2.delete(0, tkinter.END)
    else:
        messagebox.showwarning("ADVERTENCIA", "RECUERDA INGRESAR BIEN LOS DATOS")
        

def irventana3():
    global ventanaprincipal
    respuesta = messagebox.askquestion("CONFIRMACIÓN", "¿DESEAS CONTINUAR A LA SIGUIENTE VENTANA?")
    if respuesta == "yes":
        ventanaprincipal = "ventana3"
        cambiarimagen()
        ventana2.withdraw()
        ventana3.deiconify()
        
def irventana4():
    global ventanaprincipal
    respuesta = messagebox.askquestion("CONFIRMACIÓN", "¿DESEAS CONTINUAR A LA SIGUIENTE VENTANA?")
    if respuesta == "yes":
        ventanaprincipal = "ventana4"
        cambiarimagen()
        ventana3.withdraw()
        ventana4.deiconify()

def analisisdatos():
    global ventanaprincipal
    global nombre, apellido, edad, genero, hemoglobina, plaquetas, bilirrubina, globulosrojos, globulosblancos, glucosa, creatinina, colesterol, sodio, potasio, calcio
    global estadohemoglobina, estadoplaquetas, estadobilirrubina, estadoglobulosrojos, estadoglobulosblancos, estadoglucosa, estadocreatinina, estadocolesterol, estadosodio, estadopotasio, estadocalcio 
    respuesta = messagebox.askquestion("CONFIRMACIÓN", "¿DESEAS ANALIZAR LOS DATOS LLENADOS?")
    if respuesta == "yes":
        ventanaprincipal = "ventana5"
        cambiarimagen()
        ventana4.withdraw()
        ventana5.deiconify()
        
        nombre = entry14.get().strip()
        apellido = entry15.get().strip()
        edad = int(entry16.get().strip())
        hemoglobina = float(entry3.get().strip())
        plaquetas = float(entry4.get().strip())
        bilirrubina = float(entry5.get().strip())
        globulosrojos = float(entry6.get().strip())
        globulosblancos = float(entry7.get().strip())
        glucosa = float(entry8.get().strip())
        creatinina = float(entry9.get().strip())
        colesterol = float(entry10.get().strip())
        sodio = float(entry11.get().strip())
        potasio = float(entry12.get().strip())
        calcio = float(entry13.get().strip())
        

        # Niños 1-12:
        if (edad >= 1 and edad <= 12) and (genero == "HOMBRE" or genero == "MUJER"):
            if hemoglobina < 11.5:
                estadohemoglobina = "DEFICIENTE"
            elif hemoglobina >= 11.5 and hemoglobina <= 14.5:
                estadohemoglobina = "NORMAL"
            else:
                estadohemoglobina = "EXCESO"
        
            if globulosblancos < 5000:
                estadoglobulosblancos = "DEFICIENTE"
            elif globulosblancos >= 5000 and globulosblancos <= 13000:
                estadoglobulosblancos = "NORMAL"
            else:
                estadoglobulosblancos = "EXCESO"
            
            if globulosrojos < 4100000:
                estadoglobulosrojos = "DEFICIENTE"
            elif globulosrojos >= 4100000 and globulosrojos <= 550000:
                estadoglobulosrojos = "NORMAL"
            else:
                estadoglobulosrojos = "EXCESO"
    
            if plaquetas < 150000:
                estadoplaquetas = "DEFICIENTE"
            elif plaquetas >= 150000 and plaquetas <= 450000:
                estadoplaquetas = "NORMAL"
            else:
                estadoplaquetas = "EXCESO"
        
            if glucosa < 70:
                estadoglucosa = "DEFICIENTE"
            elif glucosa >= 70 and glucosa <= 100:
                estadoglucosa = "NORMAL"
            else:
                estadoglucosa = "EXCESO"
        
            if creatinina < 0.3:
                estadocreatinina = "DEFICIENTE"
            elif creatinina >= 0.3 and creatinina <= 0.7:
                estadocreatinina = "NORMAL"
            else:
                estadocreatinina = "EXCESO"
        
            if bilirrubina < 0.2:
                estadobilirrubina = "DEFICIENTE"
            elif bilirrubina >= 0.2 and bilirrubina <= 1.0:
                estadobilirrubina = "NORMAL"
            else:
                estadobilirrubina = "EXCESO"
        
            if colesterol < 170:
                estadocolesterol = "NORMAL"
            else:
                estadocolesterol = "EXCESO"
            if sodio < 135:
                estadosodio = "DEFICIENTE"
            elif sodio >= 135 and sodio <= 145:
                estadosodio = "NORMAL"
            else:
                estadosodio = "EXCESO"
    
            if potasio < 3.5:
                estadopotasio = "DEFICIENTE"
            elif potasio >= 3.5 and potasio <= 5.5:
                estadopotasio = "NORMAL"
            else:
                estadopotasio = "EXCESO"
        
            if calcio < 9.0:
                estadocalcio = "DEFICIENTE"
            elif calcio >= 9.0 and calcio <= 11.0:
                estadocalcio = "NORMAL"
            else:
                estadocalcio = "EXCESO"
    

        # Adolescentes 13-18:
        if (edad >= 13 and edad <= 18) and (genero == "HOMBRE" or genero == "MUJER"):
            if genero == "HOMBRE":
                if globulosrojos < 4500000:
                    estadoglobulosrojos = "DEFICIENTE"
                elif globulosrojos >= 4500000 and globulosrojos <= 590000:
                    estadoglobulosrojos = "NORMAL"
                else:
                    estadoglobulosrojos = "EXCESO"
            elif genero == "MUJER":
                if globulosrojos < 4100000:
                    estadoglobulosrojos = "DEFICIENTE"
                elif globulosrojos >= 4100000 and globulosrojos <= 550000:
                    estadoglobulosrojos = "NORMAL"
                else:
                    estadoglobulosrojos = "EXCESO"
            
            if hemoglobina < 12.0:
                estadohemoglobina = "DEFICIENTE"
            elif hemoglobina >= 12.0 and hemoglobina <= 16.0:
                estadohemoglobina = "NORMAL"
            else:
                estadohemoglobina = "EXCESO"
                
            if globulosblancos < 4500:
                estadoglobulosblancos = "DEFICIENTE"
            elif globulosblancos >= 4500 and globulosblancos <= 11000:
                estadoglobulosblancos = "NORMAL"
            else:
                estadoglobulosblancos = "EXCESO"
    
            if plaquetas < 150000:
                estadoplaquetas = "DEFICIENTE"
            elif plaquetas >= 150000 and plaquetas <= 450000:
                estadoplaquetas = "NORMAL"
            else:
                estadoplaquetas = "EXCESO"
        
            if glucosa < 70:
                estadoglucosa = "DEFICIENTE"
            elif glucosa >= 70 and glucosa <= 100:
                estadoglucosa = "NORMAL"
            else:
                estadoplaquetas = "EXCESO"
        
            if creatinina < 0.5:
                estadocreatinina = "DEFICIENTE"
            elif creatinina >= 0.5 and creatinina <= 1.0:
                estadocreatinina = "NORMAL"
            else:
                estadocreatinina = "EXCESO"
        
            if bilirrubina < 0.1:
                estadobilirrubina = "DEFICIENTE"
            elif bilirrubina >= 0.1 and bilirrubina <= 1.2:
                estadobilirrubina = "NORMAL"
            else:
                estadobilirrubina = "EXCESO"
        
            if colesterol < 170:
                estadocolesterol = "NORMAL"
            else:
                estadocolesterol = "EXCESO"
        
            if sodio < 135:
                estadosodio = "DEFICIENTE"
            elif sodio >= 135 and sodio <= 145:
                estadosodio = "NORMAL"
            else:
                estadosodio = "EXCESO"
    
            if potasio < 3.5:
                estadopotasio = "DEFICIENTE"
            elif potasio >= 3.5 and potasio <= 5.0:
                estadopotasio = "NORMAL"
            else:
                estadopotasio = "EXCESO"
        
            if calcio < 9.0:
                estadocalcio = "DEFICIENTE"
            elif calcio >= 9.0 and calcio <= 10.5:
                estadocalcio = "NORMAL"
            else:
                estadocalcio = "EXCESO"
    
        # Adultos 18-65:
        if (edad >= 18 and edad <= 65) and (genero == "HOMBRE" or genero == "MUJER"):
            if genero == "HOMBRE":
                if hemoglobina < 13.8:
                    estadohemoglobina = "DEFICIENTE"
                elif hemoglobina >= 13.8 and hemoglobina <= 17.2:
                    estadohemoglobina = "NORMAL"
                else:
                    estadohemoglobina = "EXCESO"
                    
                if globulosrojos < 4700000:
                    estadoglobulosrojos = "DEFICIENTE"
                elif globulosrojos >= 4700000 and globulosrojos <= 610000:
                    estadoglobulosrojos = "NORMAL"
                else:
                    estadoglobulosrojos = "EXCESO"
                    
            elif genero == "MUJER":
                if hemoglobina < 12.1:
                    estadohemoglobina = "DEFICIENTE"
                elif hemoglobina >= 12.1 and hemoglobina <= 15.1:
                    estadohemoglobina = "NORMAL"
                else:
                    estadohemoglobina = "EXCESO"
                    
                if globulosrojos < 4200000:
                    estadoglobulosrojos = "DEFICIENTE"
                elif globulosrojos >= 4200000 and globulosrojos <= 540000:
                    estadoglobulosrojos = "NORMAL"
                else:
                    estadoglobulosrojos = "EXCESO"
        
            if globulosblancos < 4500:
                estadoglobulosblancos = "DEFICIENTE"
            elif globulosblancos >= 4500 and globulosblancos <= 11000:
                estadoglobulosblancos = "NORMAL"
            else:
                estadoglobulosblancos = "EXCESO"
    
            if plaquetas < 150000:
                estadoplaquetas = "DEFICIENTE"
            elif plaquetas >= 150000 and plaquetas <= 400000:
                estadoplaquetas = "NORMAL"
            else:
                estadoplaquetas = "EXCESO"
        
            if glucosa < 70:
                estadoglucosa = "DEFICIENTE"
            elif glucosa >= 70 and glucosa <= 100:
                estadoglucosa = "NORMAL"
            else:
                estadoglucosa = "EXCESO"
        
            if genero == "HOMBRE":
                if creatinina < 0.7:
                    estadocreatinina = "DEFICIENTE"
                elif creatinina >= 0.7 and creatinina <= 1.3:
                    estadocreatinina = "NORMAL"
                else:
                    estadocreatinina = "EXCESO"
        
            elif genero == "MUJER":
                if creatinina < 0.5:
                    estadocreatinina = "DEFICIENTE"
                elif creatinina >= 0.5 and creatinina <= 1.1:
                    estadocreatinina = "NORMAL"
                else:
                    estadocreatinina = "EXCESO"
        
            if bilirrubina < 0.1:
                estadobilirrubina = "DEFICIENTE"
            elif bilirrubina >= 0.1 and bilirrubina <= 1.2:
                estadobilirrubina = "NORMAL"
            else:
                estadobilirrubina = "EXCESO"
        
            if colesterol < 200:
                estadocolesterol = "NORMAL"
            else:
                estadocolesterol = "EXCESO"
        
            if sodio < 135:
                estadosodio = "DEFICIENTE"
            elif sodio >= 135 and sodio <= 145:
                estadosodio = "NORMAL"
            else:
                estadosodio = "EXCESO"
    
            if potasio < 3.5:
                estadopotasio = "DEFICIENTE"
            elif potasio >= 3.5 and potasio <= 5.0:
                estadopotasio = "NORMAL"
            else:
                estadopotasio = "EXCESO"
        
            if calcio < 8.5:
                estadocalcio = "DEFICIENTE"
            elif calcio >= 8.5 and calcio <= 10.5:
                estadocalcio = "NORMAL"
            else:
                estadocalcio = "EXCESO"
        
        
        # Adultos Mayores > 65:
        if (edad > 65) and (genero == "HOMBRE" or genero == "MUJER"):
            if genero == "HOMBRE":
                if hemoglobina < 12.6:
                    estadohemoglobina = "DEFICIENTE"
                elif hemoglobina >= 12.6 and hemoglobina <= 15.0:
                    estadohemoglobina = "NORMAL"
                else:
                    estadohemoglobina = "EXCESO"
                
                if globulosrojos < 4000000:
                    estadoglobulosrojos = "DEFICIENTE"
                elif globulosrojos >= 4000000 and globulosrojos <= 560000:
                    estadoglobulosrojos = "NORMAL"
                else:
                    estadoglobulosrojos = "EXCESO"
                    
            elif genero == "MUJER":
                if hemoglobina < 11.5:
                    estadohemoglobina = "DEFICIENTE"
                elif hemoglobina >= 11.5 and hemoglobina <= 14.5:
                    estadohemoglobina = "NORMAL"
                else:
                    estadohemoglobina = "EXCESO"
                    
                if globulosrojos < 3800000:
                    estadoglobulosrojos = "DEFICIENTE"
                elif globulosrojos >= 3800000 and globulosrojos <= 520000:
                    estadoglobulosrojos = "NORMAL"
                else:
                    estadoglobulosrojos = "EXCESO"
        
            if globulosblancos < 3800:
                estadoglobulosblancos = "DEFICIENTE"  
            elif globulosblancos >= 3800 and globulosblancos <= 10500:
                estadoglobulosblancos = "NORMAL"
            else:
                estadoglobulosblancos = "EXCESO"
    
            if plaquetas < 140000:
                estadoplaquetas = "DEFICIENTE"
            elif plaquetas >= 140000 and plaquetas <= 400000:
                estadoplaquetas = "NORMAL"
            else:
                estadoplaquetas = "EXCESO"
        
            if glucosa < 70:
                estadoglucosa = "DEFICIENTE"
            elif glucosa >= 70 and glucosa <= 126:
                estadoglucosa = "NORMAL"
            else:
                estadoglucosa = "EXCESO"
        
            if creatinina < 0.6:
                estadocreatinina = "DEFICIENTE"
            elif creatinina >= 0.6 and creatinina <= 1.2:
                estadocreatinina = "NORMAL"
            else:
                estadocreatinina = "EXCESO"
        
            if bilirrubina < 0.1:
                estadobilirrubina = "DEFICIENTE"
            elif bilirrubina >= 0.1 and bilirrubina <= 1.2:
                estadobilirrubina = "NORMAL"
            else:
                estadobilirrubina = "EXCESO"
        
            if colesterol < 200:
                estadocolesterol = "NORMAL"
            else:
                estadocolesterol = "EXCESO"
        
            if sodio < 132:
                estadosodio = "DEFICIENTE"
            elif sodio >= 132 and sodio <= 145:
                estadosodio = "NORMAL"
            else:
                estadosodio = "EXCESO"
    
            if potasio < 3.5:
                estadopotasio = "DEFICIENTE"
            elif potasio >= 3.5 and potasio <= 5.0:
                estadopotasio = "NORMAL"
            else:
                estadopotasio = "EXCESO"
        
            if calcio < 8.5:
                estadocalcio = "DEFICIENTE"
            elif calcio >= 8.5 and calcio <= 10.2:
                estadocalcio = "NORMAL"
            else:
                estadocalcio = "EXCESO"
                
        text1.config(text=nombre)
        text2.config(text=apellido)
        text3.config(text=edad)
        text4.config(text=genero)
        text5.config(text=estadohemoglobina)
        text6.config(text=estadoplaquetas)
        text7.config(text=estadobilirrubina)
        text8.config(text=estadoglobulosrojos)
        text9.config(text=estadoglobulosblancos)
        text10.config(text=estadoglucosa)
        text11.config(text=estadocreatinina)
        text12.config(text=estadocolesterol)
        text13.config(text=estadosodio)
        text14.config(text=estadopotasio)
        text15.config(text=estadocalcio)

        
        
        
def irventana6():
    global ventanaprincipal
    respuesta = messagebox.askquestion("CONFIRMACIÓN", "¿DESEAS CONTINUAR A LA SIGUIENTE VENTANA?")
    if respuesta == "yes":
        ventanaprincipal = "ventana6"
        cambiarimagen()
        ventana5.withdraw()
        ventana6.deiconify()

def irventana7():
    global ventanaprincipal
    respuesta = messagebox.askquestion("CONFIRMACIÓN", "¿DESEAS CONTINUAR A LA SIGUIENTE VENTANA?")
    if respuesta == "yes":
        ventanaprincipal = "ventana7"
        cambiarimagen()
        ventana6.withdraw()
        ventana7.deiconify()

# Regresar Ventanas:

def regresarventana1():
    global ventanaprincipal
    respuesta = messagebox.askquestion("CONFIRMACIÓN", "¿DESEAS REGRESAR ATRÁS?")
    if respuesta == "yes":
        ventanaprincipal = "ventana1"
        cambiarimagen()
        ventana2.withdraw()
        ventana1.deiconify()

def regresarventana2():
    global ventanaprincipal
    respuesta = messagebox.askquestion("CONFIRMACIÓN", "¿DESEAS REGRESAR ATRÁS?")
    if respuesta == "yes":
        ventanaprincipal = "ventana2"
        cambiarimagen()
        ventana3.withdraw()
        ventana2.deiconify()

def regresarventana3():
    global ventanaprincipal
    respuesta = messagebox.askquestion("CONFIRMACIÓN", "¿DESEAS REGRESAR ATRÁS?")
    if respuesta == "yes":
        ventanaprincipal = "ventana3"
        cambiarimagen()
        ventana4.withdraw()
        ventana3.deiconify()
        
def regresarventana4():
    global ventanaprincipal
    respuesta = messagebox.askquestion("CONFIRMACIÓN", "¿DESEAS REGRESAR ATRÁS?")
    if respuesta == "yes":
        ventanaprincipal = "ventana4"
        cambiarimagen()
        ventana5.withdraw()
        ventana4.deiconify()
        
def regresarventana5():
    global ventanaprincipal
    respuesta = messagebox.askquestion("CONFIRMACIÓN", "¿DESEAS REGRESAR ATRÁS?")
    if respuesta == "yes":
        ventanaprincipal = "ventana5"
        cambiarimagen()
        ventana6.withdraw()
        ventana5.deiconify()

def regresarventana6():
    global ventanaprincipal
    respuesta = messagebox.askquestion("CONFIRMACIÓN", "¿DESEAS REGRESAR ATRÁS?")
    if respuesta == "yes":
        ventanaprincipal = "ventana6"
        cambiarimagen()
        ventana7.withdraw()
        ventana6.deiconify()

# Generar Datos Aleatorios:

def aleatorio():
    respuesta = messagebox.askquestion("CONFIRMACIÓN", "¿DESEAS GENERAR VALORES ALEATORIOS?")
    if respuesta == "yes":
        entry3.delete(0, tkinter.END)
        entry4.delete(0, tkinter.END)
        entry5.delete(0, tkinter.END)
        entry6.delete(0, tkinter.END)
        entry7.delete(0, tkinter.END)
        entry8.delete(0, tkinter.END)
        entry9.delete(0, tkinter.END)
        entry10.delete(0, tkinter.END)
        entry11.delete(0, tkinter.END)
        entry12.delete(0, tkinter.END)
        entry13.delete(0, tkinter.END)
        entry14.delete(0, tkinter.END)
        entry15.delete(0, tkinter.END)
        entry16.delete(0, tkinter.END)
        
        global nombres
        global apellidos
        
        edad = random.randint(1, 95)
        entry16.insert(tkinter.END, str(edad))
        
        nombre = random.choice(nombres)
        entry14.insert(tkinter.END, str(nombre))
        
        apellido = random.choice(apellidos)
        entry15.insert(tkinter.END, str(apellido))
        
        hemoglobina = random.uniform(5.0, 20.0)
        hemoglobinar = round(hemoglobina, 2)
        entry3.insert(tkinter.END, str(hemoglobinar))
        
        globulosrojos = random.randint(3500000, 6500000)
        entry6.insert(tkinter.END, str(globulosrojos))
        
        globulosblancos = random.randint(3000, 15000)
        entry7.insert(tkinter.END, str(globulosblancos))
        
        plaquetas = random.randint(120000, 500000)
        entry4.insert(tkinter.END, str(plaquetas))
        
        glucosa = random.randint(50, 140)
        entry8.insert(tkinter.END, str(glucosa))
        
        creatinina = random.uniform(0, 1.7)
        creatininar = round(creatinina, 2)
        entry9.insert(tkinter.END, str(creatininar))
        
        colesterol = random.randint(80, 270)
        entry10.insert(tkinter.END, str(colesterol))
        
        sodio = random.randint(100, 170)
        entry11.insert(tkinter.END, str(sodio))
        
        potasio = random.uniform(2.5, 6.5)
        potasior = round(potasio, 2)
        entry12.insert(tkinter.END, str(potasior))
        
        calcio = random.uniform(7.0, 12.5)
        calcior = round(calcio, 2)
        entry13.insert(tkinter.END, str(calcior))
        
        bilirrubina = random.uniform(0, 1.8)
        bilirrubinar = round(bilirrubina, 2)
        entry5.insert(tkinter.END, str(bilirrubinar))

# GENEROS:

def masculino():
    global genero
    messagebox.showwarning("ADVERTENCIA", "ACABAS DE ELEGIR EL GÉNERO MASCULINO")
    genero = "HOMBRE"

def femenino():
    global genero
    messagebox.showwarning("ADVERTENCIA", "ACABAS DE ELEGIR EL GÉNERO FEMENINO")
    genero = "MUJER"

# DEFINICIONES:

def definicion1():
    messagebox.showinfo("¿SABIAS QUÉ?",
                        "LA HEMOGLOBINA ES UNA PROTEÍNA EN LOS GLÓBULOS ROJOS QUE TRANSPORTA OXÍGENO DESDE LOS PULMONOS HACIA LOS TEJIDOS Y DIÓXIDO DE CARBONO DESDE LOS TEJIDOS HACIA LOS PULMONES.")

def definicion2():
    messagebox.showinfo("¿SABIAS QUÉ?",
                        "LAS PLAQUETAS SON FRAGMENTOS CELULARES QUE PARTICIPAN EN LA COAGULACIÓN DE LA SANGRE, AYUDANDO A DETENER EL SANGRADO CUANDO OCURRE UNA LESIÓN.")

def definicion3():
    messagebox.showinfo("¿SABIAS QUÉ?",
                        "LA BILIRRUBINA ES UN PIGMENTO AMARRILLO PRODUCIDO DURANTE LA DESCOMPOSICIÓN DE LA HEMOGLOBINA DE LOS GLÓBULOS ROJOS VIEJOS.")

def definicion4():
    messagebox.showinfo("¿SABIAS QUÉ?",
                        "LOS GLÓBULOS ROJOS SON CÉLULAS SANGUÍNEAS RESPONSABLES DE TRANSPORTAR OXÍGENO A LOS TEJIDOS DEL CUERPO Y ELIMINAR DIÓXIDO DE CARBONO.")
    
def definicion5():
    messagebox.showinfo("¿SABIAS QUÉ?",
                        "LOS GLÓBULOS BLANCOS SON CÉLULAS DEL SISTEMA INMUNOLÓGICO QUE PROTEGEN AL CUERPO CONTRA INFECCIONES Y AYUDAN EN LA DEFENSA CONTRA AGENTES EXTRAÑOS.")

def definicion6():
    messagebox.showinfo("¿SABIAS QUÉ?",
                        "LA GLUCOSA ES EL AZUCAR PRESENTE EN LA SANGRE, FUNDAMENTAL PARA PROPORCIONAR ENERGÍA AL CUERPO.")

def definicion7():
    messagebox.showinfo("¿SABIAS QUÉ?",
                        "LA CREATININA ES UN DESECHO PRODUCIDO POR LOS MÚSCULOS, MEDIDO PARA EVALUAR LA FUNCIÓN RENAL.")

def definicion8():
    messagebox.showinfo("¿SABIAS QUÉ?",
                        "EL COLESTEROL ES UNA SUSTANCIA GRASA NECESARIA PARA ALGUNAS FUNCIONES DEL CUERPO, PERO SU EXCESO PUEDE CAUSAR PROBLEMAS CARDIOVASCULARES.")
    
def definicion9():
    messagebox.showinfo("¿SABIAS QUÉ?",
                        "LOS ELECTROLITOS DE SODIO SON MINERALES ESENCIALES PARA EL EQUILIBRIO DE LÍQUIDOS Y FUNCIONES MUSCULARES/NEUROLÓGICAS.")

def definicion10():
    messagebox.showinfo("¿SABIAS QUÉ?",
                        "LOS ELECTROLITOS DE POTASIO SON IMPORTANTES PARA LA FUNCIÓN MUSCULAR, CARDIACA Y EL EQUILIBRIO ELECTROLÍTICO.")

def definicion11():
    messagebox.showinfo("¿SABIAS QUÉ?",
                        "LOS ELECTROLITOS DE CALCIO SON IMPORTANTES PARA LAS FUNCIONES MUSCULARES, CARDIOVASCULARES, SEAS Y SANGUÍNEAS.")
             
             
pacientes_guardados = []

pacientes = []  

def guardar_datos_paciente():
    global paciente_contador
    global nombre, apellido, edad, genero, hemoglobina, plaquetas, bilirrubina, globulosrojos, globulosblancos, glucosa, creatinina, colesterol, sodio, potasio, calcio
    global estadohemoglobina, estadoplaquetas, estadobilirrubina, estadoglobulosrojos, estadoglobulosblancos, estadoglucosa, estadocreatinina, estadocolesterol, estadosodio, estadopotasio, estadocalcio

   
    paciente_contador += 1

   
    datos_paciente = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Edad": edad,
        "Género": genero,
        "Datos Médicos": {
            "Hemoglobina": (hemoglobina, estadohemoglobina),
            "Plaquetas": (plaquetas, estadoplaquetas),
            "Bilirrubina": (bilirrubina, estadobilirrubina),
            "Glóbulos Rojos": (globulosrojos, estadoglobulosrojos),
            "Glóbulos Blancos": (globulosblancos, estadoglobulosblancos),
            "Glucosa": (glucosa, estadoglucosa),
            "Creatinina": (creatinina, estadocreatinina),
            "Colesterol": (colesterol, estadocolesterol),
            "Sodio": (sodio, estadosodio),
            "Potasio": (potasio, estadopotasio),
            "Calcio": (calcio, estadocalcio),
        }
    }

    pacientes.append(datos_paciente)  
    messagebox.showinfo("Guardado", f"Paciente {paciente_contador} guardado.")
    
    

def agregar_nuevo_paciente():
    respuesta = messagebox.askquestion("Nuevo Paciente", "¿Deseas agregar un nuevo paciente?")
    if respuesta == "yes":
        entry3.delete(0, tkinter.END)
        entry4.delete(0, tkinter.END)
        entry5.delete(0, tkinter.END)
        entry6.delete(0, tkinter.END)
        entry7.delete(0, tkinter.END)
        entry8.delete(0, tkinter.END)
        entry9.delete(0, tkinter.END)
        entry10.delete(0, tkinter.END)
        entry11.delete(0, tkinter.END)
        entry12.delete(0, tkinter.END)
        entry13.delete(0, tkinter.END)
        entry14.delete(0, tkinter.END)
        entry15.delete(0, tkinter.END)
        entry16.delete(0, tkinter.END)
        ventana7.withdraw()
        ventana2.deiconify()
        messagebox.showinfo("Nuevo Paciente", "Listo para registrar un nuevo paciente.")
        
def exportar():
    if not pacientes:
        messagebox.showerror("Error", "No hay pacientes registrados para exportar.")
        return

    respuesta = messagebox.askquestion("Exportar", "¿Deseas exportar los datos de todos los pacientes en formato CSV?")
    if respuesta == "yes":
        with open("datos_pacientes.csv", mode="w", newline='') as archivo_csv:
            escritor = csv.writer(archivo_csv, delimiter=" ")
            escritor.writerow(["-------- DATOS ANALIZADOS --------"]) 

            for i, paciente in enumerate(pacientes, 1):
                escritor.writerow([f"Paciente {i}"])
                escritor.writerow(["Nombre:", paciente["Nombre"]])
                escritor.writerow(["Apellido:", paciente["Apellido"]])
                escritor.writerow(["Edad:", paciente["Edad"]])
                escritor.writerow(["Género:", paciente["Género"]])
                escritor.writerow(["-------- Datos Médicos --------"])

                for key, value in paciente["Datos Médicos"].items():
                    escritor.writerow([f"{key}:", value[0]])
                    escritor.writerow([f"Estado {key}:", value[1]])

                escritor.writerow([]) 
                escritor.writerow(["-------- FIN DE PACIENTE --------"])
                escritor.writerow([])

            escritor.writerow(["-------- ANÁLISIS COMPLETO --------"]) 

        subprocess.run(["notepad", "datos_pacientes.csv"], shell=True)


# Ventana 1:

ventana1 = tkinter.Tk()
ventana1.geometry("1280x720")
ventana1.title("BIOPY")
ventana1.resizable(0, 0)

labelinicio = tkinter.Label(ventana1)
labelinicio.pack()

label1 = tkinter.Label(ventana1)
label1.pack()

entry1 = tkinter.Entry(font=("Comic Sans MS", 16))
entry1.place(x=130, y=370)

entry2 = tkinter.Entry(font=("Comic Sans MS", 16), show="*")  # Contraseña
entry2.place(x=130, y=525)

boton1 = tkinter.Button(ventana1, text="INICIAR",font=("Comic Sans MS", 8), height=3, width=17, command=irventana2)
boton1.place(x=1100, y=620)

# Ventana 2:

ventana2 = tkinter.Toplevel(ventana1)
ventana2.geometry("1280x720")
ventana2.title("BIOPY - DATOS PERSONALES")
ventana2.resizable(0, 0)

labelventana2 = tkinter.Label(ventana2)
labelventana2.pack()

boton18 = tkinter.Button(ventana2, text="REGRESAR", font=("Comic Sans MS", 8), height=2, width=15, command=regresarventana1)
boton18.place(x=130, y=620)

boton19 = tkinter.Button(ventana2, text="SIGUIENTE", font=("Comic Sans MS", 8), height=2, width=15, command=irventana3)
boton19.place(x=1100, y=620)

boton25 = tkinter.Button(ventana2, text="MASCULINO", font=("Comic Sans MS", 8), height=2, width=15, command=masculino)
boton25.place(x=792, y=525)

boton26 = tkinter.Button(ventana2, text="FEMENINO", font=("Comic Sans MS", 8), height=2, width=15, command=femenino)
boton26.place(x=940, y=525)

entry14 = tkinter.Entry(ventana2, font=("Comic Sans MS", 16))
entry14.place(x=306, y=373)

entry15 = tkinter.Entry(ventana2, font=("Comic Sans MS", 16))
entry15.place(x=792, y=373)

entry16 = tkinter.Entry(ventana2, font=("Comic Sans MS", 16))
entry16.place(x=306, y=525)

ventana2.withdraw()

# Ventana 3:

ventana3 = tkinter.Toplevel(ventana2)
ventana3.geometry("1280x720")
ventana3.title("BIOPY - DATOS HEMATOLÓGICOS")
ventana3.resizable(0, 0)

labelventana3 = tkinter.Label(ventana3)
labelventana3.pack()

entry3 = tkinter.Entry(ventana3, font=("Comic Sans MS", 16))
entry3.place(x=178, y=370)

boton8 = tkinter.Button(ventana3, text="?", height=1, width=2, command=definicion1)
boton8.place(x=465, y=315)

entry4 = tkinter.Entry(ventana3, font=("Comic Sans MS", 16))
entry4.place(x=558, y=370)

boton9 = tkinter.Button(ventana3, text="?", height=1, width=2, command=definicion2)
boton9.place(x=817, y=315)

entry5 = tkinter.Entry(ventana3, font=("Comic Sans MS", 16))
entry5.place(x=918, y=370)

boton0 = tkinter.Button(ventana3, text="?", height=1, width=2, command=definicion3)
boton0.place(x=1183, y=315)

entry6 = tkinter.Entry(ventana3, font=("Comic Sans MS", 16))
entry6.place(x=260, y=537)

boton10 = tkinter.Button(ventana3, text="?", height=1, width=2, command=definicion4)
boton10.place(x=574, y=481)

entry7 = tkinter.Entry(ventana3, font=("Comic Sans MS", 16))
entry7.place(x=795, y=537)

boton11 = tkinter.Button(ventana3, text="?", height=1, width=2, command=definicion5)
boton11.place(x=1134, y=481)

boton2 = tkinter.Button(ventana3, text="REGRESAR", font=("Comic Sans MS", 8), height=2, width=15, command=regresarventana2)
boton2.place(x=130, y=620)

boton3 = tkinter.Button(ventana3, text="SIGUIENTE", font=("Comic Sans MS", 8), height=2, width=15, command=irventana4)
boton3.place(x=1100, y=620)

boton6 = tkinter.Button(ventana3, text="DATOS RANDOM", font=("Comic Sans MS", 8),  height=2, width=15, command=aleatorio)
boton6.place(x=620, y=620)

ventana3.withdraw()

# Ventana 4:

ventana4 = tkinter.Toplevel(ventana3)
ventana4.geometry("1280x720")
ventana4.title("BIOPY - DATOS BIOQUÍMICOS")
ventana4.resizable(0, 0)

labelventana4 = tkinter.Label(ventana4)
labelventana4.pack()

entry8 = tkinter.Entry(ventana4, font=("Comic Sans MS", 16))
entry8.place(x=185, y=370)

boton12 = tkinter.Button(ventana4, text="?", height=1, width=2, command=definicion6)
boton12.place(x=422, y=314)

entry9 = tkinter.Entry(ventana4, font=("Comic Sans MS", 16))
entry9.place(x=536, y=370)

boton13 = tkinter.Button(ventana4, text="?", height=1, width=2, command=definicion7)
boton13.place(x=794, y=314)

entry10 = tkinter.Entry(ventana4, font=("Comic Sans MS", 16))
entry10.place(x=886, y=370)

boton14 = tkinter.Button(ventana4, text="?", height=1, width=2, command=definicion8)
boton14.place(x=1153, y=314)

entry11 = tkinter.Entry(ventana4, font=("Comic Sans MS", 16))
entry11.place(x=195, y=555)

boton15 = tkinter.Button(ventana4, text="?", height=1, width=2, command=definicion9)
boton15.place(x=436, y=500)

entry12 = tkinter.Entry(ventana4, font=("Comic Sans MS", 16))
entry12.place(x=542, y=555)

boton16 = tkinter.Button(ventana4, text="?", height=1, width=2, command=definicion10)
boton16.place(x=800, y=500)

entry13 = tkinter.Entry(ventana4, font=("Comic Sans MS", 16))
entry13.place(x=892, y=555)

boton17 = tkinter.Button(ventana4, text="?", height=1, width=2, command=definicion11)
boton17.place(x=1140, y=500)

boton4 = tkinter.Button(ventana4, text="REGRESAR", font=("Comic Sans MS", 8), height=2, width=15, command=regresarventana3)
boton4.place(x=130, y=620)

boton5 = tkinter.Button(ventana4, text="ANALIZAR DATOS", font=("Comic Sans MS", 8), height=2, width=15, command=analisisdatos)
boton5.place(x=1100, y=620)



ventana4.withdraw()

# Ventana 5:

ventana5 = tkinter.Toplevel(ventana4)
ventana5.geometry("1280x720")
ventana5.title("BIOPY - RESULTADOS DEL ANÁLISIS")
ventana5.resizable(0, 0)

labelventana5 = tkinter.Label(ventana5)
labelventana5.pack()

text1 = tkinter.Label(ventana5, font=("Comic Sans MS", 16))
text1.place(x=306, y=373)


text2 = tkinter.Label(ventana5, font=("Comic Sans MS", 16))
text2.place(x=792, y=373)

text3 = tkinter.Label(ventana5, font=("Comic Sans MS", 16))
text3.place(x=306, y=525)

text4 = tkinter.Label(ventana5, font=("Comic Sans MS", 16))
text4.place(x=792, y=525)

boton20 = tkinter.Button(ventana5, text="REGRESAR", font=("Comic Sans MS", 8), height=2, width=15, command=regresarventana4)
boton20.place(x=130, y=620)

boton21 = tkinter.Button(ventana5, text="SIGUIENTE", font=("Comic Sans MS", 8), height=2, width=15, command=irventana6)
boton21.place(x=1100, y=620)

ventana5.withdraw()


# Ventana 6:

ventana6 = tkinter.Toplevel(ventana5)
ventana6.geometry("1280x720")
ventana6.title("BIOPY - RESULTADOS DEL ANÁLISIS")
ventana6.resizable(0, 0)

labelventana6 = tkinter.Label(ventana6)
labelventana6.pack()

text5 = tkinter.Label(ventana6, font=("Comic Sans MS", 16))
text5.place(x=178, y=370)

text6 = tkinter.Label(ventana6, font=("Comic Sans MS", 16))
text6.place(x=558, y=370)

text7 = tkinter.Label(ventana6, font=("Comic Sans MS", 16))
text7.place(x=918, y=370)

text8 = tkinter.Label(ventana6, font=("Comic Sans MS", 16))
text8.place(x=260, y=537)

text9 = tkinter.Label(ventana6, font=("Comic Sans MS", 16))
text9.place(x=795, y=537)

boton22 = tkinter.Button(ventana6, text="REGRESAR", font=("Comic Sans MS", 8), height=2, width=15, command=regresarventana5)
boton22.place(x=130, y=620)

boton23 = tkinter.Button(ventana6, text="SIGUIENTE", font=("Comic Sans MS", 8), height=2, width=15, command=irventana7)
boton23.place(x=1100, y=620)


ventana6.withdraw()

# Ventana 7:

ventana7 = tkinter.Toplevel(ventana6)
ventana7.geometry("1280x720")
ventana7.title("BIOPY - RESULTADOS DEL ANÁLISIS")
ventana7.resizable(0, 0)

labelventana7 = tkinter.Label(ventana7)
labelventana7.pack()

text10 = tkinter.Label(ventana7, font=("Comic Sans MS", 16))
text10.place(x=185, y=370)

text11 = tkinter.Label(ventana7, font=("Comic Sans MS", 16))
text11.place(x=536, y=370)

text12 = tkinter.Label(ventana7, font=("Comic Sans MS", 16))
text12.place(x=886, y=370)

text13 = tkinter.Label(ventana7, font=("Comic Sans MS", 16))
text13.place(x=195, y=555)

text14 = tkinter.Label(ventana7, font=("Comic Sans MS", 16))
text14.place(x=542, y=555)

text15 = tkinter.Label(ventana7, font=("Comic Sans MS", 16))
text15.place(x=892, y=555)

boton24 = tkinter.Button(ventana7, text="REGRESAR", font=("Comic Sans MS", 8), height=2, width=15, command=regresarventana6)
boton24.place(x=130, y=620)

boton25 = tkinter.Button(ventana7, text="EXPORTAR", font=("Comic Sans MS", 8), height=2, width=15, command=exportar)
boton25.place(x=1100, y=620)

# Botón para guardar datos del paciente
boton_guardar = tkinter.Button(
    ventana7, 
    text="Guardar Datos", 
    font=("Comic Sans MS", 8), 
    height=2, 
    width=15, 
    command=guardar_datos_paciente
)
boton_guardar.place(x=494, y=620)

# Botón para ingresar un nuevo perfil
boton_nuevo = tkinter.Button(
    ventana7, 
    text="Ingresar Nuevo Perfil", 
    font=("Comic Sans MS", 8), 
    height=2, 
    width=20, 
    command=agregar_nuevo_paciente
)
boton_nuevo.place(x=727, y=620)


ventana7.withdraw()

cambiarimagen()
ventana1.mainloop()


        
