def imprime_matriz(a, l, u, x, z, n):
    print("\n")
    print("A(estendida) = ", end="")
    print(a)
    print("\n")
    print("L = ", end="")
    print(l)
    print("\n")
    print("U = ", end="")
    print(u)
    print("\n")
    print("L*U = ", end="")
    mult_matr(l, u, a, x, z, n)

def mult_matr(L, U, a, x, z, n):
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
    passo_oitavo(a, L, U, x, z, n)

def passo_oitavo(a, l, u, x, z, n):
    print("\n")
    print("SOLUÇÃO Lz = b")
    print("\n")
    for i in range(n):
        print("z(%d):%f " %(i+1, z[i]))
    print("\n")
    print("SOLUÇÃO Ux = z")
    print("\n")
    for i in range(n):
        print("x(%d):%f " %(i+1, x[i]))

def passo_setimo(x, z, u, n):
    for i in range(n-2, -1, -1):
        x[i] = z[i]-u[i][i+1]*x[i+1];
    return x

def passo_sexto(x, z, n):
    x[n-1] = z[n-1]
    return x

def passo_quinto(a, l, z, n):
    for i in range(n):
        z[i] = (1/l[i][i])*(a[i][n]-l[i][i-1]*z[i-1])
    return z

def passo_quarto(a, l, z, n):
    z[0] = a[0][n]/l[0][0]
    return z

def passo_terceiro(a, l, u, n):
    l[n-1][n-2] = a[n-1][n-2]
    l[n-1][n-1] = a[n-1][n-1]-l[n-1][n-2]*u[n-2][n-1]
    return l

def passo_segundo(a, l, u, n):
    for i in range(1, n-1):
        l[i][i-1] = a[i][i-1]
        l[i][i] = a[i][i]-l[i][i-1]*u[i-1][i]
        u[i][i+1] = a[i][i+1]/l[i][i]

    for i in range(n):
        u[i][i] = 1

    return l, u

def passo_primeiro(a, l, u, n):
    for i in range(n):
        linha = []
        for j in range(n):
            if i == 0 and j == 0:
                linha.append(a[0][0])
            else:
                linha.append(0)
        l.append(linha)

    for i in range(n):
        linha = []
        for j in range(n):
            if i == 0 and j == 1:
                linha.append(a[0][1]/l[0][0])
            else:
                linha.append(0)
        u.append(linha)
    return l, u

def cria_matriz(a, n, z, g):
    for i in range(n):
        z.append(0)
        g.append(0)
        linha = []
        for j in range(n):
            if i == j or i-j == 1 or j-i == 1:
                x = float(input("Digite o elemento a%d%d: " %(i+1, j+1)))
                linha.append(x)
            else:
                linha.append(0)
        b = float(input("Digite o elemento b%d: " %(i+1)))
        linha.append(b)
        a.append(linha)
    return a, z, g


def main():
    a = []
    l = []
    u = []
    z = []
    x = []
    
    n = int(input("Digite a ordem da matriz: "))
    a, z, x = cria_matriz(a, n, z, x)
    l, u = passo_primeiro(a, l, u, n)
    l, u = passo_segundo(a, l, u, n)
    l = passo_terceiro(a, l, u, n)
    z = passo_quarto(a, l, z, n)
    z = passo_quinto(a, l, z, n)
    x = passo_sexto(x, z, n)
    x = passo_setimo(x, z, u, n)
    imprime_matriz(a, l, u, x, z, n)
        
main()
