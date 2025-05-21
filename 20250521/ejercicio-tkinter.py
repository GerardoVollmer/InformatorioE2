import tkinter as tk

import datetime

def mostrar_hora_actual():
    print(f"{datetime.datetime.now()}")

ventana = tk.Tk()
ventana.title(" Ventana con hora")
ventana.geometry("800x600")

texto = tk.Label(ventana, text="imprime la hs actual", font=("arial",35), fg="red")
texto.pack()

boton = tk.Button(ventana, text="Mostrar hora", command=mostrar_hora_actual)
boton.pack()

ventana.mainloop()
