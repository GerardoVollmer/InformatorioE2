#el usuario ingresa por pantalla una serie de numeros
# se debe sumar entre si la cadena ingresada, entra 99,
# resultado 18. ingresa 999, resultado 27
#ingresa 101, el resultado es 2

numero = int(input('ingrese un numero: '))
suma = 0
while numero > 0:
    print(numero % 10)
    suma = suma + (numero % 10)
    numero = numero // 10
print(f'la suma de los digitos es: {suma}')
# el usuario ingresa por pantalla una serie de numeros
