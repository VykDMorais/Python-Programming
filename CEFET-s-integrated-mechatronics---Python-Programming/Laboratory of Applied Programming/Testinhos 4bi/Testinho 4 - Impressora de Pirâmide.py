def impressora (a):
    for x in range (a):#a = 5 e x = 2
        for h in range (x):#vai até 2
            print ('.', end = '')#printa 2 .
        for l in range (a-x):#vai até 2
            print ('#', end = '')#printa 3 #
        print ('  ', end ='')# da o espaço
        for h in range (a-x):#vai até 2
            print ('#', end = '')#printa 3 #
        for l in range (x):#vai até 2
            print ('.', end = '')#printa 2 .
        print()
num = int(input("Digite um valor: "))   
impressora (num)
input()