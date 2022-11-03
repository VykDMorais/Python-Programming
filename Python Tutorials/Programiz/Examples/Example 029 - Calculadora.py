def somador (fator1, fator2):
    print (f"{fator1} + {fator2} = {fator1 + fator2}")
def subtrator (fator1, fator2):
    print (f"{fator1} - {fator2} = {fator1 - fator2}")
def multiplicador (fator1, fator2):
    print (f"{fator1} * {fator2} = {fator1 * fator2}")
def divisor (fator1, fator2):
    print (f"{fator1} / {fator2} = {fator1 / fator2}")
def potencia (fator1, fator2):
    print (f"{fator1} ^ {fator2} = {fator1 ** fator2}")
def fato (fator1, fator2):
    fatinho = int(fator1)
    result = 1
    for i in range (1, fatinho + 1, 1):
        result = result * i
    print (f"{fatinho}! = {result}")
while (True):
    print ("Se você quiser somar, digite 1\nSe você quiser subtrair, digite 2\nSe você quer multiplicar, digite 3")
    print ("Se você quer dividir, digite 4\nSe você quer potência ou raiz, digite 5\nSe você quer fatorial, digite 6")
    choice = int(input("Escolha a operação: "))
    if choice >= 1 and choice <= 6:
        fator1 = float(input("Digite o fator 1: "))
        fator2 = float(input("Digite o fator 2: "))  
        if choice == 1:
            valor = somador (fator1, fator2)
        elif choice == 2:
            valor = subtrator (fator1, fator2)
        elif choice == 3:
            valor = multiplicador (fator1, fator2)
        elif choice == 4:
            valor = divisor (fator1, fator2)
        elif choice == 5:
            valor = potencia (fator1, fator2)
        else:
            valor = fato (fator1, fator2)
    else:
        print("Valor inválido")  
input()  