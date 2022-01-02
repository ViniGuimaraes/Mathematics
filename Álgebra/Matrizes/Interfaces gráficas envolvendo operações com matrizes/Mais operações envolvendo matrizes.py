from tkinter import *
from functools import partial
from scipy.linalg import lu
import numpy as np

def solucao_sist_lin(tfMatriz, tfEntradas, n):
    A = []
    B = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(float(tfMatriz[i][j].get()))
        A.append(aux)

    for i in range(n):
        B.append(float(tfEntradas[i].get()))

    lbVazioj = Label(janela)
    lbVazioj.grid(row = 8, column = 0)
    
    frSolucoes = Frame(janela)
    frSolucoes.grid(row = 9, column = 0, columnspan = 3)

    x = np.linalg.solve(A, B)

    X = []
    for i in range(n):
        X.append(Label(frSolucoes, text = str("{:.6f}".format(x[i]))))

    lbVazio = Label(frSolucoes)

    lbSol = Label(frSolucoes, text = "Soluções")
    lbSol.grid(row = 0, column = 0)
    lbVazio.grid(row = 1, column = 0)

    lbSolucoes = []
    for i in range(n):
        lbSolucoes.append(Label(frSolucoes, text = "x"+str(i+1)))
    lbIguais = []
    for i in range(n):
        lbIguais.append(Label(frSolucoes, text = "="))

    for i in range(n):
        lbSolucoes[i].grid(row = 2+i, column = 0)
        lbIguais[i].grid(row = 2+i, column = 1)
        X[i].grid(row = 2+i, column = 3)

def construir_sist_lin(tfOrdem):
    n = int(tfOrdem.get())
    lbVazio = Label(janela)
    lbVazio.grid(row = 6, column = 0)
    
    frMatriz = Frame(janela)
    frMatriz.grid(row = 7, column = 0, columnspan = 3)

    tfmatriz = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(Entry(frMatriz, width = 5))
        tfmatriz.append(aux)

    tfEntradas = []
    for i in range(n):
        tfEntradas.append(Entry(frMatriz, width = 5))

    lbIguais = []
    for i in range(n):
        lbIguais.append(Label(frMatriz, text = "="))

    lbVariaveis = []
    for i in range(n):
        aux = []
        for j in range(n):
            if j == n-1:
                aux.append(Label(frMatriz, text = "x"+str(j+1)))
            else:
                aux.append(Label(frMatriz, text = "x"+str(j+1)+"+"))
        lbVariaveis.append(aux)
    cont = 0
    linhas = 0
    for i in range(n):
        linhas = i
        cont = 0
        for j in range(n):
            tfmatriz[i][j].grid(row = i, column = j+cont, padx = 5, pady = 5)
            lbVariaveis[i][j].grid(row = i, column = j+cont+1, padx = 5, pady = 5)
            if j == n-1:
                lbIguais[i].grid(row = i, column = j+cont+2, padx = 5, pady = 5)
                tfEntradas[i].grid(row = i, column = j+cont+3, padx = 5, pady = 5)
            cont+=1
            
    btSolucionar = Button(frMatriz, text = "Solucionar", command = partial(solucao_sist_lin, tfmatriz, tfEntradas, n))
    btSolucionar.grid(row = linhas+1, column = 0)

def construir_sist_lin_tri(tfOrdem):
    n = int(tfOrdem.get())
    lbVazio = Label(janela)
    lbVazio.grid(row = 6, column = 0)
    
    frMatrizTri = Frame(janela)
    frMatrizTri.grid(row = 7, column = 0, columnspan = 3)

    tfmatriztriL = []
    tfmatriztriT = []
    for i in range(n):
        auxL = []
        auxT = []
        for j in range(n):
            a = Entry(frMatrizTri, width = 5)
            if abs(i-j)>=2:
                auxL.append(Label(frMatrizTri, text = "0", font = "bold"))
                a.insert(END, "0")
                auxT.append(a)
            else:
                auxL.append(a)
                auxT.append(a)
        tfmatriztriL.append(auxL)
        tfmatriztriT.append(auxT)

    tfEntradas = []
    for i in range(n):
        tfEntradas.append(Entry(frMatrizTri, width = 5))

    lbIguais = []
    for i in range(n):
        lbIguais.append(Label(frMatrizTri, text = "="))

    lbVariaveis = []
    for i in range(n):
        aux = []
        for j in range(n):
            if j == n-1:
                aux.append(Label(frMatrizTri, text = "x"+str(j+1)))
            else:
                aux.append(Label(frMatrizTri, text = "x"+str(j+1)+"+"))
        lbVariaveis.append(aux)
    cont = 0
    linhas = 0
    for i in range(n):
        linhas = i
        cont = 0
        for j in range(n):
            tfmatriztriL[i][j].grid(row = i, column = j+cont, padx = 5, pady = 5)
            lbVariaveis[i][j].grid(row = i, column = j+cont+1, padx = 5, pady = 5)
            if j == n-1:
                lbIguais[i].grid(row = i, column = j+cont+2, padx = 5, pady = 5)
                tfEntradas[i].grid(row = i, column = j+cont+3, padx = 5, pady = 5)
            cont+=1
            
    btSolucionar = Button(frMatrizTri, text = "Solucionar", command = partial(solucao_sist_lin, tfmatriztriT, tfEntradas, n))
    btSolucionar.grid(row = linhas+1, column = 0)

def construir_LU(tfOrdem):
    n = int(tfOrdem.get())
    lbVazio = Label(janela)
    lbVazio.grid(row = 6, column = 0)
    
    frMatriz = Frame(janela)
    frMatriz.grid(row = 7, column = 0, columnspan = 3)

    tfmatriz = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(Entry(frMatriz, width = 5))
        tfmatriz.append(aux)
    linhas = 0
    for i in range(n):
        linhas = i
        for j in range(n):
            tfmatriz[i][j].grid(row = i, column = j, padx = 15, pady = 5)
    
    btSolucionar = Button(frMatriz, text = "Decompor", command = partial(decomposicao_LU_solucao, tfmatriz, n))
    btSolucionar.grid(row = linhas+1, column = 0)

def construir_QR(tfOrdem):
    n = int(tfOrdem.get())
    lbVazio = Label(janela)
    lbVazio.grid(row = 6, column = 0)
    
    frMatriz = Frame(janela)
    frMatriz.grid(row = 7, column = 0, columnspan = 3)

    tfmatriz = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(Entry(frMatriz, width = 5))
        tfmatriz.append(aux)
    linhas = 0
    for i in range(n):
        linhas = i
        for j in range(n):
            tfmatriz[i][j].grid(row = i, column = j, padx = 15, pady = 5)
    
    btSolucionar = Button(frMatriz, text = "Decompor", command = partial(decomposicao_QR_solucao, tfmatriz, n))
    btSolucionar.grid(row = linhas+1, column = 0)

def construir_auto(tfOrdem):
    n = int(tfOrdem.get())
    lbVazio = Label(janela)
    lbVazio.grid(row = 6, column = 0)
    
    frMatriz = Frame(janela)
    frMatriz.grid(row = 7, column = 0, columnspan = 3)

    tfmatriz = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(Entry(frMatriz, width = 5))
        tfmatriz.append(aux)
    linhas = 0
    for i in range(n):
        linhas = i
        for j in range(n):
            tfmatriz[i][j].grid(row = i, column = j, padx = 15, pady = 5)
    
    btSolucionar = Button(frMatriz, text = "Solucionar", command = partial(autovalores_autovetores_solucao, tfmatriz, n))
    btSolucionar.grid(row = linhas+1, column = 0)
    
def decomposicao_LU_solucao(tfMatriz, n):
    def somatorio(L, U, m, j):
        s = 0
        for k in range(0, m):
            s+=L[m][k]*U[k][j]
        return s

    def somatorio_d(L, U, m, i):
        s = 0
        for k in range(0, m):
            s+=L[i][k]*U[k][m]
        return s

    def somatorio_ultimo(n, L, U):
        s = 0
        for k in range(0, n):
            s+=L[n-1][k]*U[k][n-1]
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
        return L, U

    A = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(float(tfMatriz[i][j].get()))
        A.append(aux)

    L = []
    U = []

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
    L, U = algoritmo(L, U, A, n)
   
    
    lbVazioj = Label(janela)
    lbVazioj.grid(row = 8, column = 0)
    
    frSolucoes = Frame(janela)
    frSolucoes.grid(row = 9, column = 0, columnspan = 3)


    lbVazio = Label(frSolucoes)

    lbLower = Label(frSolucoes, text = "Matriz Lower(L)")
    lbUpper = Label(frSolucoes, text = "Matriz Upper(U)")
    lbProduct = Label(frSolucoes, text = "LU")
    
    lbLower.grid(row = 0, column = 0)
    lbVazio.grid(row = 1, column = 0)

    lbvLower = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(Label(frSolucoes, text = "{:.6f}".format(L[i][j])))
        lbvLower.append(aux)
        
    lbvUpper = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(Label(frSolucoes, text = "{:.6f}".format(U[i][j])))
        lbvUpper.append(aux)

    lbvProduct = []
    Product = np.dot(L, U)
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(Label(frSolucoes, text = "{:.6f}".format(Product[i][j])))
        lbvProduct.append(aux)

    linhas = 0
    for i in range(n):
        linhas = i
        for j in range(n):
            lbvLower[i][j].grid(row = 2+i, column = j, padx = 15, pady = 5)
            
    lbVazio.grid(row = 3+linhas, column = 0)
    lbUpper.grid(row = 4+linhas, column = 0)
    for i in range(n):
        for j in range(n):
            lbvUpper[i][j].grid(row = 5+linhas+i, column = j, padx = 15, pady = 5)
    lbVazioNovo = Label(frSolucoes)
    lbVazioNovo.grid(row = 6+2*linhas, column = 0)
    lbProduct.grid(row = 7+2*linhas, column = 0)
    for i in range(n):
        linhas+=1
        for j in range(n):
            lbvProduct[i][j].grid(row = 8+2*linhas+i, column = j, padx = 15, pady = 5)

def decomposicao_QR_solucao(tfMatriz, n):
    A = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(float(tfMatriz[i][j].get()))
        A.append(aux)

    Q = []
    R = []

    Q, R = np.linalg.qr(A)
    
    lbVazioj = Label(janela)
    lbVazioj.grid(row = 8, column = 0)
    
    frSolucoes = Frame(janela)
    frSolucoes.grid(row = 9, column = 0, columnspan = 3)


    lbVazio = Label(frSolucoes)

    lbQ = Label(frSolucoes, text = "Q")
    lbR = Label(frSolucoes, text = "R")
    lbProduct = Label(frSolucoes, text = "QR")
    
    lbQ.grid(row = 0, column = 0)

    lbvQ = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(Label(frSolucoes, text = "{:.6f}".format(Q[i][j])))
        lbvQ.append(aux)
        
    lbvR = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(Label(frSolucoes, text = "{:.6f}".format(R[i][j])))
        lbvR.append(aux)

    lbvProduct = []
    Product = np.dot(Q, R)
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(Label(frSolucoes, text = "{:.6f}".format(Product[i][j])))
        lbvProduct.append(aux)

    linhas = 0
    for i in range(n):
        linhas = i
        for j in range(n):
            lbvQ[i][j].grid(row = 2+i, column = j, padx = 15, pady = 5)
            
    lbVazio.grid(row = 3+linhas, column = 0)
    lbR.grid(row = 4+linhas, column = 0)
    for i in range(n):
        for j in range(n):
            lbvR[i][j].grid(row = 5+linhas+i, column = j, padx = 15, pady = 5)
    lbVazioNovo = Label(frSolucoes)
    lbVazioNovo.grid(row = 6+2*linhas, column = 0)
    lbProduct.grid(row = 7+2*linhas, column = 0)
    for i in range(n):
        linhas+=1
        for j in range(n):
            lbvProduct[i][j].grid(row = 8+2*linhas+i, column = j, padx = 15, pady = 5)

def autovalores_autovetores_solucao(tfMatriz, n):
    A = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(float(tfMatriz[i][j].get()))
        A.append(aux)

    autovalores = []
    autovetores = []

    autovalores, autovetores = np.linalg.eig(A)

    lbVazioj = Label(janela)
    lbVazioj.grid(row = 8, column = 0)
    
    frSolucoes = Frame(janela)
    frSolucoes.grid(row = 9, column = 0, columnspan = 3)

    lbVazio = Label(frSolucoes)

    lbAutoVal = Label(frSolucoes, text = "Autovalores")
    lbAutoVet = Label(frSolucoes, text = "Autovetores")

    lbAutoVal.grid(row = 0, column = 0)

    lbvAutoVal = []
    for i in range(n):
        lbvAutoVal.append(Label(frSolucoes, text = "{:.6f}".format(autovalores[i])))

    lbvAutoVet = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(Label(frSolucoes, text = "{:.6f}".format(autovetores[i][j])))
        lbvAutoVet.append(aux)

    for i in range(n):
        lbvAutoVal[i].grid(row = 2, column = i, padx = 15, pady = 5)

    lbVazio.grid(row = 3, column = 0)
    lbAutoVet.grid(row = 4, column = 0)

    for i in range(n):
        for j in range(n):
            lbvAutoVet[i][j].grid(row = 5+i, column = j, padx = 15, pady = 5)
    
def autovalores_autovetores():
    lbOrdem = Label(janela, text = "Ordem da matriz")
    tfOrdem = Entry(janela)
    btOK = Button(janela, text = "OK", command = partial(construir_auto, tfOrdem), width = 25)

    lbOrdem.grid(row = 5, column = 0)
    tfOrdem.grid(row = 5, column = 1)
    btOK.grid(row = 5, column = 2, padx = 10)

def decomposicao_QR():
    lbOrdem = Label(janela, text = "Ordem da matriz")
    tfOrdem = Entry(janela)
    btOK = Button(janela, text = "OK", command = partial(construir_QR, tfOrdem), width = 25)

    lbOrdem.grid(row = 5, column = 0)
    tfOrdem.grid(row = 5, column = 1)
    btOK.grid(row = 5, column = 2, padx = 10)

def decomposicao_LU():
    lbOrdem = Label(janela, text = "Ordem da matriz")
    tfOrdem = Entry(janela)
    btOK = Button(janela, text = "OK", command = partial(construir_LU, tfOrdem), width = 25)

    lbOrdem.grid(row = 5, column = 0)
    tfOrdem.grid(row = 5, column = 1)
    btOK.grid(row = 5, column = 2, padx = 10)

def sistemas_lineares_tridiagonais():
    lbOrdem = Label(janela, text = "Ordem do sistema tridiagonal")
    tfOrdem = Entry(janela)
    btOK = Button(janela, text = "OK", command = partial(construir_sist_lin_tri, tfOrdem), width = 25)

    lbOrdem.grid(row = 5, column = 0)
    tfOrdem.grid(row = 5, column = 1)
    btOK.grid(row = 5, column = 2, padx = 10)

def sistemas_lineares():
    lbOrdem = Label(janela, text = "Ordem do sistema")
    tfOrdem = Entry(janela)
    btOK = Button(janela, text = "OK", command = partial(construir_sist_lin, tfOrdem), width = 25)

    lbOrdem.grid(row = 5, column = 0)
    tfOrdem.grid(row = 5, column = 1)
    btOK.grid(row = 5, column = 2, padx = 10)

janela = Tk()

btSistemasLineares = Button(janela, text = "Sistemas Lineares", width = 25, command = sistemas_lineares)
btSistemasLinearesTridiagonais = Button(janela, text = "Sistemas Lineares Tridiagonais", width = 25, command = sistemas_lineares_tridiagonais)
btLU = Button(janela, text = "Decomposição LU", width = 25, command = decomposicao_LU)
btQR = Button(janela, text = "Decomposição QR", width = 25, command = decomposicao_QR)
btAuto = Button(janela, text = "Autovalores e Autovetores", width = 25, command = autovalores_autovetores)

btSistemasLineares.grid(row = 0, column = 0)
btSistemasLinearesTridiagonais.grid(row = 1, column = 0)
btLU.grid(row = 2, column = 0)
btQR.grid(row = 3, column = 0)
btAuto.grid(row = 4, column = 0)

janela.mainloop()
