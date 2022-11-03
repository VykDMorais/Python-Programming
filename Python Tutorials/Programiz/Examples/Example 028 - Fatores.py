div = []
def fatores (num):
    for i in range (1, num + 1, 1):
        if num % i == 0:
            div.append(i)
    print (f"Os fatores de {num} são: {div}")
num = int(input("Digite um número: "))
fatores (num)
input()