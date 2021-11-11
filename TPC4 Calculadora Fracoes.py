import sys
''' calculadora de funções
com menu que envolva:
- somar
- subtrair
- multiplicar
- dividir
-sair
 mostre sempre o resultado na forma irredutivel
 '''

        
def Menu ():
    print ('''\t MENU
1. somar
2. subtrair
3. multiplicar
4. dividir
5. sair''')

def sair():
    sys.exit()

def criarFracao (numerador, denominador):
    return (numerador, denominador)
    
def verFracao (f):
    n, d = f
    print (str (int(n)) + '/' + str(int(d)))

def mdc(a,b):
    res=1
    if a>b:
        a,b=b,a
    for i in range (2,a):
        if (a%i ==0) and (b%i==0):
            res=i
    return res

def mdc2 (a,b):
    if a<b:
        return mdc (b,a)
    elif a%b ==0:
        return(b)
    else:
        return mdc (a,a%b)
           
def simplificarFracao(f):
    n,d=f
    m=mdc2 (n,d)
    return (int(n/m), int(d/m))

def somarFracao (f1,f2):
    n1,d1 =f1
    n2,d2 =f2
    return simplificarFracao(criarFracao(n1*d2 + n2*d1, d1*d2))

def subtrairFacao (f1,f2):
    n1,d1 =f1
    n2,d2 =f2
    return simplificarFracao(criarFracao(n1*d2 - n2*d1, d1*d2))

def dividirFracao(f1,f2):
    n1,d1 =f1
    n2,d2 =f2
    return simplificarFracao(criarFracao(n1*d2, d1*n2))

def multiplicarFracao(f1,f2):
    n1,d1 =f1
    n2,d2 =f2
    return simplificarFracao(criarFracao(n1*n2, d1*d2))

def gerar():
    numerador=int(input("Numerador: "))
    denominador=int(input("Denominador: "))
    return((numerador, denominador))

def jogar():
    res=0
    while(True):
        print("1ª Fração")
        (numerador1, denominador1)=gerar()
        print("2ª Fração")
        (numerador2, denominador2)=gerar()
        Menu()
        p=input('Seleciona uma opção: ')
        if int(p)== 1:   
            res=somarFracao( (numerador1, denominador1), (numerador2, denominador2))
            verFracao(res)
        if int(p)== 2:   
            res=subtrairFacao( (numerador1, denominador1), (numerador2, denominador2))
            verFracao(res)
        if int(p)== 3:   
            res=multiplicarFracao( (numerador1, denominador1), (numerador2, denominador2))
            verFracao(res)
        if int(p)== 4:   
            res=dividirFracao( (numerador1, denominador1), (numerador2, denominador2))
            verFracao(res)            
        if int(p)==5 :
            sair()

jogar()  
