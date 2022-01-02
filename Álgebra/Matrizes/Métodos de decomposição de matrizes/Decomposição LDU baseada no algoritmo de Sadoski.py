from copy import deepcopy
import numpy as np

def segunda_U(n_1_matrizes, n):
    U = []
    for i in range(len(n_1_matrizes[len(n_1_matrizes)-1])):
        linha = []
        alfa = i
        t = n+1-i
        for j in range(len(n_1_matrizes[len(n_1_matrizes)-1])):
            if i == j:
                linha.append(1)
            elif i>j:
                linha.append(0)
            else:
                if n_1_matrizes[t-2][0][j-alfa] == 0:
                    linha.append(0)
                else:
                    linha.append(n_1_matrizes[t-2][0][j-alfa]/n_1_matrizes[t-2][0][0])
        U.append(linha)
    return U

def segunda_L(n_1_matrizes, n):
    L = []
    for j in range(len(n_1_matrizes[len(n_1_matrizes)-1])):
        linha = []
        k = []
        cont = 0
        for m in range(0, n-j):
            k.append(m)
        t = n-j
        for i in range(len(n_1_matrizes[len(n_1_matrizes)-1])):
            if j == 0:
                linha.append(n_1_matrizes[len(n_1_matrizes)-1][i][j])
            elif j>i:
                linha.append(0)
            else:
                p = 1
                for l in range(n+2-j, n+2):
                    p*=n_1_matrizes[l-2][0][0]
                if n_1_matrizes[t-1][k[cont]][0]==0:
                    linha.append(0)
                else:
                    linha.append(n_1_matrizes[t-1][k[cont]][0]/p)
                cont+=1
        L.append(linha)
    return np.transpose(L)
    
def primeira_U(n_1_matrizes, n):
    U = []
    k = []
    for i in range(len(n_1_matrizes[len(n_1_matrizes)-1])):
        linha = []
        cont = 0
        t = n-i-1
        k = []
        if i !=0:
            for m in range(n-1):
                k.append(m)
        for j in range(len(n_1_matrizes[len(n_1_matrizes)-1])):
            if i == 0:
                linha.append(n_1_matrizes[len(n_1_matrizes)-1][i][j])
            elif i>j:
                linha.append(0)
            else:
                p = 1
                for l in range(n-i, n):
                    p*=n_1_matrizes[l][0][0]
                if n_1_matrizes[t][0][k[cont]] == 0:
                    linha.append(0)
                else:
                    linha.append(n_1_matrizes[t][0][k[cont]]/p)
                cont+=1
        U.append(linha)               
    return U

def primeira_L(n_1_matrizes, n):
    L = []
    for i in range(len(n_1_matrizes[len(n_1_matrizes)-1])):
        linha = []
        for j in range(len(n_1_matrizes[len(n_1_matrizes)-1])):
            if i == j:
                linha.append(1)
            elif j>i:
                linha.append(0)
            else:
                alfa = j
                t = n+1-j
                if n_1_matrizes[t-2][i-alfa][0] == 0:
                    linha.append(0)
                else:
                    linha.append(n_1_matrizes[t-2][i-alfa][0]/n_1_matrizes[t-2][0][0])
        L.append(linha)
    return L

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
    n_1_matrizes = []
    L_1 = []
    U_1 = []
    L_2 = []
    U_2 = []
    
    n = int(input("Digite a ordem da matriz: "))
    matriz = cria_matriz(n)
    n_1_matrizes = matrizes_secundarias(matriz, n)
#PRIMEIRO CONJUNTO DE LU (L1U1)
    L_1 = primeira_L(n_1_matrizes, n)
    U_1 = primeira_U(n_1_matrizes, n)

    print("DECOMPOSIÇÃO LU PRIMEIRA")
    print("L1 = ")
    print(L_1)
    print("\n")
    print("U1 = ")
    print(U_1)
    print("\n")
    print("VERIFICAÇÃO L1U1")
    print(np.dot(L_1, U_1))
    print("\n")
#SEGUNDO CONJUNTO DE LU (L2U2)
    L_2 = segunda_L(n_1_matrizes, n)
    U_2 = segunda_U(n_1_matrizes, n)

    print("DECOMPOSIÇÃO LU SEGUNDA")
    print("L2 = ")
    print(L_2)
    print("\n")
    print("U2 = ")
    print(U_2)
    print("\n")
    print("VERIFICAÇÃO L2U2")
    print(np.dot(L_2, U_2))
    print("\n")
#PRIMEIRO CONJUNTO LDU (L1DlU2)
    Dl = [[U_1[0][0], 0, 0],[0, U_1[1][1], 0],[0, 0, U_1[2][2]]]
    print("DECOMPOSIÇÃO LDU PRIMEIRA")
    print("L1 = ")
    print(L_1)
    print("\n")
    print("Dl = ")
    print(Dl)
    print("\n")
    print("U2 = ")
    print(U_2)
    print("\n")
    print("VERIFICAÇÃO L1DlU2")
    print(np.dot(np.dot(L_1, Dl), U_2))
    print("\n")
#SEGUNDO CONJUNTO LDU (L2DuU1)
    if round(np.linalg.det(matriz))==0:
        print("DECOMPOSIÇÃO LDU SEGUNDA")
        print("\n")
        print("A matriz, por ser singular, não admite uma fatoração LDU segunda")
        print("\n")
    else:
        Du = [[1/U_1[0][0], 0, 0],[0, 1/U_1[1][1], 0],[0, 0, 1/U_1[2][2]]]
        print("DECOMPOSIÇÃO LDU SEGUNDA")
        print("L2 = ")
        print(L_2)
        print("\n")
        print("Du = ")
        print(Du)
        print("\n")
        print("U1 = ")
        print(U_1)
        print("\n")
        print("VERIFICAÇÃO L2DuU1")
        print(np.dot(L_2, np.dot(Du, U_1)))
        print("\n")

main()