lista = [1, 2, 4, 6, 8, 69, 234, 676, 112]
nova_lista = list(filter(lambda x: (x%2 == 0), lista))
print (nova_lista)
lista2 = list(map(lambda x: x*2, lista))
print (lista2)
dobro = lambda x: x* 2
print (dobro(5))
input()