from copy import deepcopy

def imprimir(x):
    print("")
    for i in range(len(x)):
        print("x"+str(i+1)+" = "+str(x[i]))

def solucoes(n, c, cp, potencia):
    raiz = 2**potencia
    x = []
    inv = c[::-1]
    for i in range(len(cp)-1):
        x.append((cp[i+1]/cp[i])**(1/raiz))
    for i in range(len(x)):
        s = 0
        for j in range(len(c)):
            if j == 0:
                s+=inv[j]
            else:
                s+=inv[j]*x[i]**j
        if round(s)!=0:
            x[i]=(-1)*x[i]
    return x

def coeficientes_potencia(c, potencia):
    cp = deepcopy(c)
    for t in range(potencia):
        if t == 0:
            pass
        else:
            c = deepcopy(cp)
        for i in range(len(c)):
            if i == 0 or i == len(c)-1:
                cp[i] = cp[i]**2
            else:
                p = 0
                if i<=len(c)-2-i: #mais próximo do termo de maior grau
                    for j in range(1, i+1):
                        p+=((-1)**j)*(2*c[i-j]*c[i+j])
                else:
                    for j in range(1, len(c)-i):
                        p+=((-1)**j)*(2*c[i-j]*c[i+j])
                cp[i] = c[i]**2+p
    return cp

def coeficientes_polinomio(n):
    c = []
    for i in range(n+1):
        c.append(float(input("Digite o termo a"+str(i)+": ")))
    return c

def main():
    c = []
    cp  = []
    x = []

    n = int(input("Digite a ordem do polinômio: "))
    potencia = int(input("Digite a potência de 2: "))
    potencia = int(potencia**(1/2))
    c = coeficientes_polinomio(n)
    cp = coeficientes_potencia(c, potencia)
    x = solucoes(n, c, cp, potencia)
    imprimir(x)
main()
