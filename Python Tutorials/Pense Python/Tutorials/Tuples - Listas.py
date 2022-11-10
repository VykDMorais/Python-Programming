s = 'abc'
t = [0, 1, 2]
A = zip(s, t)
print (A)
for pair in zip (s, t):
    print (pair)
z = list(zip(s, t))
print (z)
for letra, numero in z:
    print(numero, letra)
def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            print (x)
            return (True)
    return False
t1 = (1, 2, 3, 4, 5)
t2 = (0, 2, 4, 6, 8)
has_match (t1, t2)
for index, element in enumerate ("abcde"):
    print (element, index)