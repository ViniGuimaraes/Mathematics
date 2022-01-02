import numpy as np
from copy import deepcopy

def segundaG(n_1_matrizes, n):
    G_2 = []
    for i in range(n):
        linha = []
        for j in range(n):
            if j<i:
                linha.append(0)
            else:
                alfa = i
                t = n-i
                p = 1
                for l in range(n-i-1, n):
                    p*=n_1_matrizes[l][0][0]
                linha.append(n_1_matrizes[t-1][0][j-alfa]/p**(1/2))
        G_2.append(linha)
    return G_2

def primeiraG(n_1_matrizes, n):
    G_1 = []
    for i in range(n):
        linha = []
        for j in range(n):
            if j>i:
                linha.append(0)
            else:
                alfa = j
                t = n-j
                p = 1
                for l in range(n-j-1, n):
                    p*=n_1_matrizes[l][0][0]
                linha.append(n_1_matrizes[t-1][i-alfa][0]/p**(1/2))
        G_1.append(linha)
    return G_1

def matrizes_secundarias(matriz, n):
    m2 = [0]*n
    m2[n-1] = deepcopy(matriz)
    for t in range(n-2, -1, -1):
        aux = []
        for i in range(t+1):
            linha = []
            for j in range(t+1):
                linha.append(round(np.linalg.det([[m2[t+1][0][0], m2[t+1][0][j+1]],[m2[t+1][i+1][0], m2[t+1][i+1][j+1]]])))
            aux.append(linha)
        m2[t] = deepcopy(aux)
    return m2
    
def menores(matriz, n):
    if round(np.linalg.det(matriz))<=0:
        return  False
    for i in range(1, n):
        menor = []
        for j in range(i):
            menor.append(matriz[0:i][j][0:i])
        if round(np.linalg.det(menor))<=0:
            return False
    return True

def cria_matriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(float(input("Digite o elemento a%d,%d da matriz: " %(i+1, j+1))))
        matriz.append(linha)
    return matriz

def main():
    matriz = []
    n = int(input("Digite a ordem da matriz: "))
    matriz = cria_matriz(n)
    if np.array_equal(matriz, np.transpose(matriz)):
        if menores(matriz, n):
            n_1_matrizes = []
            n_1_matrizes = matrizes_secundarias(matriz, n)
            G_1 = []
            G_2 = []
            G_1 = primeiraG(n_1_matrizes, n)
            G_2 = segundaG(n_1_matrizes, n)
            print("G1 = ")
            print(G_1)
            print("\n")
            print("G1^T = ")
            print(np.transpose(G_1))
            print("\n")
            print("VERIFICAÇÃO G1G1^T")
            print(np.dot(G_1, np.transpose(G_1)))
            print("\n")

            print("G2 = ")
            print(G_2)
            print("\n")
            print("G2^T = ")
            print(np.transpose(G_2))
            print("\n")
            print("VERIFICAÇÃO G2G2^T")
            print(np.dot(np.transpose(G_2), G_2))

        else:
            print("A matriz possui menor principal nulo")
    else:
        print("A matriz não é simétrica")
main()
