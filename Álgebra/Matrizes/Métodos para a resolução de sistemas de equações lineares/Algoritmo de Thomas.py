import copy
def imprimir(X):
    print("\n")
    print("SOLUÇÕES DO SISTEMA Ax = b")
    print("\n")
    for i in range(len(X)):
        print("x%d = " %(i+1), end = "")
        print(X[i])
    print("\n")

def thomas(A, b):
    n = len(b)
    terms = copy.deepcopy(b)
    x = []
    d = []
    upper = []
    lower = []
 
    for i in range(n):
        d.append(A[i][i])
        x.append(0.0)
        upper.append(0.0)
        lower.append(0.0)
    for i in range(n - 1):
        upper[i] = A[i][i + 1]
        lower[i] = A[i + 1][i]
 
    for i in range(1, n):
        d[i] = d[i] - lower[i - 1] * upper[i - 1] / d[i - 1]
        terms[i] = terms[i] - lower[i - 1] * terms[i - 1] / d[i - 1]
    x[n - 1] = terms[n - 1] / d[n - 1]
 
    for i in range(n - 2, -1, -1):
        x[i] = (terms[i] - upper[i] * x[i + 1]) / d[i]
    return x

def cria_matriz(A, b, n):
    for i in range(n):
        linha = []
        for j in range(n):
            if i == j or i-j == 1 or j-i == 1:
                x = float(input("Digite o elemento a%d%d: " %(i+1, j+1)))
                linha.append(x)
            else:
                linha.append(0)
        y = float(input("Digite o elemento b%d: " %(i+1)))
        b.append(y)
        A.append(linha)
    return A, b

def main():
    while True:
        A = []
        b = []
        X = []
        n = int(input("Digite a ordem da matriz: "))
        A, b = cria_matriz(A, b, n)
        X = thomas(A, b)
        imprimir(X)
main()
