from random import randint
def craps ():
    def jogar():
        dado_1 = randint (1, 6)
        dado_2 = randint (1, 6)
        print (f"Dado 1: {dado_1}\nDado 2: {dado_2}\nSoma: {dado_1 + dado_2}")
        return (dado_1 + dado_2)
    conta = ganho = perda = 0
    while (True):
        a = input("Pressione para jogar. Para desistir, digite 0: ")
        if a != '0':
            valor = jogar ()
            if conta == 0 and (valor == 7 or valor == 11):
                print ("É isso caralhooo, ganhou!")
                ganho += 1
                conta = 0
            elif conta == 0 and (valor == 2 or valor == 3 or valor == 12):
                print ("Não foi dessa vez, meu consagrado!")
                perda += 1
                conta = 0
            elif conta == 0:
                print ("Jogue novamente")
                ponto = valor
                conta = 1    
            elif conta >= 1:
                if ponto == valor:
                    print ("Vitória, campeão!")
                    ganho += 1
                    conta = ponto = 0
                elif valor == 7:
                    print ("PeRdEu OtÁrIo!")
                    perda += 1
                    conta = ponto = 0
                else:
                    print("Jogue novamente")    
        else:
            print (f"Você ganhou {ganho} vezes e perdeu {perda} vezes")
            break
    print ("Obrigado por jogar!")
craps ()
input ()