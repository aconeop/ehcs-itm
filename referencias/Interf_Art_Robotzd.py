from tkinter import *

raiz = Tk()

raiz.title("ARTICULACION ROBOTIZADA")
#imagenL=PhotoImage(file="")
#raiz.resizable(ancho,alto)
#raiz.resizable(0,0)

raiz.iconbitmap("sinfin.ico")
#miframe=Frame(raiz,width=1200,height=600)
#miframe.pack()
raiz.geometry("670x400")



Titulo=Label(raiz,text="ARTICULACION ROBOTIZADA",font=("Castellar",18))
Titulo.pack(side="top")



Velocidad=Label(raiz,text="VELOCIDAD:",font=("Arial black",12))
Velocidad.place(x=380,y=150)
txt=Entry(raiz)
txt.place(x=500,y=155)


Sentido=Label(raiz,text="SENTIDO DEL MOTOR:",font=("Arial black",12))
Sentido.place(x=330,y=220)


#ImgBoton=PhotoImage(file="horario1.ico")
#boton1=Button(raiz,image=ImgBoton,height=80,width=100)

boton1=Button(raiz,text="HORARIO",font=("Arial black",9),bg="blue")
boton1.place(x=540,y=220)

boton2=Button(raiz,text="ANTI HORARIO",font=("Arial black",9),bg="red")
boton2.place(x=540,y=250)

Grados=Label(raiz,text="GRADOS°:",font=("Arial black",12))
Grados.place(x=20,y=150)
txt=Entry(raiz)
txt.place(x=120,y=155)

Posicion=Label(raiz,text="POSICION ACTUAL:",font=("Arial black",12))
Posicion.place(x=20,y=220)
txt=Entry(raiz)
txt.place(x=25,y=260)

botonPosicion=Button(raiz,text="MOSTRAR",font=("Arial black",9))
botonPosicion.place(x=40,y=285)

raiz.mainloop()

