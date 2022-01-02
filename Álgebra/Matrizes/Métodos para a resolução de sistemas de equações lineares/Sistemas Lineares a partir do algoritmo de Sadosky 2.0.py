import numpy as np
from copy import deepcopy

def imprimir_resultados(solucoes):
    solucoes = solucoes[::-1]
    print("")
    for i in range(len(solucoes)):
        print("x"+str(i+1)+" = "+str(solucoes[i]))

def sistema_linear_solucao(sistema_linear):
    solucao = []
    for i in range(0, len(sistema_linear)):
        soma = 0
        for j in range(i):
            soma+=solucao[j]*sistema_linear[i][len(sistema_linear[i])-2-j]
        solucao.append((sistema_linear[i][len(sistema_linear[i])-1]-soma)/sistema_linear[i][0])
    return solucao

def forma_sistema(sub_matrizes):
    sistema = []
    for i in range(len(sub_matrizes)):
        sistema.append(sub_matrizes[i][0])
    return sistema

def n_1_matrizes(matriz_estendida, n):
    matriz_estendida = np.array(matriz_estendida)
    m2 = [0]*n
    m2[n-1] = deepcopy(matriz_estendida)

    if m2[n-1][0][0] == 0:
        nova_linha = []
        encontrou = False
        for i in range(1, n):
            if m2[n-1][i][0]!=0:
                nova_linha = deepcopy(m2[n-1][i])
                m2[n-1][i] = m2[n-1][0]
                m2[n-1][0] = nova_linha
                encontrou = True
                break
        if encontrou==False:
            nova_coluna = []
            for j in range(1, n):
                if m2[n-1][0][j] !=0:
                    nova_coluna = deepcopy(m2[n-1][:,i])
                    m2[n-1][:,i] = m2[n-1][:,0]
                    m2[n-1][:,0] = nova_coluna
    for t in range(n-2, -1, -1):
        aux = []
        for i in range(t+1):
            linha = []
            for j in range(t+2):
                linha.append(round(np.linalg.det([[m2[t+1][0][0], m2[t+1][0][j+1]],[m2[t+1][i+1][0], m2[t+1][i+1][j+1]]])))
            aux.append(linha)
        m2[t] = deepcopy(aux)
        if t!=0:
            if m2[t][0][0] == 0:
                nova_linha = []
                encontrou = False
                for i in range(1, t+1):
                    if m2[t][i][0]!=0:
                        nova_linha = deepcopy(m2[t][i])
                        m2[t][i] = m2[t][0]
                        m2[t][0] = nova_linha
                        encontrou = True
                        break
                if encontrou==False:
                    nova_coluna = []
                    for j in range(1, t+1):
                        if m2[t][0][j] !=0:
                            nova_coluna = deepcopy(m2[t][:,i])
                            m2[t][:,i] = m2[t][:,0]
                            m2[t][:,0] = nova_coluna
        else:
            aux = []
            for i in range(t+1):
                linha = []
                for j in range(t+2):
                    linha.append(round(np.linalg.det([[m2[t+1][0][0], m2[t+1][0][j+1]],[m2[t+1][i+1][0], m2[t+1][i+1][j+1]]])))
                aux.append(linha)
            m2[t] = deepcopy(aux)
            return m2

def cria_matriz(n):
    matriz_estendida = []
    matriz_determinante = []
    for i in range(n):
        linha = []
        linha_determinante = []
        for j in range(n+1):
            if j == n:
                x = float(input("Digite o elemento b%d: " %(i+1)))
                linha.append(x)
            else:
                x = float(input("Digite o elemento a%d,%d da matriz: " %(i+1, j+1)))
                linha.append(x)
                linha_determinante.append(x)
        matriz_estendida.append(linha)
        matriz_determinante.append(linha_determinante)
    return matriz_estendida, matriz_determinante

def main():
    matriz_estendida = []
    matriz_determinante = []
    sub_matrizes = []
    sistema_linear = []
    solucoes = []

    n = int(input("Digite a ordem do sistema: "))
    matriz_estendida, matriz_determinante = cria_matriz(n)
    # if round(np.linalg.det(matriz_determinante)) == 0:
    #     print("Sistema possível e indeterminado ou sistema impossível")
    # else:
    sub_matrizes = n_1_matrizes(matriz_estendida, n)
    sistema_linear = forma_sistema(sub_matrizes)
    solucoes = sistema_linear_solucao(sistema_linear)
    imprimir_resultados(solucoes)

main()