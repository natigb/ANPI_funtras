from tkinter import Radiobutton, Tk, Text, Button, Label, Entry, END, INSERT, StringVar, Toplevel
import funtras

class Interfaz:
    def __init__(self, ventana):
        self.selected_entry = StringVar()
        self.selected_entry.set("x")
        self.ventana=ventana
        self.ventana.title("Calculadora")
        Label(self.ventana, text="Basic Calculator").grid(row=0, column =1)

        Label(self.ventana, text="x = ").grid(row=1)
        self.entry_x = Entry(self.ventana, width = 18)
        self.entry_x.grid(row=1, column=1)
        self.rbx = Radiobutton(self.ventana, variable=self.selected_entry, value="x")
        self.rbx.grid(row=1, column=2)

        Label(self.ventana, text="y = ").grid(row=2)
        self.entry_y = Entry(self.ventana, width = 18)
        self.entry_y.grid(row=2, column=1)
        self.rby = Radiobutton(self.ventana, variable=self.selected_entry, value="y")
        self.rby.grid(row=2, column=2)
        #Agregar una caja de texto para que sea la pantalla de la calculadora
        self.pantalla=Text(ventana, state="disabled", width=27, height=3, background="black", foreground="white", font=("Helvetica",15))
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
                boton23, boton24, boton25, boton26, boton27, boton28, boton29, boton30, boton31, boton32, boton33]
        counter=0
        for fila in range(4,15):
            for columna in range(3):
                botones[counter].grid(row=fila,column=columna)
                counter+=1
        #Ubicar el último botón al final
        botonhelp.grid(row=0,column=0)
        botonclr.grid(row=0,column=2)

        return
    
    def createButton(self,valor,escribir=True,ancho=9,alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica",15), command=lambda: self.click(valor,escribir))

    def toFloat(self, text):
        try:
            float(text)
        except:
            return "err"
        return float(text)

    def mostrarEnEntry(self,input):
        
        if input == "pi":
            input = funtras.pi
        if self.selected_entry.get()=="x":
            self.entry_x.insert(self.entry_x.index(INSERT),input)
        if self.selected_entry.get()=="y":
            self.entry_y.insert(self.entry_y.index(INSERT),input)

    def mostrarEnPantalla(self,input):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state="disabled")

        self.pantalla.configure(state="normal")
        self.pantalla.insert(END, input)
        self.pantalla.configure(state="disabled")
        return

    def clearAll(self):
        self.entry_x.delete(0, END)
        self.entry_y.delete(0, END)
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state="disabled")

    def obtenerResultado(self,op,x,y):
        result = 0
        if op == "senh(x)":
            return funtras.sinh_t(x)
        if op == "cosh(x)":
            return funtras.cosh_t(x)
        if op == "tanh(x)":
            return funtras.tanh_t(x)
        if op == "asen(x)":
            return funtras.asin_t(x)
        if op == "acos(x)":
            return funtras.acos_t(x)
        if op == "atan(x)":
            return funtras.atan_t(x)
        if op == "sec(x)":
            return funtras.sec_t(x)
        if op == "csc(x)":
            return funtras.csc_t(x)
        if op == "cot(x)":
            return funtras.cot_t(x)
        if op == "sen(x)":
            return funtras.sin_t(x)
        if op == "cos(x)":
            return funtras.cos_t(x)
        if op == "tan(x)":
            return funtras.tan_t(x)
        if op == "ln(x)":
            return funtras.ln_t(x)
        if op == "log10(x)":
            return funtras.log_t(x,10)
        if op == "logy(x)":
            return funtras.log_t(x,y)
        if op == "1/x":
            return funtras.div_t(x)
        if op == "sqrt(x)":
            return funtras.sqrt_t(x)
        if op == "y_root(x)":
            return funtras.root_t(x,y)
        if op == "exp(x)":
            return funtras.exp_t(x)
        if op == "x^y":
            return funtras.power_t(x,y)
        if op == "x!":
            return funtras.fact(x)

        return result
    def operacion(self,input) :
        
        x=0
        y=0
        if self.entry_x.get()!="":
            x = self.toFloat(self.entry_x.get())
        if self.entry_y.get()!="":
            y = self.toFloat(self.entry_y.get())

        if x=="err" or y=="err":
            self.mostrarEnPantalla("err")
        else:
            self.mostrarEnPantalla(self.obtenerResultado(input,x,y))
            
        

    def help(self):
            
        newWindow = Toplevel(self.ventana)
        newWindow.title("HELP")
    
        newWindow.geometry("200x200")
        info = """
                Aqui va la explicacion 
                Calculadora creada por:
                    Natalia Gonzalez Bermudez
                    Karina
                    David
                """
        Label(newWindow,
            text = info).pack()

    def click(self,texto,escribir):
        if not escribir:
            #print(texto)
            if texto== "Clear All":
                self.clearAll()
            if texto == "HELP":
                self.help()
            else:
                self.operacion(texto)
        else:
            #self.input_x= self.input_x+str(texto)
            self.mostrarEnEntry(texto)
        return
    

ventana_principal=Tk()
calculadora=Interfaz(ventana_principal)
ventana_principal.mainloop()

#http://patriciaemiguel.com/python/tutoriales/2019/08/02/calculadora-python-tkinter.html