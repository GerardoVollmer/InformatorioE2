# Selecciono el conetenido a comentar, ctrk + k + C
# Descomentar: el contenido seleccionado, ctrk + k + U

#variables enteras
int_1 = 5
int_2 = 2

#Operadores 

# suma
suma = int_1 + int_2
print(f"La suma entre {int_1} y {int_2} es: {suma}")

# resta
resta = int_1 - int_2
print(f"La resta entre {int_1} y {int_2} es: {resta}")

# multiplicacion
multiplicacion = int_1 * int_2
print(f"La multiplicacion entre {int_1} y {int_2} es: {multiplicacion}")

# Division
division = int_1 / int_2
print(f"La division entre {int_1} y {int_2} es: {division}")

# potencia
potencia = int_1 ** int_2
print(f"La potencia entre {int_1} y {int_2} es: {potencia}")

# Variables string
str_1 = "info"
str_2 = "rmatorio"

# # Operador
# Suma

suma = str_1 + str_2
print(f"La suma entre {str_1} y {str_2} es: {suma}") 

## Variables listas
lis_1 = [1, 2, 3,]
lis_2 = [4, 5, 6]  

# Operador
# Suma
suma = lis_1 + lis_2
print(f"La suma entre {lis_1} y {lis_2} es: {suma}")

# resta
resta = lis_1 - lis_2 # no se puede realizar la resta entre listas
print(f"La resta entre {lis_1} y {lis_2} es: {resta}") # no se puede realizar la resta entre listas

lista_desordenada = [93,1234124,421412,34123,12431,4]
# utilizamos .sort() para ordenar la lista
lista_desordenada = lista_desordenada.sort()

print(f"La lista desordenada es: {lista_desordenada}")

# otro ejemplo de lista
lista = [10,20,30,40,50] #para obtener el 3er elemento de la lista, se utiliza el indice 2 ya que 0 es el primer elemento
print(lista[-1]) # imprime el último elemento de la lista
print(lista[0]) # imprime el primer elemento de la lista

lista = ['Gerardo', 'juan', 'maria', 'pepe'] # lista de strings
lista.sort() # ordena la lista de strings
print(lista) # imprime la lista ordenada
lista.sort(reverse=True) # ordena la lista de strings en orden inverso
print(lista) # imprime la lista ordenada en orden inverso

tupla = ('Gerardo', 'juan', 'maria', 'pepe', 3, 1)
print(tupla) # imprime la tupla

diccionario = {39313433: "Gerardo Vollmer", 23313685: 'Lopez Isabel'}
print(diccionario) # imprime el diccionario
print(diccionario['39313433']) # imprime el valor asociado a la clave '39313433'

