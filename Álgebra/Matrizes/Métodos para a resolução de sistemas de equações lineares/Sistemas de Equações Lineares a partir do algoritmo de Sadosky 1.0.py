import numpy as np

def imprimir_solucoes(x):
    print("\n")
    print("SOLUCÕES")
    print("\n")
    for i in range(0, len(x)):
        print("x%d = %s" %(i+1, x[i]))
    print("\n")

def vet_sol(A):
    n = len(A)
    x = [0]*n
    for i in range(n-1, -1, -1):
        s = sum([A[i][j]*x[j] for j in range(i+1, n)])
        x[i] = (A[i][n]-s)/A[i][i]
    imprimir_solucoes(x)
    
def pre_gauss(v, n, k, b):
    A = []
    for i in range(0, len(v)):
        if len(v[i]) < len(v):
            n = len(v) - len(v[i])
            l = [0]*n
            for j in range(0, len(v[i][len(v[i])-1])):
                l.append(v[i][len(v[i])-1][j])
            A.append(l)
        else:
            A.append(v[i][len(v[i])-1])
    for i in range(0, len(A)):
        A[i].append(b[i][len(b[i])-1])

    vet_sol(A)

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

def bs(matriz, b, s):
    a = 0
    t = []
    for i in range(1, len(matriz)):
        a = matriz[0][0]*s[i]-matriz[i][0]*s[0]
        t.append(a)
    b.append(t)
    return b, t
        

def determinantes(matriz, linha, v, n, k, b, s):
    ç = 0
    m = []
    for l in range(1, len(matriz)):
        for c in range(1, len(matriz)):
            x = (matriz[0][0]*matriz[l][c])-(matriz[l][0]*matriz[0][c])
            linha.append(x)
        m, linha = teste_primeiro(m, linha)
    v, ç = teste_segundo(v, m)
    b, s = bs(matriz, b, s)
    if ç == False:
        pre_gauss(v, n, k, b)
    else:
        determinantes(m, linha, v, n, k, b, s)

def cria_matriz(matriz, n):
    a = []
    for i in range(n):
        linha = []
        for j in range(n+1):
            if j == n:
                x = float(input("Digite o elemento b%d: " %(i+1)))
                a.append(x)
            else:
                x = float(input("Digite o elemento a%d,%d da matriz: " %(i+1, j+1)))
                linha.append(x)
        matriz.append(linha)
    return matriz, a
    

def ordem_um():
    a = float(input("Digite o elemento a11 da matriz: "))
    b = float(input("Digite o elemento b1: "))
    if a == 0:
        print("\n")
        print("Sistema possível e indeterminado ou sistema impossível")
        print("\n")
    else:
        print("\n")
        print("x1 = %.2f" %(b/a))
        print("\n")

def main():
    while True:
        n = int(input("Digite a ordem da matriz: "))
        if n == 1:
            ordem_um()
        else:
            m = []
            v = []
            l = []
            k = 0
            x = []
            b = []
            
            m, x = cria_matriz(m, n)
            if round(np.linalg.det(m))==0:
                print("\n")
                print("Sistema possível e indeterminado ou sistema impossível")
                print("\n")
            else:
                b.append(x)
                v.append(m)
                determinantes(m, l, v, n, k, b, x)
main()
