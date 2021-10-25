def criarListaR():
    from random import randrange
    n = int(input('Introduz nº de elementos: '))
    lista= []
    i= 1
    while len(lista)<n:
        elem= randrange (0,101)
        str(i)+ ':'
        lista.append(elem)
        i=i+1
    print (lista)
    return(lista)    

def bubbleSort ():
    lista2 = criarListaR()
    alterou = True
    tentativas= 0
    i=0
    while alterou == True:
        #alterou = False
        for i in range (len(lista2)-1):
            if lista2[i] > lista2[i+1]:
                lista2[i], lista2[i+1] = lista2[i+1], lista2[i]
                i=i+1
                alterou = True
                tentativas = tentativas +1
                print (lista2)
            else:
                tentativas = tentativas + 1
                i=i+1
                print (lista2)
        
    #if tentativas > n**2
        #return (lista)
        
        
bubbleSort()
