#Name:Eduardo Bruno Martins Esperança
#1/10/2019
#
#descrição: questão 3.
def pi (n):
    cont=3
    k=76/105
    n2=1
    v1,v2=1,0
    while 5/(10**8) < -(v2-v1) :
        cont+=1
        if cont %2 ==0:

            n=(1/variante(cont))
            cont+=1
            n2=(1/variante(cont))
            k= k+(n-n2)
            v1= n-n2
       
        else:
            
            cont+=1
            n=(1/variante(cont))
            cont+=1
            n2=(1/variante(cont))
            k=k+(n-n2)
            v2= n-n2
       
    return 4*k
def variante(cont):
    return 1+2*cont
def main():
    deseja = int(input("quer iniciar, digite 1 ="))
    if deseja ==1:
        n=0
        print(pi(n))
    main()
main()
