#name:Eduardo Bruno Martins Esperança
#1/10/2019
#
#descrição:correção da questão 1 .
def baskara (a,b,c):
#como é perceptivel eu apenas esqueci de ler o primeiro comando, por falta atenção , a unica mudança a se fazer é completar a questão.
    k= (b**2)-4*a*c

    if k < 0:
        
        return 0 

    else:
        
        return 1 


a = int(input("digite a = "))
b = int(input("digite b = "))
c = int(input("digite c = "))
print(baskara(a,b,c))
