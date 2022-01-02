import numpy as np

def ordem_superior(matriz, gama, phi_n_1, C_n_2):
    inversa = []
    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz)):
            s = 0
            for l in range(len(matriz)):
                s+=matriz[i][l]*C_n_2[l][j]
            if i == j:
                linha.append((1/gama)*(s+phi_n_1))
            else:
                linha.append((1/gama)*s)
        inversa.append(linha)
    return inversa
            
def complementar(matriz, phi, C):
    Coutra = []
    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz)):
            s = 0
            for l in range(len(matriz)):
                s+=matriz[i][l]*C[l][j]
            if i == j:
                linha.append(phi+s)
            else:
                linha.append(s)
        Coutra.append(linha)
    return Coutra
    
def phi_complementar(matriz, phi, C):
    cont = 0
    for v in range(len(matriz)-2):
        cont+=1
        s1 = 0
        for i in range(len(matriz)):
            s2 = 0
            for j in range(len(matriz)):
                s2+=matriz[i][j]*C[j][i]
            s1+=s2
        phi = ((-1)/(v+2))*s1

        if cont==len(matriz)-2:
            return phi, C
        else:
            C = complementar(matriz, phi, C)
    return phi, C

def complementar_primeira(matriz, phi_1):
    C = []
    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz)):
            if i==j:
                linha.append(phi_1+matriz[i][j])
            else:
                linha.append(matriz[i][j])
        C.append(linha)
    return C

def ordem_dois(matriz, phi_1, gama):
    inversa = []
    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz)):
            if i==j:
                linha.append((matriz[i][j]+phi_1)/gama)
            else:
                linha.append((matriz[i][j])/gama)
        inversa.append(linha)
    return inversa
                
def gamaCalculo(matriz, n):
    if n%2==0:
        return round((-1)*(np.linalg.det(matriz)))
    else:
        return round(np.linalg.det(matriz))

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
    inversa = []
    
    n = int(input("Digite a ordem da matriz: "))
    matriz = cria_matriz(n)

    if round(np.linalg.det(matriz))==0:
        print("\n")
        print("A matriz inserida não é invertível, pois seu determinante é igual a zero")
        print("\n")
    else:
        gama = gamaCalculo(matriz, n)
        phi_1 = (-1)*np.trace(matriz)
        if n == 2:
            inversa = ordem_dois(matriz, phi_1, gama)
            print(inversa)
        else:
            C_1 = []
            C_1 = complementar_primeira(matriz, phi_1)
            phi_n_1, C_n_2 = phi_complementar(matriz, phi_1, C_1)
            inversa = ordem_superior(matriz, gama, phi_n_1, C_n_2)
            print(inversa)
main()
