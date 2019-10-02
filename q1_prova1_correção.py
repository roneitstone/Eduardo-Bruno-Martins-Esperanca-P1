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
        
        return 1 , (-b+(k**(1/2)))/2*a ,  (-b-(k**(1/2)))/2*a



a = int(input("digite a = "))
b = int(input("digite b = "))
c = int(input("digite c = "))
print(baskara(a,b,c))
