anio_actual = 2025
mayoria_edad = 18

anio_nac = int(input("ingrese su año de nacimiento: "))

anio_usuario = anio_actual - anio_nac

if anio_usuario >= mayoria_edad:
    print("es mayor de edad")
else:
    print("es menor de edad")
