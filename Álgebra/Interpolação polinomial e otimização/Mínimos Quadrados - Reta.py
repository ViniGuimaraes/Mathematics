import numpy as np
import matplotlib.pyplot as plt
from math import floor

def entrada_dados():
    aux = []
    x = []
    y = []
    count = 1
    while True:
        aux.append(input("Digite o par ordenado x"+str(count)+", y"+str(count)+" ou digite p para interromper: "))
        if aux[len(aux)-1]=="p" or aux[len(aux)-1]=="P":
            del aux[len(aux)-1]
            break
        count+=1
    for i in range(len(aux)):
        x.append(aux[i].split(",")[0].strip())
        y.append(aux[i].split(",")[1].strip())
    for i in range(len(aux)):
        x[i] = float(x[i])
        y[i] = float(y[i])
    return x, y

def main():
    x = []
    y = []
    A = 0
    B = 0
    x, y = entrada_dados()

    #Definiremos valores importantes para o funcionamento do método
    N = len(x)
    soma_x = np.sum(x)
    soma_y = np.sum(y)
    soma_xQuadrado = np.sum(np.multiply(x, x))
    soma_xy = np.sum(np.multiply(x, y))

    #Valor do denominador
    delta = N*soma_xQuadrado-(soma_x)**2

    #Definiremos os coeficientes A e B da reta y = A+Bx
    A = (soma_xQuadrado*soma_y-soma_x*soma_xy)/delta
    B = (N*soma_xy-soma_x*soma_y)/delta

    #Definiremos as incertezas associadas às medidas dos coeficientes linear e angular

    #deltaY:
    soma = 0
    for i in range(len(x)):
        soma += (B*x[i]+A-y[i])**2
    deltaY = (soma/(N-2))**(1/2)

    #deltaA e deltaB:
    soma = 0
    for i in range(len(x)):
        soma += (x[i]-(soma_x/N))**2
    deltaA = deltaY*(soma_xQuadrado/(N*soma))**(1/2)
    deltaB = deltaY/(soma)**(1/2)

    print("A = "+str(A))
    print("B = "+str(B))
    print("deltaA = "+str(deltaA))
    print("deltaB = "+str(deltaB))
    

##    if A<0:
##        eq_reta = str(round(B, 2))+"x - "+str(abs(round(A, 2)))
##    else:
##        eq_reta = str(round(B, 2))+"x + "+str(round(A, 2))
##
##    #Vamos traçar a reta
##    
##    fig = plt.figure()
##    ax = fig.add_subplot(111)
##    # ax.spines['left'].set_position(('data', 0))
##    # ax.spines['bottom'].set_position(('data', 0))
##    # ax.spines['right'].set_color('none')
##    # ax.spines['top'].set_color('none')
##    plt.plot(x, y, '.', color='r')
##    x = np.linspace(-A/B-1, np.amax(x)+1, 100)
##    plt.plot(x, B*x+A, 'b', label=eq_reta)
##    plt.legend(loc = 'upper left')
##    plt.show()
    
main()

#As notações aqui utilizadas seguem o padrão do livro "Introdução à análise de erros", de Taylor
