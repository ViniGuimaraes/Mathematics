import numpy as np

def metodo_Leverrier_Faddeev(matriz, n):
    An = []
    I = np.identity(n)
    qn = np.trace(matriz)
    Bn_1 = np.subtract(matriz, np.dot(qn, I))
    for a in range(n-1):
        if a == n-2:
            An = np.dot(matriz, Bn_1)
            qn = (1/n)*np.trace(An)
            return Bn_1, qn
        else:
            An = np.dot(matriz, Bn_1)
            qn = (1/(a+2))*np.trace(An)
            Bn_1 = np.subtract(An, np.dot(qn, I))
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
    if round(np.linalg.det(matriz))==0:
        print("\n")
        print("A matriz inserida não é invertível, pois seu determinante é igual a zero")
        print("\n")
    else:
        B_n_1 = []
        qn = 0
        B_n_1, qn = metodo_Leverrier_Faddeev(matriz, n)
        inversa = np.dot(1/qn, B_n_1)
        print(inversa)
main()
