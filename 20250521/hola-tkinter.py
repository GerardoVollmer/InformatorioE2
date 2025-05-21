import tkinter as tk

def saludar():
    print("¡Hola, mundo!")
# Crear la ventana principal

#clase(molde, formato) ==instanciar/crear==> objeto
#clases: tienen atriibutos funciones y metodos

ventana = tk.Tk()
ventana.title("Mi primer ventana Tkinter")
ventana.geometry("900x600")

texto = tk.Label(ventana, text="¡Hola, mundo!", font=("Arial", 48), fg="blue")
texto.pack()

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()
# Crear la ventana principal

ventana.mainloop()