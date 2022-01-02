import numpy as np

def vetores_ortogonais(w):
    v = []
    v.append(w[0])
    for i in range(1, len(w)):
        c = [0]*len(w[0])
        for j in range(0, i):
            a = np.dot(w[i], v[j])
            b = np.dot(v[j], v[j])
            q = a/b
            matrix = np.dot(q, v[j])
            c = np.add(matrix, c)
        v.append(np.subtract(w[i], c))
    print(v)

def preencher_vetores(m, n):
    vet = []
    aux = []
    for i in range(m):
        aux = []
        for j in range(n):
            aux.append(float(input("Digite o elemento a"+str(j+1)+" do "+str(i+1)+"º"+" vetor: ")))
        vet.append(aux)
    return vet

def main():
    m = int(input("Digite a quantidade de vetores: "))
    n = int(input("Digite a dimensão dos vetores: "))

    vetores = preencher_vetores(m, n)
    A = np.transpose(vetores)
    print(vetores)
    vetores_ortogonais(vetores)
    
main()
