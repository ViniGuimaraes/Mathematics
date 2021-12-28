import numpy as np
import matplotlib.pyplot as plt
import string

def gerar_grafico(x, coeficientes):
    coeficientes = coeficientes[::-1]
    y=0
    for i in range(len(coeficientes)):
        y += coeficientes[i]*x**i
    return y

def imprimir_resultados(coeficientes, x, fx):
    a = list(string.ascii_lowercase)
    print("")
    for i in range(len(x)):
        count = 0
        s=""
        for j in range(len(x)-1, -1, -1):
            if x[i]**j>=0:
                if j == len(x)-1:
                    s+=str(abs(x[i]**j))+a[count]+"^"+str(j)+" "
                else:
                    s+="+ "+str(abs(x[i]**j))+a[count]+"^"+str(j)+" "
            else:
                s+="- "+str(abs(x[i]**j))+a[count]+"^"+str(j)+" "
            count+=1
        s+=" = "+str(fx[i])
        print(s)
    print("")
    coeficientes = coeficientes[::-1]
    S = "P(x) = "
    for i in range(len(coeficientes)-1, -1, -1):
        if i == 0:
            if coeficientes[i] >= 0:
                S += " + "+str(coeficientes[i])
            else:
                s += " - "+str(abs(coeficientes[i]))
        else:
            if coeficientes[i] >= 0:
                S += " + "+str(coeficientes[i])+"x^"+str(i)
            else:
                S += " - "+str(abs(coeficientes[i]))+"x^"+str(i)
    print(S)

def formacao_sistema_linear(n, x, fx):
    matriz_coeficientes = []
    array_independentes = []
    for i in range(n):
        linha = []
        for j in range(n-1, -1, -1):
            linha.append(x[i]**j)
        array_independentes.append(fx[i])
        matriz_coeficientes.append(linha)
    return matriz_coeficientes, array_independentes

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
    A = []
    b = []

    n = int(input("Digite o número de pares ordenados (x, f(x)) conhecidos: "))
    x, fx = valores_iniciais(n)
    A, b = formacao_sistema_linear(n, x, fx)
    coeficientes = np.linalg.solve(A, b)
    imprimir_resultados(coeficientes, x, fx)
    x = np.linspace(-10, 10, num=1000)
    fig, ax = plt.subplots()
    ax.plot(x, gerar_grafico(x, coeficientes))
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    plt.show()

main()