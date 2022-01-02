def imprime_matrizes(L, U):
    print("\n")
    print("L = ", end = "")
    print(L)
    print("\n")
    print("U = ", end = "")
    print(U)
    print("\n")

def produtorio(v, i):
    p = 1
    for a in range(i):
        p*=v[a][0][0]
    return p

def matriz_upper(v, n):
    p = 0
    U = []
    for i in range(n):
        linha = []
        for j in range(n):
            if i == 0:
                linha.append(v[0][i][j])
            elif i>j:
                linha.append(0)
            elif i == j:
                p = produtorio(v, i)
                linha.append(v[i][0][0]/p)
            elif j-i>=2:
                linha.append(0)
            else:
                p = produtorio(v, i)
                linha.append(v[i][0][1]/p)
        U.append(linha)
    return U

def matriz_lower(v, n):
    L = []
    for i in range(n):
        linha = []
        for j in range(n):
            if i == j:
                linha.append(1)
            elif i<j:
                linha.append(0)
            elif i-j>=2:
                linha.append(0)
            elif i - j == 1:
                linha.append(v[j][1][0]/v[j][0][0])
        L.append(linha)
    return L      

def novo_centro(v, n):
    lower = []
    upper = []

    lower = matriz_lower(v, n)
    upper = matriz_upper(v, n)

    imprime_matrizes(lower, upper)

def delete(linha):
    return linha.clear()
    
def teste_segundo(v, m):
    v.append(m)
    if len(m) == 1:
        return v, False
    else:
        return v, True

def teste_primeiro(m, linha):
    a = [0]*(len(linha))
    for i in range(0, len(linha)):
        a[i] = linha[i]
    linha.clear()
    m.append(a)
    return m, linha

def sub_matrizes(matriz, linha, v, n):
    ç = 0
    m = []
    for l in range(1, len(matriz)):
        for c in range(1, len(matriz)):
            x = (matriz[0][0]*matriz[l][c])-(matriz[l][0]*matriz[0][c])
            linha.append(x)
        m, linha = teste_primeiro(m, linha)
    v, ç = teste_segundo(v, m)
    if ç == False:
        novo_centro(v, n)
    else:
        sub_matrizes(m, linha, v, n)

def cria_matriz(a, n):
    for i in range(n):
        linha = []
        for j in range(n):
            if i == j or i-j == 1 or j-i == 1:
                x = float(input("Digite o elemento a%d%d: " %(i+1, j+1)))
                linha.append(x)
            else:
                linha.append(0)
        a.append(linha)
    return a

def main():
    while True:
        matriz = []
        linha = []
        v = []
        
        n = int(input("Digite a ordem da matriz: "))
        
        matriz = cria_matriz(matriz, n)
        v.append(matriz)
        v = sub_matrizes(matriz, linha, v, n)
main()
