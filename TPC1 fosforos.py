#escrever as regras do jogo
import random
print("\t JOGO DOS 21 FÓSFOROS \n O objetivo do jogo é retirar 1-4")
print ( "fósforos de cada vez, quem ficar com o último fósforo perde o jogo.")
print ("As jogadas são intercaladas pelo jogador e o computador. Boa sorte!")

print("\nSeleciona 1 para seres o primeiro a jogar \n" "Seleciona 2 para seres o segundo a jogar")

f=21
n= int(input())
    
if (n==1):
    print (f)
    cont=1
    
    while (f>1): 

        if (cont%2 != 0) :
            x= int(input("digite o nº de fósforos que quer retirar: "))
            f= (f-x)
            print (f)
            cont=cont+1

        else:
            r =(5-x)
            print ("O computador retirou ",r, " fósforos")
            f= (f-r)
            print (f)
            cont=cont+1

    if (f==1):
        print("Perdes-te o jogo :c")

elif (n==2):
    print (f)
    cont = 1

    while (f>1):
        if (cont%2 != 0) :
            x= random.randrange(1,4,1)
            print("O computador retirou:",x)
            f= (f-x)
            print(f)
            cont= cont+1
            
        else:
            r= int(input("digite o nº de fósforos que quer retirar: "))
            f=(f-r)
            print (f)
            cont= cont+1
            soma= (x+r)
            
            if soma != 5:
                c= abs(5- soma)
                f= f-c
                print ("o computador retirou:",c)
                print (f)
                cont= cont+1


    if (f==1):
        print ("Ganhas-te o jogo!")


            





            
    
