#Name:Eduardo Bruno Martins Esperança
#1/10/2019
#
#descrição: questão 3.

#a questão está errada pois não entendi o que era iteração nunca ouvi falar, porém o que tinha entendido era que o 1 - (n) que tinha que ser <= ao valor da questão, mas depois vi que isso era impossível e fiz a correção com a ideia da resposta.
def pi (n):
    cont=0
    while (5/10**8) < (1-n):
        cont+=1
        if cont %2 ==0:
            n=n+(1/variante(cont))
        if cont %2 ==0:
            n=n-(1/variante(cont))
    
    return 4*(1-n)
def variante(cont):
    return 1+2*cont
def main():
    deseja = int(input("quer iniciar, digite 1 ="))
    if deseja ==1:
        n=0
        print(pi(n))
main()
