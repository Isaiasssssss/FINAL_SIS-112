import tkinter
from tkinter import messagebox
import random

ventanaprincipal = "ventana1"

# Cambiar Imagen:

def cambiarimagen():
    global ventanaprincipal
    if ventanaprincipal == "ventana1":
        imagen1 = tkinter.PhotoImage(file="IBIO.png")
        labelinicio.config(image=imagen1)
        labelinicio.image = imagen1
    elif ventanaprincipal == "ventana2":
        imagen2 = tkinter.PhotoImage(file="DATOSH.png")
        labelventana2.config(image=imagen2)
        labelventana2.image = imagen2
    elif ventanaprincipal == "ventana3":
        imagen3 = tkinter.PhotoImage(file="DATOSB.png")
        labelventana3.config(image=imagen3)
        labelventana3.image = imagen3
        
# Ingresar a la Ventana 2:

def irventana2():
    global ventanaprincipal
    usuarioc = "Garecona"
    contraseñac = "1306"
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
        
# Retornar a la Ventana 1:

def regresarventana1():
    global ventanaprincipal
    respuesta = messagebox.askquestion("CONFIRMACIÓN", "¿DESEAS REGRESAR ATRÁS?")
    if respuesta == "yes":
        ventanaprincipal = "ventana1"
        cambiarimagen()
        ventana2.withdraw()
        ventana1.deiconify()

def irventana3():
    global ventanaprincipal
    respuesta = messagebox.askquestion("CONFIRMACIÓN", "¿DESEAS CONTINUAR A LA SIGUIENTE VENTANA?")
    if respuesta == "yes":
        ventanaprincipal = "ventana3"
        cambiarimagen()
        ventana2.withdraw()
        ventana3.deiconify()
        
def regresarventana2():
    global ventanaprincipal
    respuesta = messagebox.askquestion("CONFIRMACIÓN", "¿DESEAS REGRESAR ATRÁS?")
    if respuesta == "yes":
        ventanaprincipal = "ventana2"
        cambiarimagen()
        ventana3.withdraw()
        ventana2.deiconify()
        
        
# Generar Datos Aleatorios:

def aleatorio():
    respuesta = messagebox.askquestion("CONFIRMACIÓN", "¿DESEAS GENERAR VALORES ALEATORIOS?")
    if respuesta == "yes":
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

#  Eliminar Datos:

def eliminar():
    respuesta = messagebox.askquestion("CONFIRMACIÓN", "¿ESTÁ SEGURO DE ELIMINAR TODOS LOS DATOS?")
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

# Comparaciones:


    

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

entry2 = tkinter.Entry(font=("Comic Sans MS", 16))
entry2.place(x=130, y=525)

boton1 = tkinter.Button(ventana1, text="INICIAR",font=("Comic Sans MS", 8), height=3, width=17, command=irventana2)
boton1.place(x=1100, y=620)

# Ventana 2:

ventana2 = tkinter.Toplevel(ventana1)
ventana2.geometry("1280x720")
ventana2.title("BIOPY - DATOS HEMATOLÓGICOS")
ventana2.resizable(0, 0)

labelventana2 = tkinter.Label(ventana2)
labelventana2.pack()

entry3 = tkinter.Entry(ventana2, font=("Comic Sans MS", 16))
entry3.place(x=178, y=370)

entry4 = tkinter.Entry(ventana2, font=("Comic Sans MS", 16))
entry4.place(x=558, y=370)

entry5 = tkinter.Entry(ventana2, font=("Comic Sans MS", 16))
entry5.place(x=918, y=370)

entry6 = tkinter.Entry(ventana2, font=("Comic Sans MS", 16))
entry6.place(x=260, y=537)

entry7 = tkinter.Entry(ventana2, font=("Comic Sans MS", 16))
entry7.place(x=795, y=537)

boton2 = tkinter.Button(ventana2, text="REGRESAR", height=2, width=15, command=regresarventana1)
boton2.place(x=130, y=620)

boton3 = tkinter.Button(ventana2, text="SIGUIENTE", height=2, width=15, command=irventana3)
boton3.place(x=1100, y=620)

boton6 = tkinter.Button(ventana2, text="DATOS RANDOM", height=2, width=15, command=aleatorio)
boton6.place(x=620, y=620)

ventana2.withdraw()

# Ventana 3:

ventana3 = tkinter.Toplevel(ventana2)
ventana3.geometry("1280x720")
ventana3.title("BIOPY - DATOS BIOQUÍMICOS")
ventana3.resizable(0, 0)

labelventana3 = tkinter.Label(ventana3)
labelventana3.pack()

entry8 = tkinter.Entry(ventana3, font=("Comic Sans MS", 16))
entry8.place(x=185, y=370)

entry9 = tkinter.Entry(ventana3, font=("Comic Sans MS", 16))
entry9.place(x=536, y=370)

entry10 = tkinter.Entry(ventana3, font=("Comic Sans MS", 16))
entry10.place(x=886, y=370)

entry11 = tkinter.Entry(ventana3, font=("Comic Sans MS", 16))
entry11.place(x=195, y=555)

entry12 = tkinter.Entry(ventana3, font=("Comic Sans MS", 16))
entry12.place(x=542, y=555)

entry13 = tkinter.Entry(ventana3, font=("Comic Sans MS", 16))
entry13.place(x=892, y=555)

boton4 = tkinter.Button(ventana3, text="REGRESAR", height=2, width=15, command=regresarventana2)
boton4.place(x=130, y=620)

boton5 = tkinter.Button(ventana3, text="SIGUIENTE", height=2, width=15)
boton5.place(x=1100, y=620)

boton7 = tkinter.Button(ventana3, text="ELIMINAR", height=2, width=15, command=eliminar)
boton7.place(x=620, y=620)


ventana3.withdraw()

cambiarimagen()
ventana1.mainloop()