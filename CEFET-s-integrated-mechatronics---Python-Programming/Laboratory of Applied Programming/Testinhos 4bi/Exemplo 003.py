def ex():
    def nome ():
        pass#passa pro prÃ³ximo
    def func ():
        print ("o ano tá acabando!")
    def somador (a = 1, b = 2):#se o usuáio enviar somador () -> valores default
        print (f"A soma de {a} + {b} = {a+b}")
        c = a + b
        return c
    nome()
    func()
    c = somador ()
    somador (6, 7)
    somador (4)
    somador (b = 6)
    print (c)
def divisor (num, den):
    if den != 0:
        r = num/den
    else:
        r = None
    return r
#ex()
#resultado1 = divisor (den = 2, num = 10)
#resultado2 = divisor (10,2)
#print (resultado1,"          ", resultado2)
#print (f"{resultado1*10}")

def tup (*args):# * -> pode ter qualquer tamanho
#def fun(a, b, c, *args)
    for i in (args):#quando n é int, tem que tirar o range
        if i > 5:
            print (i)
    print (args) #retorna em tuple
tup (1,15,3,4,5,11,12,13)
tup (3, 4, 5)
input()