import numpy as np
from fractions import gcd

global congruencias, iDel, jDel
congruencias = []

iDel = 0
jDel = 0

def algoritmo(a, b, c, d):
    inverso = 0
    j = gcd(d, b)

    if d%j == 0 and b%j == 0 and (a-c)%j == 0:

        #Inverso multiplicativo
        for i in range(int(d/j)):
            if int(b/j)*i%int(d/j) == 1:
                inverso = i
        
        p1 = inverso*(b/j)*(c-a) + a
        p2 = (b/j)*(d/j)*j

        del congruencias[iDel]
        del congruencias[jDel]
        congruencias.append((p1, p2))
    else:
        return "Não há solução"

def abcd():
    a = 0
    b = 0
    c = 0
    d = 0

    for i in range(len(congruencias)):
        a = congruencias[i][0]
        b = congruencias[i][1]
        for j in range(len(congruencias)):
            if congruencias[j][0] > congruencias[i][0] and congruencias[j][1] > congruencias[i][1]:
                c = congruencias[j][0]
                d = congruencias[j][1]
                iDel = i
                jDel = j
                return [a, b, c, d]

def entrada(qtd):
    for i in range(qtd):
        x = int(input("Digite a"+str(i+1)+": "))
        y = int(input("Digite b"+str(i+1)+": "))

        congruencias.append((x, y))

def main():
    sistema = []

    qtd = int(input("Digite o número de congruências: "))
    entrada(qtd)
    
    while len(congruencias) != 1:
        sistema = abcd()
        ret = algoritmo(sistema[0], sistema[1], sistema[2], sistema[3])
        if ret == "Não há solução":
            print("Não há solução")
            break
    if ret != "Não há solução":
        atualizado = congruencias[0][0]
        gama = congruencias[0][1]
        while atualizado > congruencias [0][1]:
            atualizado = congruencias[0][0] % congruencias[0][1]

        del congruencias[0]
        congruencias.append((atualizado, gama))
        
        print("x = "+str(congruencias[0][0])+" + "+str(congruencias[0][1])+"k, k inteiro")
    
main()
