def mmc (a, b):
    if a > b:
        maior = a
    else:
        maior = b
    while (True):
        if maior%a == 0 and maior%b == 0:
            return (maior)
        else:
            maior += 1
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
print(f"O mmc de {a} e {b} é: {mmc(a, b)}")
input()