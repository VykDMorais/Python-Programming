import math as m
def comparador_log (a, b):
    if a > b:
        result = m.log(a)/m.log(b)
        if result%int(result) == 0:
            return (True)
        else:
            return (False)
    else:
        result = m.log(b)/m.log(a)
        if result%int(result) == 0:
            return (True)
        else:
            return (False)
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
print (f"Utilizando o comparador_log: {comparador_log (a, b)}")
input()