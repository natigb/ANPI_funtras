from tkinter import Tk, Text, Button, Label, Entry

class Interfaz:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title("Calculadora")
        Label(self.ventana, text="Basic Calculator").grid(row=0, column =1)

        Label(self.ventana, text="x = ").grid(row=1)
        entry_x = Entry(self.ventana, width = 100)
        entry_x.grid(row=1, column=1)
        Label(self.ventana, text="y = ").grid(row=2)
        entry_y = Entry(self.ventana, width = 100)
        entry_y.grid(row=2, column=1)

        #Agregar una caja de texto para que sea la pantalla de la calculadora
        self.pantalla=Text(ventana, state="disabled", width=40, height=3, background="black", foreground="white", font=("Helvetica",15))
        self.pantalla.grid(row=3, column=0, columnspan=3)

        botonhelp=self.createButton("HELP",escribir=False)
        botonclr=self.createButton("Clear All",escribir=False)

        boton1=self.createButton("senh(x)",escribir=False)
        boton2=self.createButton("cosh(x)",escribir=False)
        boton3=self.createButton("tanh(x)",escribir=False)
        boton4=self.createButton("asen(x)",escribir=False)
        boton5=self.createButton("acos(x)",escribir=False)
        boton6=self.createButton("atan(x)",escribir=False)
        boton7=self.createButton("sec(x)",escribir=False)
        boton8=self.createButton("csc(x)",escribir=False)
        boton9=self.createButton("cot(x)",escribir=False)
        boton10=self.createButton("sen(x)",escribir=False)
        boton11=self.createButton("cos(x)",escribir=False)
        boton12=self.createButton("tan(x)",escribir=False)
        boton13=self.createButton("ln(x)",escribir=False)
        boton14=self.createButton("log10(x)",escribir=False)
        boton15=self.createButton("logy(x)",escribir=False)
        boton16=self.createButton("1/x",escribir=False)
        boton17=self.createButton("sqrt(x)",escribir=False)
        boton18=self.createButton("y_root(x)",escribir=False)
        boton19=self.createButton("exp(x)",escribir=False)
        boton20=self.createButton("x^y",escribir=False)
        boton21=self.createButton("x!",escribir=False)
        boton22=self.createButton(7)
        boton23=self.createButton(8)
        boton24=self.createButton(9)
        boton25=self.createButton(4)
        boton26=self.createButton(5)
        boton27=self.createButton(6)
        boton28=self.createButton(1)
        boton29=self.createButton(2)
        boton30=self.createButton(3)
        boton31=self.createButton("pi")
        boton32=self.createButton(0)
        boton33=self.createButton(".")
        botones=[boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton10, boton11, 
                boton12, boton13, boton14, boton15, boton16, boton17, boton18, boton19, boton20, boton21, boton22,
                boton23, boton24, boton25, boton26, boton27, boton28, boton29, boton30, boton31, boton32, boton33
                ]
        counter=0
        for fila in range(4,14):
            for columna in range(3):
                botones[counter].grid(row=fila,column=columna)
                counter+=1
        #Ubicar el último botón al final
        botonhelp.grid(row=0,column=0)
        botonclr.grid(row=0,column=3)

        return

    def createButton(self,valor,escribir=True,ancho=9,alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica",15), command=lambda: self.click(valor,escribir))

ventana_principal=Tk()
calculadora=Interfaz(ventana_principal)
ventana_principal.mainloop()

#http://patriciaemiguel.com/python/tutoriales/2019/08/02/calculadora-python-tkinter.html