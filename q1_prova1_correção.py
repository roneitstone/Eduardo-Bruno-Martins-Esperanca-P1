#name:Eduardo Bruno Martins Esperança
#1/10/2019
#
#descrição:correção da questão 1 .
def baskara (a,b,c):

    k= (b**2)-4*a*c
#a correção feita da questão para se adequar a ambas as perguntas.
    if k < 0:
        k=-(k)
       
        print((-b+(k**(1/2)))/2*a ,"*i", "/" , (-b-(k**(1/2)))/2*a , "*i")
        return 0 

    else:
        print((-b+(k**(1/2)))/2*a ,  (-b-(k**(1/2)))/2*a)
        return 1 



a = int(input("digite a = "))
b = int(input("digite b = "))
c = int(input("digite c = "))
baskara(a,b,c)
