menor = int(input("Digite o menor inteiro do intervalo de primos: "))
maior = int(input("Digite o maior inteiro do intervalo de primos: "))
for n in range(menor, maior + 1):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            print(n)
input()