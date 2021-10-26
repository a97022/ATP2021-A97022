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
    alterou = 1
    tentativas= 1
    i=0
    while alterou != 0:
        alterou = 0
        for i in range (len(lista2)-1):
            if lista2[i] > lista2[i+1]:
                lista2[i], lista2[i+1] = lista2[i+1], lista2[i]
                i=i+1
                tentativas = tentativas + 1
            else:
                tentativas = tentativas + 1
                i=i+1
    print(lista2)
    return (lista2)
        
        
bubbleSort()
