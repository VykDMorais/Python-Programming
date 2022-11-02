menor = int(input("Digite o menor inteiro: "))
maior = int(input("Digite o maior inteiro: "))
for num in range (menor, maior + 1, 1):
    ordem = len(str(num))
    soma = 0
    aux = num
    while aux > 0:
        digito = aux%10
        soma += digito**ordem
        aux //= 10
    if num == soma:
        print(num)