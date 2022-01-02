def numero_digitos(n):
    cont = 0
    r0 = (n-1)%n
    rPERMANENTE = (n-1)%n
    cont+=1
    
    while True:
        r = (r0*10)%n
        if r == rPERMANENTE:
            break
        else:
            cont+=1
            r0 = r
            
    print(n," ","-"," ", end = "")
    print(cont," ","-"," ", end = "")
    if (n-1)%cont == 0:
        print(" primo")
    else:
        print(" nao primo")

def main():
    n = int(input("Digite um número: "))
    numero_digitos(n)
    
main()
