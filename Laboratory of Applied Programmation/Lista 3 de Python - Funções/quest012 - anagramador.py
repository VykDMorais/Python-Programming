import random
def anagramador (palavra):
    embaralha = random.sample(palavra, len(palavra)) #string vira lista
    anagrama = ''.join (embaralha) #lista vira string
    print (f"Anagrama: {anagrama}")
while (True):
    palavra = input("Digite uma palavra [0 para encerrar]: ").lower()
    if palavra == '0':
        break
    anagramador (palavra)