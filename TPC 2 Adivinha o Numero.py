def jogo ():
    print("""\t ADIVINHA O NÚMERO EM QUE ESTOU A PENSAR

Pensa num número de 0 a 100

O número em que pensaste é maior que 50?""")
    
    acertou= False
    b=50
    minimo= 0
    maximo=100
    tentativas=0
    p= int(input("1:sim   0:não    2:igual - "))
    
    while acertou == False:
        if p == 1:
            minimo= b
            intervalo= (maximo-minimo)
            b = minimo + (intervalo//2)
            #maximo= b
            tentativas= tentativas +1
            print("O número em que pensaste é ",b,"?")
            p= int(input("1:maior   2:igual  0:menor -"))

        elif p == 0:
            maximo=b
            intervalo= (maximo-minimo)
            b = (intervalo//2)+ minimo
            tentativas= tentativas +1
            print("O número em que pensaste é ",b,"?")
            p= int(input("1:maior   2:igual  0:menor -"))

        elif p == 2:
            acertou= True
            tentativas=tentativas +1
            print("O computador adivinhou o seu número em",tentativas,"jogada(s)")
            return(b)

        else:
            acertou= True
            print ("Erro, pfv respeite as regras do jogo\n")           
            jogo()

jogo()
