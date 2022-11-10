def cal (t):
    return min(t), max (t)
g = tuple()#g = ('a',)
q = tuple ("bobão")
print(q, "------", q[0], "------", q[1:3])#q[1:3] -> começa na casa 1 e acaba 1 antes da casa 3, ou seja, na casa 2
q = q[:3] + ('õ', 'e', 's')#q = ('A',) + q[1:] = ('A', 'o', 'b', 'ã', 'O') 
print (q)
a, b = 1, 2
print(a, "------", b)
addr = "victor.morais.vbdm@gmail.com"
nome, email = addr.split('@')
print(f"Nome: {nome}\nEmail: {email}")
quo, resto = divmod (7, 3)
t = divmod (8, 6)
print (cal(t))
def printall (*args):#*args é uma tuple querada momentaneamente
    print(sum(args), args)
printall (1, 2, 5, 6, 2, 6)
r = (7, 3)
q1, r1, = divmod(*r)
print (q1, r1)
input()