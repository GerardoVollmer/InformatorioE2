# EJERCICIO: Tenemos que ingresar por pantalla un string con la fecha en formato ISO por ejemplo:
# '20250505', identificar el mes en elque se encuentra en este caso .

# SOLUCIÓN:


#Trabajo 2 Ejercicio: Definir una lista de 1..1000 y determinen todos los numeros primos que aparecen
# entre el 1 y el 1000, y guardarlos en una lista llamada numeros_primos.

# SOLUCIÓN:
# Creo la funcion para veriicar si un numero es primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#genero la lista de numeros primos del 1 al 1000
numeros_primos = [num for num in range(1, 1001) if es_primo(num)]
print(numeros_primos) #imprimo la lista de numeros primos