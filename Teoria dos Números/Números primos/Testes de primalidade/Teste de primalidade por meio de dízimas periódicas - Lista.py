def numero_digitos(pr):
    for i in range(0, len(pr)):
        cont = 0
        r0 = (pr[i]-1)%pr[i]
        rPERMANENTE = (pr[i]-1)%pr[i]
        cont += 1
        while True:
            r = (r0*10)%pr[i]
            if r == rPERMANENTE:
                break
            else:
                cont+=1
                r0 = r
        print(pr[i]," ","-"," ", end = "")
        print(cont," ","-"," ", end = "")
        if (pr[i]-1)%cont == 0:
            print(" primo")
        else:
            print(" nao primo")
            
def elementos_matriz(n):
    pr = [7, 11, 13, 17, 19, 23, 29, 31]
    for i in range(1, n):
        for j in range(8):
            pr.append(pr[j]+30*i)
    return pr

def main():
    pr = []
    
    n = int(input("Até que linha deve ir a lista: "))
    pr = elementos_matriz(n)

    numero_digitos(pr)
    
main()
