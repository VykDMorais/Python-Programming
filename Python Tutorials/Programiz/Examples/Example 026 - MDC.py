def mdc (a, b):
    if a > b:
        menor = b
    else:
        menor = a
    for i in range (1, menor + 1, 1):
        if a%i == 0 and b%i == 0:
            divi = i
    return (divi)
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
print(f"O mdc de {a} e {b} é: {mdc (a, b)}")
input()