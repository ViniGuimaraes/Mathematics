import numpy as np
import matplotlib.pyplot as plt

array = []
r = 's'
s = 0

def gerar_grafico(x, P, n):
    y = 0
    for i in range(n+1):
        y += P[i]*x**i
    return y

def imprimir(P, array):
    print("\n")
    for i in range(len(array)):
        s = "f["
        for j in range(i+1):
            if j==i:
                s+="x"+str(j)+"] = "+str(array[i])
            else:
                s+="x"+str(j)+","
        print(s)
    print("\n")
    print("\n")
    print(P)
    print("\n")

def polinomio_final(x, fx, fc):
    P = 0
    for i in range(len(fx)):
        produto = 1
        if i == 0:
            P+= fc[0]
        else:
            for j in range(i):
                produto *= np.poly1d([x[j]], True)
            P+= produto*fc[i]
    return P

def polinomios_derivada(x, fx):
    global r, s
    if r == 's':
        s = x[0]
        r = 0.0
    if len(fx) == 1:
        if x[0] == s: array.append(fx[0])
        return float(fx[0])
    else:
        r = (polinomios_derivada(x[1:],fx[1:])-polinomios_derivada(x[:-1],fx[:-1]))/(x[-1]-x[0])
        if x[0] == s: array.append(r)
        return float(r)

def valores_iniciais(n):
    x = []
    fx = []
    for i in range(n):
        x.append(float(input("Digite o valor x"+str(i)+": ")))
        fx.append(float(input("Digite o valor f(x"+str(i)+"): ")))
    return x, fx

def main():
    x = []
    fx = []
    P = 0

    n = int(input("Digite o número de pares ordenados (x, f(x)) conhecidos: "))
    x, fx = valores_iniciais(n)
    polinomios_derivada(x, fx)
    P = polinomio_final(x, fx, array)
    imprimir(P, array)

    x = np.linspace(-10, 10, num=1000)
    fig, ax = plt.subplots()
    ax.plot(x, gerar_grafico(x,P,n))
    ax.axhline(y=0, color = 'k')
    ax.axvline(x=0, color = 'k')
    plt.show()

main()
