import numpy as np
x = np.arange(10, 30, 2)
print (x)
indice = np.array ([0, 2, 3])
print (x[indice])
x.shape = (2, 5)
t = np.linspace (0, 2, 9)
print (t)
print (t[0:2]) #retorna dois elementos a partir do zero    
print (x[0][2])
print (x[0, :])#retorna linha 0
print (x[:, 2])#retorna coluna 2
y = np.array ([1, 2, 3, 4])
verdade = np.array ([0, 1, 0, 1], dtype = bool)
print (y[verdade])
q = np.identity(3)
print (q)
b = np.zeros_like (x)
np.copyto (b, x)
def func (vetor):
    print (vetor > 15)
func = np.vectorize(func)
func (y)
