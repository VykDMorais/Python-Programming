x = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
y = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range (len(x)): #3 linhas
    for j in range (len(x[0])): #3 colunas
        result [i][j] = x[i][j] + y [i][j]
for r in result:#para r no result -> isso para imprimir linhas e colunas certinho
    print (r) 
input()