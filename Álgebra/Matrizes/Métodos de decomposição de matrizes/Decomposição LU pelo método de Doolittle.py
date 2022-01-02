def mult_matr(L, U):
    num_linhas_L, num_colunas_L = len(L), len(L)
    num_linhas_U, num_colunas_U = len(U), len(U)
    C = []

    for linha in range(0, num_linhas_L):
        C.append([])
        for coluna in range(num_colunas_U):
            C[linha].append(0)
            for k in range(num_colunas_L):
                C[linha][coluna] += L[linha][k]*U[k][coluna]
    print(C)

def impressao(L, U):
    print("\n")
    print("L = ", end="")
    print(L)
    print("\n")
    print("U = ", end="")
    print(U)
    print("\n")
    print("L*U = ", end="")
    mult_matr(L, U)
    print("\n")
    

def somatorio_ultimo(n, L, U):
    s = 0
    for k in range(0, n):
        s+=L[n-1][k]*U[k][n-1]
    return s

def somatorio_d(L, U, m, i):
    s = 0
    for k in range(0, m):
        s+=L[i][k]*U[k][m]
    return s

def somatorio(L, U, m, j):
    s = 0
    for k in range(0, m):
        s+=L[m][k]*U[k][j]
    return s
    

def algoritmo(L, U, matriz, n):
    for i in range(0, len(U)):
        U[0][i] = matriz[0][i]
        
    for i in range(1, len(L)):
        L[i][0] = matriz[i][0]/U[0][0]

    for m in range(0, n-1):
        for j in range(m, n):
            s = somatorio(L, U, m, j)
            U[m][j] = matriz[m][j]-s

    for m in range(0, n-1):
        for i in range(m+1, n):
            s = somatorio_d(L, U, m, i)
            L[i][m] = (matriz[i][m]-s)/U[m][m]

    s = 0
    s = somatorio_ultimo(n, L, U)
    U[n-1][n-1] = matriz[n-1][n-1]-s

    impressao(L, U)
    
def zera(L, U, n):
    for i in range(n):
        l = [0]*n
        L.append(l)
        
    for i in range(n):
        l = [0]*n
        U.append(l)

    for i in range(n):
        for j in range(n):
            if i == j:
                L[i][j] = 1
    return L, U

def cria_matriz(matriz, n):
    for i in range(n):
        linha = []
        for j in range(n):
            x = float(input("Digite o elemento a%d,%d da matriz: " %(i+1, j+1)))
            linha.append(x)
        matriz.append(linha)
    return matriz

def main():
    while True:
        n = int(input("Digite a ordem da matriz: "))
        matriz = []
        matriz = cria_matriz(matriz, n)
        L = []
        U = []
        L, U = zera(L, U, n)
        algoritmo(L, U, matriz, n)
main()
