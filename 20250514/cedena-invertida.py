# se ingresa por pantalla una cadena y se debe invertir
# cadena = input('Ingrese una cadena: ')
# no se puede usar [:: -1] ni reverse
# si la palabra es palindroma/capicua



cadena = input('ingrese una palabra o oracion')
invertida = ''

for letra in cadena:
    invertida = letra + invertida

print(f"la cadena invertida se ve como: {invertida}")
# verificar si la cadena es capicua
# una cadena es capicua si se lee igual de izquierda a derecha que de derecha a izquierda
if (cadena == invertida):
    print(f'la palabra es capicua {cadena}')
else:
    print(f'la palabra no es capicua {invertida}')


