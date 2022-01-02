def sadoski(v, n, k):
    print(v)
    s = 0
    p1 = v[len(v)-1][0][0]
    pk = 1
    pt = 0
    for i in range(3, n+1):
        s+=1
        for j in range(0, len(v)):
            if len(v[j]) == i:
                pt = (v[j][0][0])**s
                pk*=pt
    if pk == 0:
        print("\n")
        print("det(A) = 0.0")
        print("\n")
    else:
        print("\n")
        print("det(A) = %.2f" %((p1/pk)*(-1)**k))
        print("\n")
    main()

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

def determinantes(matriz, linha, v, n, k):
    ç = 0
    m = []
    for l in range(1, len(matriz)):
        for c in range(1, len(matriz)):
            x = (matriz[0][0]*matriz[l][c])-(matriz[l][0]*matriz[0][c])
            linha.append(x)
        m, linha = teste_primeiro(m, linha)
    v, ç = teste_segundo(v, m)
    if ç == False:
        sadoski(v, n, k)
    else:
        determinantes(m, linha, v, n, k)

def ordem_dois(n):
    l = []
    for i in range(n):
        for j in range(n):
            x = float(input("Digite o elemento a%d%d da matriz: " %(i+1, j+1)))
            l.append(x)
    det = l[0]*l[3]-l[1]*l[2]
    print("\n")
    print("det(A) = %.2f" %det)
    print("\n")
    
def cria_matriz(matriz, n):
    for i in range(n):
        linha = []
        for j in range(n):
            x = float(input("Digite o elemento a%d,%d da matriz: " %(i+1, j+1)))
            linha.append(x)
        matriz.append(linha)
    return matriz
    

def ordem_um():
    a = float(input("Digite o elemento a11 da matriz: "))
    print("\n")
    print("det(A) = %.2f" %a)
    print("\n")

def alteracao(m, k):
    k+=1
    a = []
    for i in range(len(m)):
        a.append(m[i][0])
    for i in range(len(m)):
        m[i][0] = m[i][1]
    for i in range(len(m)):
        m[i][1] = a[i]
    return m, k

def main():
    while True:
        n = int(input("Digite a ordem da matriz: "))
        if n == 1:
            ordem_um()
        elif n == 2:
            ordem_dois(n)
        else:
            m = []
            v = []
            l = []
            k = 0
            
            m = cria_matriz(m, n)
            if m[0][0] == 0:
                m, k = alteracao(m, k)
            v.append(m)
            determinantes(m, l, v, n, k)
main()
