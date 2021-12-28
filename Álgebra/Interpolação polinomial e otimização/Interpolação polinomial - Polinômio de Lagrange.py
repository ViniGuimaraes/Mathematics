import numpy as np
import matplotlib.pyplot as plt

def gerar_grafico(x, P, n):
    y = 0
    for i in range(n+1):
        y += P[i]*x**i
    return y

def imprimir(P, L):
    print("")
    for i in range(len(L)):
        print("L"+str(i)+"(x)"+" = ")
        print("")
        print(L[i])
        print("")
    print("\n")
    print("P(X) = ")
    print("")
    print(P)
    print("\n")

def polonomio_final(L, fx):
    P = 0
    for i in range(len(fx)):
        P+=fx[i]*L[i]
    return P

def polinomios_L(n, x, fx):
    L = []
    for a in range(n):
        produto = 1
        v = []
        for b in range(n):
            if a!=b:
                produto*=(x[a]-x[b])
                v.append(x[b])
        L.append(np.poly1d(v, True)/produto)
    return L

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
    L = []
    P = 0

    n = int(input("Digite o número de pares ordenados (x, f(x)) conhecidos: "))
    x, fx = valores_iniciais(n)
    L = polinomios_L(n, x, fx)
    P = polonomio_final(L, fx)
    imprimir(P, L)

    x = np.linspace(-10, 10, num=1000)
    fig, ax = plt.subplots()
    ax.plot(x, gerar_grafico(x,P,n))
    ax.axhline(y=0, color = 'k')
    ax.axvline(x=0, color = 'k')
    plt.show()

main()