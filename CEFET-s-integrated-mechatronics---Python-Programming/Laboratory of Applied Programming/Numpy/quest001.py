import numpy as np
def media (dado):
    formato = dado.shape
    n_element = 1
    for i in formato:
        n_element = n_element * i
        print (n_element)
    dado.shape = (n_element)
    print (n_element)
    media = sum(dado)/n_element
    dado.shape = (formato)
    return media
w = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]])
print(media (w))