def imprime (n: int):
    for linha in range (1, n + 1):
        for coluna in range (linha):
            print (coluna, end='  ')
        print ('')
n = int(input("Digite um número: "))
input()