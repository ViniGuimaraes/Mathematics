def nao_conhecido(c_pol, S, n, p):
    soma = 0
    cont=p-1
    for i in range(n):
        soma+=(-1)*(S[cont]*c_pol[i+1])
        cont-=1
    soma = soma/c_pol[0]
    S.append(soma)
    return S
    

def main():
    n = int(input("Digite o grau do polinômio: "))
    p = int(input("Digite a potencia desejada: "))
    print("\n")
    c_pol = []
    c_der = []
    S = []
    P = []

    for i in range(0, n+1):
        c_pol.append(float(input("Digite o termo a%d do polinômio: " %(n-i))))

    print("\n")

    for i in range(0, n):
        c_der.append(float(input("Digite o termo a%d da derivada: " %(n-1-i))))
    c_der.append(0)

    print("\n")

    for i in range(0, n+1):
        q = c_der[0]/c_pol[0]
        S.append(q)

        for j in range(0, len(c_pol)):
            P.append(q*c_pol[j])

        for j in range(0, len(c_der)):
            c_der[j] = c_der[j]-P[j]
        P.clear()
        for j in range(0, len(c_der)-1):
            aux = c_der[j+1]
            c_der[j+1] = c_der[j]
            c_der[j] = aux

    if p-n<=0 and p>=0:
        print("Soma das potências das raízes^"+str(p)+" = ", end = "")
        print(S[p])
    if p<0:
        pass
    if p-n==1:
        S = nao_conhecido(c_pol, S, n, p)
        print("Soma das potências das raízes^"+str(p)+" = ", end = "")
        print(S[p])
    if p-n>=2:
        for i in range(1+n, p+1):
            S = nao_conhecido(c_pol, S, n, i)
        print("Soma das potências das raízes^"+str(p)+" = ", end = "")
        print(S[p])
main()
