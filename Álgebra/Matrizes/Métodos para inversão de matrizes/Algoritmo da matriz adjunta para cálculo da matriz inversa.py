import numpy as np
from math import *

def final(matriz, determinante):
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[0])):
            matriz[i][j] = (1/determinante)*(matriz[i][j])

    print("A^-1 = ", end = "")
    print(matriz)
    return matriz

def sinais(det_menor):
    for i in range(0, len(det_menor)):
        for j in range(0, len(det_menor[0])):
            if (i+j)%2!=0:
                det_menor[i][j] = (-1)*(det_menor[i][j])
    return det_menor

def menores(agrupadas):
    m0 = []
    for a in range(0, len(agrupadas)):
        l = []
        for b in range(0, len(agrupadas[0])):
            determinante = np.linalg.det(agrupadas[a][b])
            l.append(determinante)
        m0.append(l)
    return m0

def agrupamento(det_menor, n):
    m = []
    for a in range(0, len(det_menor), n):
        l = []
        for b in range(a, a+n):
            l.append(det_menor[b])
        m.append(l)
    return m

def matriz_determinantes_menores(matriz, n):
    detM = []
    aux = []
    
    for i in range(n):
        for j in range(n):
            for a in range(n):
                l = []
                for b in range(n):
                    if a!= i and b != j:
                        l.append(matriz[a][b])
                if len(l)!=0:
                    aux.append(l)
            detM.append(aux)
            aux = []
    return detM

def cria_matriz(matriz, n):
    for i in range(n):
        linha = []
        for j in range(n):
            x = float(input("Digite o elemento a%d,%d da matriz: " %(i+1, j+1)))
            linha.append(x)
        matriz.append(linha)
    return matriz

def ordem_dois(matriz, n):
    adjunta = [[0, 0], [0, 0]]
    determinante = np.linalg.det(matriz)

    if abs(determinante)<10**(-5):
        print("Não há inversa")
    else:
        adjunta[0][0] = matriz[1][1]
        adjunta[0][1] = (-1)*matriz[0][1]
        adjunta[1][0] = (-1)*matriz[1][0]
        adjunta[1][1] = matriz[0][0]

        for i in range(n):
            for j in range(n):
                adjunta[i][j] = (1/determinante)*(adjunta[i][j])

        print("A^-1 = ", end="")
        print(adjunta)

def ordem_um():
    a = float(input("Digite o elemento a11: "))
    print("A^-1", end = "")
    print(1/a)

def main():
    n = int(input("Digite a ordem da matriz: "))
    if n == 1:
        ordem_um()
    elif n == 2:
        matriz = []
        matriz = cria_matriz(matriz, n)
        ordem_dois(matriz, n)
    else:
        matriz = []
        matriz = cria_matriz(matriz, n)
        if round(np.linalg.det(matriz))==0:
            print("\n")
            print("A matriz inserida não é invertível, pois seu determinante é igual a zero")
            print("\n")
        else:
            det_menor = []
            agrupada = []
            det_menor_final = []
            det_menor = matriz_determinantes_menores(matriz, n)
            agrupada = agrupamento(det_menor, n)
            det_menor_final = menores(agrupada)
            det_menor_final = sinais(det_menor_final)
            det_menor_final = np.transpose(det_menor_final)
            determinante = np.linalg.det(matriz)
            final(det_menor_final, determinante) 
main()

