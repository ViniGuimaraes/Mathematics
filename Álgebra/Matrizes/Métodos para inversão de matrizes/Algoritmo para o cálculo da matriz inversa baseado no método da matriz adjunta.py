import numpy as np

def final(inversa, determinante):
    for i in range(0, len(inversa)):
        for j in range(0, len(inversa[0])):
            inversa[i][j] = (1/determinante)*inversa[i][j]
    print("A^-1 = ")
    print(inversa)

def sinais(inversa):
    for i in range(0, len(inversa)):
        for j in range(0, len(inversa[0])):
            if (i+j)%2!=0:
                inversa[i][j] = (-1)*inversa[i][j]
    return inversa

def inversa_primeiro(determinantes, n):
    I = []
    for i in range(0, len(determinantes), n):
        l = []
        l.extend(determinantes[i:i+n])
        I.append(l)
    return I

def dets(matriz_exp, k):
    n = int((len(matriz_exp))/2)+1
    m0 = np.array(matriz_exp)
    D = []
    for i in range(0, n):
        for j in range(0, n):
            D.append(np.linalg.det(m0[i:k-1+i, j:k-1+j]))
    return D

def transformacao(matriz_exp, n):
    linha = []
    for a in range(0, 2*(n-1)):
        linha.append([])
        
    for a in range(0, 2):
        for i in range(0, n-1):
            linha[i].extend(matriz_exp[a][i])

    for b in range(2, 4):
        for i in range(0, n-1):
            linha[i+(n-1)].extend(matriz_exp[b][i])

    return linha

def matriz_expandida(matriz, n):
    aux = []
    exp = []
    for i in range(0, len(matriz)):
        l = []
        for j in range(0, len(matriz[0])):
            if i!=0 and j!=0:
                l.append(matriz[i][j])
        if len(l)!=0:
            aux.append(l)
    exp.append(aux)

    aux = []
    
    for i in range(0, len(matriz)):
        l = []
        for j in range(0, len(matriz[0])):
            if i!=0 and j!=(len(matriz)-1):
                l.append(matriz[i][j])
        if len(l)!=0:
            aux.append(l)
    exp.append(aux)

    aux = []

    for i in range(0, len(matriz)):
        l = []
        for j in range(0, len(matriz[0])):
            if i!=(len(matriz)-1)and j!=0:
                l.append(matriz[i][j])
        if len(l)!=0:
            aux.append(l)
    exp.append(aux)

    aux = []

    for i in range(0, len(matriz)):
        l = []
        for j in range(0, len(matriz[0])):
            if i!=(len(matriz)-1) and j!=(len(matriz)-1):
                l.append(matriz[i][j])
        if len(l)!=0:
            aux.append(l)
    exp.append(aux)
    
    return exp
    
def cria_matriz(matriz, n):
    for i in range(n):
        linha = []
        for j in range(n):
            x = float(input("Digite o elemento a%d,%d da matriz: " %(i+1, j+1)))
            linha.append(x)
        matriz.append(linha)
    return matriz

def main():
    matriz = []
    matriz_exp = []
    determinantes = []
    
    n = int(input("Digite a ordem da matriz: "))
    
    matriz = cria_matriz(matriz, n)
    determinante = np.linalg.det(matriz)

    matriz_exp = matriz_expandida(matriz, n)
    matriz_exp = transformacao(matriz_exp, n)
    determinantes = dets(matriz_exp, n)
    inversa = inversa_primeiro(determinantes, n)
    inversa = np.transpose(inversa)
    if n>3:
        inversa = sinais(inversa)
    final(inversa, determinante)
main()
