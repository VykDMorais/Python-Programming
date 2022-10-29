def testador (a):
    if a > 0:
        r = 'P'
        return r
    elif a < 0:
        r = "N"
        return r
    else:
        r = 0
        return r
a = int(input("Digite um número: "))
print (f"{a} é {testador(a)}")
input()