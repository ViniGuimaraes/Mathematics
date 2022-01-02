import numpy as np

def vetores_ortogonais(w):
    v = []
    v.append(w[0])
    for i in range(1, len(w)):
        c = [0]*len(w[0])
        for j in range(0, i):
            a = np.dot(w[i], v[j])
            b = np.dot(v[j], v[j])
            q = a/b
            matrix = np.dot(q, v[j])
            c = np.add(matrix, c)
        v.append(np.subtract(w[i], c))
    return v

def definir_vetores(matriz):
    w = []
    for j in range(len(matriz)):
        aux = []
        for i in range(len(matriz)):
            aux.append(matriz[i][j])
        w.append(aux)
    return w           

def cria_matriz(n):
    matriz = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(float(input("Digite o elemento a"+str(i+1)+str(j+1)+" da matriz: ")))
        matriz.append(aux)
    return matriz
def main():
    n = int(input("Digite a ordem da matriz: "))
    matriz = cria_matriz(n)
    w = definir_vetores(matriz)
    v = vetores_ortogonais(w)
    R = np.dot(np.transpose(v), matriz)

    print(np.dot(v, R))
    
main()
