from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import time


def init_window():
    window = Tk()

    window.title("My fist app")

    window.geometry("600x400")

    window.config(background="red")


    messagebox.showinfo("Info","en la siguiente app podra realizar calculos simples,  recuerde  no dividir por cero")

    def explode():
        label.config(text="ERROR",font=("Italic bold", 125))
        boton_r.grid(column=0,row=1)
        label_entrada1.config(text="",background="black")
        label_entrada1.config(text="",background="black")
        label_entrada2.config(text="",background="black")
        label_entrada2.config(text="",background="black")
        label_resultado.config(text="",background="black")
        label_operador.config(text="",background="black")
        label_bg.config(text="",background="black")
        espacio.config(background="black")
        espacio1.config(background="black")

        window.config(background="black")

        window.config(background="red")

        window.config(background="white")

        window.config(background="black")





    label = Label(window,text="Epic Hot Calulatoronix ",font=("Italic bold",20))
    label.grid(column=0,row=0)

    entrada1 = Spinbox(window, from_=0, to=100, width=5)
    entrada2 = Spinbox(window, from_=0, to=100, width=5)



    entrada1.grid(column=1,row=1)
    entrada2.grid(column=1,row=2)



    label_entrada1 = Label(window,text="Digit One",font=("Italic bold",10))
    label_entrada1.grid(column=0,row=1)

    label_entrada2 = Label(window,text="Digit Two",font=("Italic bold",10))
    label_entrada2.grid(column=0,row=2)

    label_operador = Label(window,text="Choose Operator",font=("Italic bold",10))
    label_operador.grid(column=0,row=3)

    label_bg = Label(window,text="Background",font=("Italic bold",10))
    label_bg.grid(column=0,row=5)

    combo_operadores= ttk.Combobox(window)
    combo_operadores["values"] = ["+","-","*","/","pow"]
    combo_operadores.current(0)
    combo_operadores.grid(column=1,row=3)
    combo_operadores.config(width="5")

    label_resultado = Label(window,text="Result",font=("Helvetica bold",10))
    label_resultado.grid(column=0,row=4)


    def calculator(num1, num2, operador):
        resultado = 0
        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            resultado = round(num1 / num2, 2)
        elif operador == "pow":
            resultado = num1 ** num2

        return resultado

    def click_calulator(label, num1, num2, operador):
        valor1 = float(num1)
        valor2 = float(num2)

        res = calculator(valor1, valor2, operador)
        label.configure(text="Epic Result Is:  " + str(res))

    boton = Button(window,command = lambda:click_calulator(label_resultado,entrada1.get(),entrada2.get(),combo_operadores.get()), text="Calculate")
    boton.grid(column = 1, row= 4)
    espacio1 = Label(text="", bg='red')
    espacio1.grid(column=1,row=7)
    boton_e = Button(window,command = lambda:explode(), text="EXPLODE!!!")
    boton_e.grid(column = 1, row= 8)
    boton_r = Button(window,command = lambda:init_window(), text="restart")
    boton_r.grid(column = 1, row= 9)

    def azul():
        window.config(background="blue")
        espacio.config(background="blue")
        espacio1.config(background="blue")
    rad1 = Radiobutton(window, text='Blue', value=1,command= lambda:azul())
    def verde():
        window.config(background="green")
        espacio.config(background="green")
        espacio1.config(background="green")
    rad2 = Radiobutton(window, text='Green', value=1,command= lambda:verde())
    def amarillo():
        window.config(background="yellow")
        espacio.config(background="yellow")
        espacio1.config(background="yellow")
    rad3 = Radiobutton(window, text='Yellow', value=1,command= lambda:amarillo())

    espacio = Label(text="",bg='red')

    rad1.grid(column=1, row=5)
    rad2.grid(column=2, row=5)
    espacio.grid(column=3,row=5)
    rad3.grid(column=4, row=5)



    window.mainloop()











def main():
    init_window()

main ()