from math import gcd

def egcd(a, b):
    x = 0
    y = 0
    if a == 0:
        return 0, 1
    else:
        x, y = egcd(b%a, a)
        return y-(b//a)*x, x

def crt_especifico(a, m):
    N = 1
    N_a = []
    for i in range(len(m)):
        N*=m[i]
    for i in range(len(m)):
        produtorio = 1
        for j in range(len(m)):
            if i!=j:
                produtorio*=m[j]
        N_a.append(produtorio)
    inversos = []
    for i in range(len(N_a)):
        for j in range(m[i]+1):
            if j*N_a[i]%m[i] == 1:
                inversos.append(j)
                break
    x = 0
    for i in range(len(N_a)):
        x += N_a[i]*inversos[i]*a[i]
    x = x%N
    solucao = []
    solucao.append(x)
    solucao.append(N)
    return solucao

def crt_geral(a, m):
    n = len(a)
    a1 = a[0]
    m1 = m[0]

    for i in range(1, n):
        a2 = a[i]
        m2 = m[i]

        g = gcd(m1, m2)
        if a1%g!=a2%g:
            return [-1, -1]
        p = 0
        q = 0
        p, q = egcd(m1/g, m2/g)
        p = int(p)
        q = int(q)

        mod = (m1/g)*m2
        mod = int(mod)

        x = (a1*(m2/g)*q+a2*(m1/g)*p)%mod

        a1 = x
        if a1<0:
            a1+=mod
        m1 = mod
        a1 = int(a1)
    return [a1, m1]


def main():
    eqs = int(input("Digite o número de equações do sistema: "))
    a = []
    m = []
    S = []

    escolha = True
    
    for i in range(eqs):
        a.append(int(input("Digite a"+str(i+1)+": ")))
        m.append(int(input("Digite m"+str(i+1)+": ")))
    for i in range(len(m)-1):
        for j in range(i+1, len(m)):
            if gcd(m[i], m[j])!=1:
                escolha = False
    if escolha == True:
        S = crt_especifico(a, m)
        print("S = { "+str(S[0])+" +- "+str(S[1])+"n, n natural }")
    else:
        S = crt_geral(a, m)
        print("S = { "+str(S[0])+" +- "+str(S[1])+"n, n natural }")
main()
