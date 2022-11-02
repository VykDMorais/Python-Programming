num = int(input("Qual número você quer? "))
termo = int(input("Quantos termos você quer? "))
resultado = list(map(lambda x: num**x, range(termo)))
for i in range (termo):
    print (f"{num} elevado a {i} = {resultado[i]}")
input()