#lista_1 = ['string', 123, False]

#lista_2 = ['Ramon', 'Sere','Gerardo']

#lista_3 = ['un dato', lista_1, 'Datos2', lista_2]
# print(lista_3)
# print(lista_3[1][0]) #imprime el primer elemento de la lista 1
# lista_1.appende('valor nuevo') #agrega un nuevo elemento a la lista 1






#lista = [1, 2, 3, 4, 5]
# print(lista[0]) #imprime el primer elemento de la lista
#lista.reverse() #invierte la lista
#print(lista) #imprime la lista invertida

#tupla = (1, 2, 3, 4, 5) #tupla
#print(tupla[0]) #imprime el primer elemento de la tupla

#crear una lista nueva, con los elementos de potenciados por si mismos
# 0** 0, 4**4, 9**9, 16**16, 25**25

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_potencia = [x**x for x in lista]
print(lista_potencia)