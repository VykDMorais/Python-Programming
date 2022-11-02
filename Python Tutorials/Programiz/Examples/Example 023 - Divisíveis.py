lista = []
a = int(input("Quantos números você quer digitar? "))
for i in range (0, a, 1):
    lista.append(int(input(f"Digite o {i} número: ")))
div = int(input("Qual é o denominador? "))
lista = list(filter(lambda x: (x%div == 0), lista))
print (f"Da lista que você forneceu, os números que são divisíveis por {div}, são: {lista}")
input()