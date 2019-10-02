#Nome:Eduardo Bruno Martins Esperança
#1/10/2019
#
#descrrção:questão 4.
def nob(num_a,num_b):
    if len(num_a) ==1 and len(num_b) ==2:
        v1=int(num_a[0])
        v2=int(num_b[0])+int(num_b[1])
    if len(num_a) ==2 and len(num_b) ==1:
        v1=int(num_b[0])
        v2=int(num_a[0])+int(num_a[1])
    if len(num_a) ==1 and len(num_b) ==1:
        v1=int(num_a[0])
        v2=int(num_b[0])
    if len(num_a) ==2 and len(num_b) ==2:
        v1=int(num_a[0])+int(num_a[1])
        v2=int(num_b[0])+int(num_b[1])
    return v1+v2
def main():
    num_a=input("digite o primeiro valor =")
    num_b=input("digite o segundo valor = ")
    print(nob(num_a,num_b))
main()
