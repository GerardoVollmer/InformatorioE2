# se ingresa por pantalla una cadena y se debe invertir
# cadena = input('Ingrese una cadena: ')
# no se puede usar [:: -1] ni reverse

cadena = input('ingrese una palabra o oracion')
invertida = ''

for letra in cadena:
    invertida = letra + invertida

print(invertida)

