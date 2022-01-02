import math
import numpy as np

def propriedade_diagonalizavel(matriz, vetor1, vetor2, vetor3, autovalores, n):
    if n == 2:
        P = [[vetor1[0], vetor2[0]],[vetor1[1], vetor2[1]]]
    if n == 3:
        P = [[vetor1[0], vetor2[0], vetor3[0]], [vetor1[1], vetor2[1], vetor3[1]], [vetor1[2], vetor2[2], vetor3[2]]]
    if abs(np.linalg.det(P)) < 10**(-5):
        print("A matriz não é diagonalizável")
    else:
        P_1 = np.linalg.inv(P)
        M = np.dot(P_1, matriz)
        D = np.dot(M, P)
        print("A matriz é diagonalizável: ")
        print(D)

def propriedade_soma(autovalores, matriz):
    s = 0
    for i in range(len(autovalores)):
        s+=autovalores[i]
    if s == np.trace(matriz):
        print("Propriedade da soma dos autovalores - Verdadeira")
    else:
        print("Propriedade da soma dos autovalores - Falsa")
        
def propriedade_produto(autovalores, matriz):
    s = 1
    for i in range(len(autovalores)):
        s*=autovalores[i]
    if s == round(np.linalg.det(matriz)):
        print("Propriedade do produto dos autovalores - Verdadeira")
    else:
        print("Propriedade do produto dos autovalores - Falsa")

def propriedade_determinante(autovalores, matriz):
    I = []
    M = []

    for i in range(len(matriz)):
        l = []
        for j in range(len(matriz)):
            l.append(matriz[i][j])
        M.append(l)
    
    for i in range(len(matriz)):
        l = []
        for j in range(len(matriz)):
            if i == j:
                l.append(1)
            else:
                l.append(0)
        I.append(l)
        
    for a in range(len(autovalores)):
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                matriz[i][j] = M[i][j]-autovalores[a]*I[i][j]
        if np.linalg.det(matriz) == 0:
            print("Propriedade do determinante para o "+str(a+1)+"º autovalor - Verdadeira")
        else:
            print("Propriedade do determinante para o "+str(a+1)+"º autovalor - Falsa")

def impressao_ordem_tres(matriz, vetor1, vetor2, vetor3, VO1, VO2, VO3, autovalores):
    print("\n")
    print("AUTOVALORES")
    for i in range(len(autovalores)):
        print("x"+str(i+1)+" = ",autovalores[i])

    print("\n")
    print("AUTOVETORES")
    print("\n")
    print("FORMA GERAL DOS AUTOVETORES")
    print("\n")
    print("V1 = ", VO1)
    print("V2 = ", VO2)
    print("V3 = ", VO3)
    print("\n")
    print("SOLUÇÃO ESPECÍFICA")
    print("\n")
    print("V1 = ", vetor1)
    print("V2 = ", vetor2)
    print("V3 = ", vetor3)
    print("\n") 

def impressao_ordem_dois(matriz, vetor1, vetor2, VO1, VO2, autovalores):
    print("\n")
    print("AUTOVALORES")
    for i in range(len(autovalores)):
        print("x"+str(i+1)+" = ",autovalores[i])

    print("\n")
    print("AUTOVETORES")
    print("\n")
    print("FORMA GERAL DOS AUTOVETORES")
    print("\n")
    print("V1 = ", VO1)
    print("V2 = ", VO2)
    print("\n")
    print("SOLUÇÃO ESPECIFICA PARA y = 1")
    print("\n")
    print("V1 = ", vetor1)
    print("V2 = ", vetor2)
    print("\n")
    
def cria_matriz(n):
    m = []
    for i in range(n):
        l = []
        for j in range(n):
            a = float(input("Digite o termo a"+str(i+1)+str(j+1)+" da matriz: "))
            l.append(a)
        m.append(l)
    return m

def main():
    n = int(input("Digite a ordem da matriz: "))
    matriz = cria_matriz(n)

    if n == 2:
        a = 1
        b = (-1)*(np.trace(matriz))
        c = np.linalg.det(matriz)

        delta = b**2-4*a*c

        if delta <= 10**(-10):
            x1 = ((-1)*(b))/(2*a)
            x2 = x1
        else:
            x1 = ((-1)*(b)+(delta)**(1/2))/(2*a)
            x2 = ((-1)*(b)-(delta)**(1/2))/(2*a)

        autoval = [x1, x2]

        if matriz[0][0]-x1 == 0:
            vetor1 = [(x1-matriz[1][1])/matriz[1][0],1]
            VO1 = [str((x1-matriz[1][1])/matriz[1][0])+"y","y"]
        else:
            vetor1 = vetor1 = [((-1)*(matriz[0][1]))/(matriz[0][0]-x1),1]
            VO1 = [str(((-1)*(matriz[0][1]))/(matriz[0][0]-x1))+"y","y"]

        if matriz[0][0]-x2 == 0:
            vetor2 = [(x2-matriz[1][1])/matriz[1][0],1]
            VO2 = [str((x2-matriz[1][1])/matriz[1][0])+"y","y"]
        else:
            vetor2 = [((-1)*(matriz[0][1]))/(matriz[0][0]-x2),1]
            VO2 = [str(((-1)*(matriz[0][1]))/(matriz[0][0]-x2))+"y","y"]
        
        impressao_ordem_dois(matriz, vetor1, vetor2, VO1, VO2, autoval)
        propriedade_diagonalizavel(matriz, vetor1, vetor2, [], autoval, n)
        propriedade_soma(autoval, matriz)
        propriedade_produto(autoval, matriz)
        propriedade_determinante(autoval, matriz)
        
    if n == 3:
        dupla = False
        
        a = 1
        b = (-1)*(np.trace(matriz))
        c = matriz[0][0]*matriz[1][1]+matriz[0][0]*matriz[2][2]+matriz[1][1]*matriz[2][2]-matriz[1][0]*matriz[0][1]-matriz[2][1]*matriz[1][2]-matriz[0][2]*matriz[2][0]
        d = (-1)*(np.linalg.det(matriz))

        Um = c/(3*a)
        Dois = b**2/(9*a**2)

        P = Um-Dois

        Tres = (b*c)/(6*a**2)
        Quatro = (b**3)/(27*a**3)
        Cinco = (d)/(2*a)

        Q = Tres-Quatro-Cinco

        Delta = P**3+Q**2
        Seis = b/(3*a)

        if Delta < 0:
            x1 = (2*(abs(P))**(1/2)*math.cos((1/3)*math.acos(Q/(abs(P)**3)**(1/2))))-Seis
            Sete = b/a
            Oito = (4*d)/(a*x1)
            D = (Sete+x1)**(2)+Oito
            x2 = ((-1)*(Sete+x1)+D**(1/2))/2
            x3 = ((-1)*(Sete+x1)-D**(1/2))/2

        elif Delta == 0:
            dupla = True
            if Q<0:
                x1 = (-1)*(2*(abs(Q))**(1/3))-Seis
            else:
                x1 = (2*(Q)**(1/3))-Seis
                
            Sete = b/a
            Oito = (4*d)/(a*x1)

            if Q!=0:
                x2 = ((-1)*(Sete+x1))/2
                x3 = x2
                
            else:
                x2 = (-1)*(Seis)
                x3 = x2
                
        else:
            x1 = (Q+(Delta)**(1/2))**(1/3)+(Q-(Delta)**(1/2))**(1/3)-Seis
            Sete = b/a
            Oito = (4*d)/(a*x1)

            x2 = ((-1)*(Sete+x1)+pow(D, 1/2))/2
            x3 = ((-1)*(Sete+x1)-pow(D, 1/2))/2

        autoval = [x1, x2, x3]

        if dupla == False:
            if matriz[0][1]*matriz[1][0]-((matriz[0][0]-x1)*(matriz[1][1]-x1)) != 0:
                vetor1 = [(matriz[0][2]*(matriz[1][1]-x1)-matriz[0][1]*matriz[1][2])/(matriz[0][1]*matriz[1][0]-((matriz[0][0]-x1)*(matriz[1][1]-x1))),
                          (matriz[1][2]*(matriz[0][0]-x1)-matriz[0][2]*matriz[1][0])/(matriz[0][1]*matriz[1][0]-((matriz[0][0]-x1)*(matriz[1][1]-x1))),1]

                VO1 = [str((matriz[0][2]*(matriz[1][1]-x1)-matriz[0][1]*matriz[1][2])/(matriz[0][1]*matriz[1][0]-((matriz[0][0]-x1)*(matriz[1][1]-x1))))+"z",
                       str((matriz[1][2]*(matriz[0][0]-x1)-matriz[0][2]*matriz[1][0])/(matriz[0][1]*matriz[1][0]-((matriz[0][0]-x1)*(matriz[1][1]-x1))))+"z","z"]
                
            elif matriz[0][1]*matriz[2][0]-((matriz[0][0]-x1)*matriz[2][1])!= 0:
                vetor1 = [(matriz[0][2]*matriz[2][1]+matriz[0][1]*(x1-matriz[2][2]))/(matriz[0][1]*matriz[2][0]-((matriz[0][0]-x1)*matriz[2][1])),
                          ((-1)*matriz[0][2]*matriz[2][0]-((matriz[0][0]-x1)*(x1-matriz[2][2])))/(matriz[0][1]*matriz[2][0]-((matriz[0][0]-x1)*matriz[2][1])),1]
                VO1 = [str((matriz[0][2]*matriz[2][1]+matriz[0][1]*(x1-matriz[2][2]))/(matriz[0][1]*matriz[2][0]-((matriz[0][0]-x1)*matriz[2][1])))+"z",
                       str(((-1)*matriz[0][2]*matriz[2][0]-((matriz[0][0]-x1)*(x1-matriz[2][2])))/(matriz[0][1]*matriz[2][0]-((matriz[0][0]-x1)*matriz[2][1])))+"z","z"]
            elif (matriz[1][1]-x1)*matriz[2][0]-matriz[1][0]*matriz[2][1] != 0:
                vetor1 = [(matriz[1][2]*matriz[2][1]+(matriz[1][1]-x1)*(x1-matriz[2][2]))/(((matriz[1][1]-x1)*matriz[2][0])-matriz[1][0]*matriz[2][1]),
                          ((-1)*(matriz[1][2]*matriz[2][0])-matriz[1][0]*(x1-matriz[2][2]))/(((matriz[1][1]-x1)*matriz[2][0])-matriz[1][0]*matriz[2][1]), 1]
                VO1 = [str((matriz[1][2]*matriz[2][1]+(matriz[1][1]-x1)*(x1-matriz[2][2]))/(((matriz[1][1]-x1)*matriz[2][0])-matriz[1][0]*matriz[2][1]))+"z",
                       str(((-1)*(matriz[1][2]*matriz[2][0])-matriz[1][0]*(x1-matriz[2][2]))/(((matriz[1][1]-x1)*matriz[2][0])-matriz[1][0]*matriz[2][1]))+"z", "z"]
            elif matriz[0][2]*matriz[1][0]-(matriz[0][0]-x1)*matriz[1][2] != 0:
                vetor1 = [(matriz[0][1]*matriz[1][2]+matriz[0][2]*(x1-matriz[1][1]))/(matriz[0][2]*matriz[1][0]-(matriz[0][0]-x1)*matriz[1][2]), 1,
                          ((-1)*matriz[0][1]*matriz[1][0]-(matriz[0][0]-x1)*(x1-matriz[1][1]))/(matriz[0][2]*matriz[1][0]-(matriz[0][0]-x1)*matriz[1][2])]
                VO1 = [str((matriz[0][1]*matriz[1][2]+matriz[0][2]*(x1-matriz[1][1]))/(matriz[0][2]*matriz[1][0]-(matriz[0][0]-x1)*matriz[1][2]))+"y", "y",
                       str(((-1)*matriz[0][1]*matriz[1][0]-(matriz[0][0]-x1)*(x1-matriz[1][1]))/(matriz[0][2]*matriz[1][0]-(matriz[0][0]-x1)*matriz[1][2]))+"y"]
            elif matriz[0][2]*matriz[2][0]-(matriz[0][0]-x1)*(matriz[2][2]-x1) != 0:
                vetor1 = [(matriz[0][1]*(matriz[2][2]-x1)-matriz[0][2]*matriz[2][1])/(matriz[0][2]*matriz[2][0]-(matriz[0][0]-x1)*(matriz[2][2]-x1)), 1,
                          ((-1)*matriz[0][1]*matriz[1][0]-(matriz[0][0]-x1)*(x1-matriz[1][1]))/(matriz[0][2]*matriz[1][0]-(matriz[0][0]-x1)*matriz[1][2])]
                VO1 = [str((matriz[0][1]*(matriz[2][2]-x1)-matriz[0][2]*matriz[2][1])/(matriz[0][2]*matriz[2][0]-(matriz[0][0]-x1)*(matriz[2][2]-x1)))+"y", "y",
                       str(((-1)*matriz[0][1]*matriz[1][0]-(matriz[0][0]-x1)*(x1-matriz[1][1]))/(matriz[0][2]*matriz[1][0]-(matriz[0][0]-x1)*matriz[1][2]))+"y"]
            elif matriz[1][2]*matriz[2][0]-matriz[1][0]*(matriz[2][2]-x1) != 0:
                vetor1 = [((matriz[1][1]-x1)*(matriz[2][2]-x1)-matriz[1][2]*matriz[2][1])/(matriz[1][2]*matriz[2][0]-matriz[1][0]*(matriz[2][2]-x1)), 1,
                          (matriz[2][0]*(x1-matriz[1][1])+matriz[1][0]*matriz[2][1])/(matriz[1][2]*matriz[2][0]-matriz[1][0]*(matriz[2][2]-x1))]
                VO1 = [str(((matriz[1][1]-x1)*(matriz[2][2]-x1)-matriz[1][2]*matriz[2][1])/(matriz[1][2]*matriz[2][0]-matriz[1][0]*(matriz[2][2]-x1)))+"y", "y",
                       str((matriz[2][0]*(x1-matriz[1][1])+matriz[1][0]*matriz[2][1])/(matriz[1][2]*matriz[2][0]-matriz[1][0]*(matriz[2][2]-x1)))+"y"]
            elif matriz[0][2]*(matriz[1][1]-x1)-matriz[0][2]*matriz[1][2] != 0:
                vetor1 = [1, (matriz[1][2]*(matriz[0][0]-x1)-matriz[0][2]*matriz[1][0])/(matriz[0][2]*(matriz[1][1]-x1)-matriz[0][2]*matriz[1][2]),
                         ((x1-matriz[0][0])*(matriz[1][1]-x1)+matriz[0][1]*matriz[1][0])/(matriz[0][2]*(matriz[1][1]-x1)-matriz[0][2]*matriz[1][2])]
                VO1 = ["x", str((matriz[1][2]*(matriz[0][0]-x1)-matriz[0][2]*matriz[1][0])/(matriz[0][2]*(matriz[1][1]-x1)-matriz[0][2]*matriz[1][2]))+"x",
                       str(((x1-matriz[0][0])*(matriz[1][1]-x1)+matriz[0][1]*matriz[1][0])/(matriz[0][2]*(matriz[1][1]-x1)-matriz[0][2]*matriz[1][2]))+"x"]
            elif matriz[0][2]*matriz[2][1]-matriz[0][1]*(matriz[2][2]-x1) != 0:
                vetor1 = [1, ((matriz[0][0]-x1)*(matriz[2][2]-x1)-matriz[0][2]*matriz[2][0])/(matriz[0][2]*matriz[2][1]-matriz[0][1]*(matriz[2][2]-x1)),
                         (matriz[2][1]*(x1 - matriz[0][0])+matriz[0][1]*matriz[2][0])/(matriz[0][2]*matriz[2][1]-matriz[0][1]*(matriz[2][2]-x1))]
                VO1 = ["x", str(((matriz[0][0]-x1)*(matriz[2][2]-x1)-matriz[0][2]*matriz[2][0])/(matriz[0][2]*matriz[2][1]-matriz[0][1]*(matriz[2][2]-x1)))+"x",
                       str((matriz[2][1]*(x1 - matriz[0][0])+matriz[0][1]*matriz[2][0])/(matriz[0][2]*matriz[2][1]-matriz[0][1]*(matriz[2][2]-x1)))+"x"]
            elif matriz[1][2]*matriz[2][1]-(matriz[1][1]-x1)*(matriz[2][2]-x1) != 0:
                vetor1 = [1, (matriz[1][0]*(matriz[2][2]-x1)-matriz[1][2]*matriz[2][0])/(matriz[1][2]*matriz[2][1]-(matriz[1][1]-x1)*(matriz[2][2]-x1)),
                         ((-1)*matriz[1][0]*matriz[2][1]+matriz[2][0]*(matriz[1][1]-x1))/(matriz[1][2]*matriz[2][1]-(matriz[1][1]-x1)*(matriz[2][2]-x1))]
                VO1 = ["x", str((matriz[1][0]*(matriz[2][2]-x1)-matriz[1][2]*matriz[2][0])/(matriz[1][2]*matriz[2][1]-(matriz[1][1]-x1)*(matriz[2][2]-x1)))+"x",
                       str(((-1)*matriz[1][0]*matriz[2][1]+matriz[2][0]*(matriz[1][1]-x1))/(matriz[1][2]*matriz[2][1]-(matriz[1][1]-x1)*(matriz[2][2]-x1)))+"x"]
            else:
                vetor1 = []
                VO1 = []
                

            if matriz[0][1]*matriz[1][0]-((matriz[0][0]-x2)*(matriz[1][1]-x2)) != 0:
                vetor2 = [(matriz[0][2]*(matriz[1][1]-x2)-matriz[0][1]*matriz[1][2])/(matriz[0][1]*matriz[1][0]-((matriz[0][0]-x2)*(matriz[1][1]-x2))),
                          (matriz[1][2]*(matriz[0][0]-x2)-matriz[0][2]*matriz[1][0])/(matriz[0][1]*matriz[1][0]-((matriz[0][0]-x2)*(matriz[1][1]-x2))),1]

                VO2 = [str((matriz[0][2]*(matriz[1][1]-x2)-matriz[0][1]*matriz[1][2])/(matriz[0][1]*matriz[1][0]-((matriz[0][0]-x2)*(matriz[1][1]-x2))))+"z",
                       str((matriz[1][2]*(matriz[0][0]-x2)-matriz[0][2]*matriz[1][0])/(matriz[0][1]*matriz[1][0]-((matriz[0][0]-x2)*(matriz[1][1]-x2))))+"z","z"]
                
            elif matriz[0][1]*matriz[2][0]-((matriz[0][0]-x2)*matriz[2][1])!= 0:
                vetor2 = [(matriz[0][2]*matriz[2][1]+matriz[0][1]*(x2-matriz[2][2]))/(matriz[0][1]*matriz[2][0]-((matriz[0][0]-x2)*matriz[2][1])),
                          ((-1)*matriz[0][2]*matriz[2][0]-((matriz[0][0]-x2)*(x2-matriz[2][2])))/(matriz[0][1]*matriz[2][0]-((matriz[0][0]-x2)*matriz[2][1])),1]
                VO2 = [str((matriz[0][2]*matriz[2][1]+matriz[0][1]*(x2-matriz[2][2]))/(matriz[0][1]*matriz[2][0]-((matriz[0][0]-x2)*matriz[2][1])))+"z",
                       str(((-1)*matriz[0][2]*matriz[2][0]-((matriz[0][0]-x2)*(x2-matriz[2][2])))/(matriz[0][1]*matriz[2][0]-((matriz[0][0]-x2)*matriz[2][1])))+"z","z"]
            elif ((matriz[1][1]-x2)*matriz[2][0])-matriz[1][0]*matriz[2][1] != 0:
                vetor2 = [(matriz[1][2]*matriz[2][1]+(matriz[1][1]-x2)*(x2-matriz[2][2]))/(((matriz[1][1]-x2)*matriz[2][0])-matriz[1][0]*matriz[2][1]),
                          ((-1)*(matriz[1][2]*matriz[2][0])-matriz[1][0]*(x2-matriz[2][2]))/(((matriz[1][1]-x2)*matriz[2][0])-matriz[1][0]*matriz[2][1]), 1]
                VO2 = [str((matriz[1][2]*matriz[2][1]+(matriz[1][1]-x2)*(x2-matriz[2][2]))/(((matriz[1][1]-x2)*matriz[2][0])-matriz[1][0]*matriz[2][1]))+"z",
                       str(((-1)*(matriz[1][2]*matriz[2][0])-matriz[1][0]*(x2-matriz[2][2]))/(((matriz[1][1]-x2)*matriz[2][0])-matriz[1][0]*matriz[2][1]))+"z", "z"]
            elif matriz[0][2]*matriz[1][0]-(matriz[0][0]-x2)*matriz[1][2] != 0:
                vetor2 = [(matriz[0][1]*matriz[1][2]+matriz[0][2]*(x2-matriz[1][1]))/(matriz[0][2]*matriz[1][0]-(matriz[0][0]-x2)*matriz[1][2]), 1,
                          ((-1)*matriz[0][1]*matriz[1][0]-(matriz[0][0]-x2)*(x2-matriz[1][1]))/(matriz[0][2]*matriz[1][0]-(matriz[0][0]-x2)*matriz[1][2])]
                VO2 = [str((matriz[0][1]*matriz[1][2]+matriz[0][2]*(x2-matriz[1][1]))/(matriz[0][2]*matriz[1][0]-(matriz[0][0]-x2)*matriz[1][2]))+"y", "y",
                       str(((-1)*matriz[0][1]*matriz[1][0]-(matriz[0][0]-x2)*(x2-matriz[1][1]))/(matriz[0][2]*matriz[1][0]-(matriz[0][0]-x2)*matriz[1][2]))+"y"]
            elif matriz[0][2]*matriz[2][0]-(matriz[0][0]-x2)*(matriz[2][2]-x2) != 0:
                vetor2 = [(matriz[0][1]*(matriz[2][2]-x2)-matriz[0][2]*matriz[2][1])/(matriz[0][2]*matriz[2][0]-(matriz[0][0]-x2)*(matriz[2][2]-x2)), 1,
                          ((-1)*matriz[0][1]*matriz[1][0]-(matriz[0][0]-x2)*(x2-matriz[1][1]))/(matriz[0][2]*matriz[1][0]-(matriz[0][0]-x2)*matriz[1][2])]
                VO2 = [str((matriz[0][1]*(matriz[2][2]-x2)-matriz[0][2]*matriz[2][1])/(matriz[0][2]*matriz[2][0]-(matriz[0][0]-x2)*(matriz[2][2]-x2)))+"y", "y",
                       str(((-1)*matriz[0][1]*matriz[1][0]-(matriz[0][0]-x2)*(x2-matriz[1][1]))/(matriz[0][2]*matriz[1][0]-(matriz[0][0]-x2)*matriz[1][2]))+"y"]
            elif matriz[1][2]*matriz[2][0]-matriz[1][0]*(matriz[2][2]-x2) != 0:
                vetor2 = [((matriz[1][1]-x2)*(matriz[2][2]-x2)-matriz[1][2]*matriz[2][1])/(matriz[1][2]*matriz[2][0]-matriz[1][0]*(matriz[2][2]-x2)), 1,
                          (matriz[2][0]*(x2-matriz[1][1])+matriz[1][0]*matriz[2][1])/(matriz[1][2]*matriz[2][0]-matriz[1][0]*(matriz[2][2]-x2))]
                VO2 = [str(((matriz[1][1]-x2)*(matriz[2][2]-x2)-matriz[1][2]*matriz[2][1])/(matriz[1][2]*matriz[2][0]-matriz[1][0]*(matriz[2][2]-x2)))+"y", "y",
                       str((matriz[2][0]*(x2-matriz[1][1])+matriz[1][0]*matriz[2][1])/(matriz[1][2]*matriz[2][0]-matriz[1][0]*(matriz[2][2]-x2)))+"y"]
            elif matriz[0][2]*(matriz[1][1]-x2)-matriz[0][2]*matriz[1][2] != 0:
                vetor2 = [1, (matriz[1][2]*(matriz[0][0]-x2)-matriz[0][2]*matriz[1][0])/(matriz[0][2]*(matriz[1][1]-x2)-matriz[0][2]*matriz[1][2]),
                         ((x2-matriz[0][0])*(matriz[1][1]-x2)+matriz[0][1]*matriz[1][0])/(matriz[0][2]*(matriz[1][1]-x2)-matriz[0][2]*matriz[1][2])]
                VO2 = ["x", str((matriz[1][2]*(matriz[0][0]-x2)-matriz[0][2]*matriz[1][0])/(matriz[0][2]*(matriz[1][1]-x2)-matriz[0][2]*matriz[1][2]))+"x",
                       str(((x2-matriz[0][0])*(matriz[1][1]-x2)+matriz[0][1]*matriz[1][0])/(matriz[0][2]*(matriz[1][1]-x2)-matriz[0][2]*matriz[1][2]))+"x"]
            elif matriz[0][2]*matriz[2][1]-matriz[0][1]*(matriz[2][2]-x2) != 0:
                vetor2 = [1, ((matriz[0][0]-x2)*(matriz[2][2]-x2)-matriz[0][2]*matriz[2][0])/(matriz[0][2]*matriz[2][1]-matriz[0][1]*(matriz[2][2]-x2)),
                         (matriz[2][1]*(x2 - matriz[0][0])+matriz[0][1]*matriz[2][0])/(matriz[0][2]*matriz[2][1]-matriz[0][1]*(matriz[2][2]-x2))]
                VO2 = ["x", str(((matriz[0][0]-x2)*(matriz[2][2]-x2)-matriz[0][2]*matriz[2][0])/(matriz[0][2]*matriz[2][1]-matriz[0][1]*(matriz[2][2]-x2)))+"x",
                       str((matriz[2][1]*(x2 - matriz[0][0])+matriz[0][1]*matriz[2][0])/(matriz[0][2]*matriz[2][1]-matriz[0][1]*(matriz[2][2]-x2)))+"x"]
            elif matriz[1][2]*matriz[2][1]-(matriz[1][1]-x2)*(matriz[2][2]-x2) != 0:
                vetor2 = [1, (matriz[1][0]*(matriz[2][2]-x2)-matriz[1][2]*matriz[2][0])/(matriz[1][2]*matriz[2][1]-(matriz[1][1]-x2)*(matriz[2][2]-x2)),
                         ((-1)*matriz[1][0]*matriz[2][1]+matriz[2][0]*(matriz[1][1]-x2))/(matriz[1][2]*matriz[2][1]-(matriz[1][1]-x2)*(matriz[2][2]-x2))]
                VO2 = ["x", str((matriz[1][0]*(matriz[2][2]-x2)-matriz[1][2]*matriz[2][0])/(matriz[1][2]*matriz[2][1]-(matriz[1][1]-x2)*(matriz[2][2]-x2)))+"x",
                       str(((-1)*matriz[1][0]*matriz[2][1]+matriz[2][0]*(matriz[1][1]-x2))/(matriz[1][2]*matriz[2][1]-(matriz[1][1]-x2)*(matriz[2][2]-x2)))+"x"]
            else:
                vetor2 = []
                VO2 = []


            if matriz[0][1]*matriz[1][0]-((matriz[0][0]-x3)*(matriz[1][1]-x3)) != 0:
                vetor3 = [(matriz[0][2]*(matriz[1][1]-x3)-matriz[0][1]*matriz[1][2])/(matriz[0][1]*matriz[1][0]-((matriz[0][0]-x3)*(matriz[1][1]-x3))),
                          (matriz[1][2]*(matriz[0][0]-x3)-matriz[0][2]*matriz[1][0])/(matriz[0][1]*matriz[1][0]-((matriz[0][0]-x3)*(matriz[1][1]-x3))),1]

                VO3 = [str((matriz[0][2]*(matriz[1][1]-x3)-matriz[0][1]*matriz[1][2])/(matriz[0][1]*matriz[1][0]-((matriz[0][0]-x3)*(matriz[1][1]-x3))))+"z",
                       str((matriz[1][2]*(matriz[0][0]-x3)-matriz[0][2]*matriz[1][0])/(matriz[0][1]*matriz[1][0]-((matriz[0][0]-x3)*(matriz[1][1]-x3))))+"z","z"]
                
            elif matriz[0][1]*matriz[2][0]-((matriz[0][0]-x3)*matriz[2][1])!= 0:
                vetor3 = [(matriz[0][2]*matriz[2][1]+matriz[0][1]*(x3-matriz[2][2]))/(matriz[0][1]*matriz[2][0]-((matriz[0][0]-x3)*matriz[2][1])),
                          ((-1)*matriz[0][2]*matriz[2][0]-((matriz[0][0]-x3)*(x3-matriz[2][2])))/(matriz[0][1]*matriz[2][0]-((matriz[0][0]-x3)*matriz[2][1])),1]
                VO3 = [str((matriz[0][2]*matriz[2][1]+matriz[0][1]*(x3-matriz[2][2]))/(matriz[0][1]*matriz[2][0]-((matriz[0][0]-x3)*matriz[2][1])))+"z",
                       str(((-1)*matriz[0][2]*matriz[2][0]-((matriz[0][0]-x3)*(x3-matriz[2][2])))/(matriz[0][1]*matriz[2][0]-((matriz[0][0]-x3)*matriz[2][1])))+"z","z"]
            elif ((matriz[1][1]-x3)*matriz[2][0])-matriz[1][0]*matriz[2][1] != 0:
                vetor3 = [(matriz[1][2]*matriz[2][1]+(matriz[1][1]-x3)*(x3-matriz[2][2]))/(((matriz[1][1]-x3)*matriz[2][0])-matriz[1][0]*matriz[2][1]),
                          ((-1)*(matriz[1][2]*matriz[2][0])-matriz[1][0]*(x3-matriz[2][2]))/(((matriz[1][1]-x3)*matriz[2][0])-matriz[1][0]*matriz[2][1]), 1]
                VO3 = [str((matriz[1][2]*matriz[2][1]+(matriz[1][1]-x3)*(x3-matriz[2][2]))/(((matriz[1][1]-x3)*matriz[2][0])-matriz[1][0]*matriz[2][1]))+"z",
                       str(((-1)*(matriz[1][2]*matriz[2][0])-matriz[1][0]*(x3-matriz[2][2]))/(((matriz[1][1]-x3)*matriz[2][0])-matriz[1][0]*matriz[2][1]))+"z", "z"]
            elif matriz[0][2]*matriz[1][0]-(matriz[0][0]-x3)*matriz[1][2] != 0:
                vetor3 = [(matriz[0][1]*matriz[1][2]+matriz[0][2]*(x3-matriz[1][1]))/(matriz[0][2]*matriz[1][0]-(matriz[0][0]-x3)*matriz[1][2]), 1,
                          ((-1)*matriz[0][1]*matriz[1][0]-(matriz[0][0]-x3)*(x3-matriz[1][1]))/(matriz[0][2]*matriz[1][0]-(matriz[0][0]-x3)*matriz[1][2])]
                VO3 = [str((matriz[0][1]*matriz[1][2]+matriz[0][2]*(x3-matriz[1][1]))/(matriz[0][2]*matriz[1][0]-(matriz[0][0]-x3)*matriz[1][2]))+"y", "y",
                       str(((-1)*matriz[0][1]*matriz[1][0]-(matriz[0][0]-x3)*(x3-matriz[1][1]))/(matriz[0][2]*matriz[1][0]-(matriz[0][0]-x3)*matriz[1][2]))+"y"]
            elif matriz[0][2]*matriz[2][0]-(matriz[0][0]-x3)*(matriz[2][2]-x3) != 0:
                vetor3 = [(matriz[0][1]*(matriz[2][2]-x3)-matriz[0][2]*matriz[2][1])/(matriz[0][2]*matriz[2][0]-(matriz[0][0]-x3)*(matriz[2][2]-x3)), 1,
                          ((-1)*matriz[0][1]*matriz[1][0]-(matriz[0][0]-x3)*(x3-matriz[1][1]))/(matriz[0][2]*matriz[1][0]-(matriz[0][0]-x3)*matriz[1][2])]
                VO3 = [str((matriz[0][1]*(matriz[2][2]-x3)-matriz[0][2]*matriz[2][1])/(matriz[0][2]*matriz[2][0]-(matriz[0][0]-x3)*(matriz[2][2]-x3)))+"y", "y",
                       str(((-1)*matriz[0][1]*matriz[1][0]-(matriz[0][0]-x3)*(x3-matriz[1][1]))/(matriz[0][2]*matriz[1][0]-(matriz[0][0]-x3)*matriz[1][2]))+"y"]
            elif matriz[1][2]*matriz[2][0]-matriz[1][0]*(matriz[2][2]-x3) != 0:
                vetor3 = [((matriz[1][1]-x3)*(matriz[2][2]-x3)-matriz[1][2]*matriz[2][1])/(matriz[1][2]*matriz[2][0]-matriz[1][0]*(matriz[2][2]-x3)), 1,
                          (matriz[2][0]*(x3-matriz[1][1])+matriz[1][0]*matriz[2][1])/(matriz[1][2]*matriz[2][0]-matriz[1][0]*(matriz[2][2]-x3))]
                VO3 = [str(((matriz[1][1]-x3)*(matriz[2][2]-x3)-matriz[1][2]*matriz[2][1])/(matriz[1][2]*matriz[2][0]-matriz[1][0]*(matriz[2][2]-x3)))+"y", "y",
                       str((matriz[2][0]*(x3-matriz[1][1])+matriz[1][0]*matriz[2][1])/(matriz[1][2]*matriz[2][0]-matriz[1][0]*(matriz[2][2]-x3)))+"y"]
            elif matriz[0][2]*(matriz[1][1]-x3)-matriz[0][2]*matriz[1][2] != 0:
                vetor3 = [1, (matriz[1][2]*(matriz[0][0]-x3)-matriz[0][2]*matriz[1][0])/(matriz[0][2]*(matriz[1][1]-x3)-matriz[0][2]*matriz[1][2]),
                         ((x3-matriz[0][0])*(matriz[1][1]-x3)+matriz[0][1]*matriz[1][0])/(matriz[0][2]*(matriz[1][1]-x3)-matriz[0][2]*matriz[1][2])]
                VO3 = ["x", str((matriz[1][2]*(matriz[0][0]-x3)-matriz[0][2]*matriz[1][0])/(matriz[0][2]*(matriz[1][1]-x3)-matriz[0][2]*matriz[1][2]))+"x",
                       str(((x3-matriz[0][0])*(matriz[1][1]-x3)+matriz[0][1]*matriz[1][0])/(matriz[0][2]*(matriz[1][1]-x3)-matriz[0][2]*matriz[1][2]))+"x"]
            elif matriz[0][2]*matriz[2][1]-matriz[0][1]*(matriz[2][2]-x3) != 0:
                vetor3 = [1, ((matriz[0][0]-x3)*(matriz[2][2]-x3)-matriz[0][2]*matriz[2][0])/(matriz[0][2]*matriz[2][1]-matriz[0][1]*(matriz[2][2]-x3)),
                         (matriz[2][1]*(x3 - matriz[0][0])+matriz[0][1]*matriz[2][0])/(matriz[0][2]*matriz[2][1]-matriz[0][1]*(matriz[2][2]-x3))]
                VO3 = ["x", str(((matriz[0][0]-x3)*(matriz[2][2]-x3)-matriz[0][2]*matriz[2][0])/(matriz[0][2]*matriz[2][1]-matriz[0][1]*(matriz[2][2]-x3)))+"x",
                       str((matriz[2][1]*(x3 - matriz[0][0])+matriz[0][1]*matriz[2][0])/(matriz[0][2]*matriz[2][1]-matriz[0][1]*(matriz[2][2]-x3)))+"x"]
            elif matriz[1][2]*matriz[2][1]-(matriz[1][1]-x3)*(matriz[2][2]-x3) != 0:
                vetor3 = [1, (matriz[1][0]*(matriz[2][2]-x3)-matriz[1][2]*matriz[2][0])/(matriz[1][2]*matriz[2][1]-(matriz[1][1]-x3)*(matriz[2][2]-x3)),
                         ((-1)*matriz[1][0]*matriz[2][1]+matriz[2][0]*(matriz[1][1]-x3))/(matriz[1][2]*matriz[2][1]-(matriz[1][1]-x3)*(matriz[2][2]-x3))]
                VO3 = ["x", str((matriz[1][0]*(matriz[2][2]-x3)-matriz[1][2]*matriz[2][0])/(matriz[1][2]*matriz[2][1]-(matriz[1][1]-x3)*(matriz[2][2]-x3)))+"x",
                       str(((-1)*matriz[1][0]*matriz[2][1]+matriz[2][0]*(matriz[1][1]-x3))/(matriz[1][2]*matriz[2][1]-(matriz[1][1]-x3)*(matriz[2][2]-x3)))+"x"]
            else:
                vetor3 = []
                VO3 = []
                
        else:
            if matriz[0][1]*matriz[1][0]-((matriz[0][0]-x1)*(matriz[1][1]-x1)) != 0:
                vetor1 = [(matriz[0][2]*(matriz[1][1]-x1)-matriz[0][1]*matriz[1][2])/(matriz[0][1]*matriz[1][0]-((matriz[0][0]-x1)*(matriz[1][1]-x1))),
                          (matriz[1][2]*(matriz[0][0]-x1)-matriz[0][2]*matriz[1][0])/(matriz[0][1]*matriz[1][0]-((matriz[0][0]-x1)*(matriz[1][1]-x1))),1]

                VO1 = [str((matriz[0][2]*(matriz[1][1]-x1)-matriz[0][1]*matriz[1][2])/(matriz[0][1]*matriz[1][0]-((matriz[0][0]-x1)*(matriz[1][1]-x1))))+"z",
                       str((matriz[1][2]*(matriz[0][0]-x1)-matriz[0][2]*matriz[1][0])/(matriz[0][1]*matriz[1][0]-((matriz[0][0]-x1)*(matriz[1][1]-x1))))+"z","z"]
                
            elif matriz[0][1]*matriz[2][0]-((matriz[0][0]-x1)*matriz[2][1])!= 0:
                vetor1 = [(matriz[0][2]*matriz[2][1]+matriz[0][1]*(x1-matriz[2][2]))/(matriz[0][1]*matriz[2][0]-((matriz[0][0]-x1)*matriz[2][1])),
                          ((-1)*matriz[0][2]*matriz[2][0]-((matriz[0][0]-x1)*(x1-matriz[2][2])))/(matriz[0][1]*matriz[2][0]-((matriz[0][0]-x1)*matriz[2][1])),1]
                VO1 = [str((matriz[0][2]*matriz[2][1]+matriz[0][1]*(x1-matriz[2][2]))/(matriz[0][1]*matriz[2][0]-((matriz[0][0]-x1)*matriz[2][1])))+"z",
                       str(((-1)*matriz[0][2]*matriz[2][0]-((matriz[0][0]-x1)*(x1-matriz[2][2])))/(matriz[0][1]*matriz[2][0]-((matriz[0][0]-x1)*matriz[2][1])))+"z","z"]
            elif ((matriz[1][1]-x1)*matriz[2][0])-matriz[1][0]*matriz[2][1] != 0:
                vetor1 = [(matriz[1][2]*matriz[2][1]+(matriz[1][1]-x1)*(x1-matriz[2][2]))/(((matriz[1][1]-x1)*matriz[2][0])-matriz[1][0]*matriz[2][1]),
                          ((-1)*(matriz[1][2]*matriz[2][0])-matriz[1][0]*(x1-matriz[2][2]))/(((matriz[1][1]-x1)*matriz[2][0])-matriz[1][0]*matriz[2][1]), 1]
                VO1 = [str((matriz[1][2]*matriz[2][1]+(matriz[1][1]-x1)*(x1-matriz[2][2]))/(((matriz[1][1]-x1)*matriz[2][0])-matriz[1][0]*matriz[2][1]))+"z",
                       str(((-1)*(matriz[1][2]*matriz[2][0])-matriz[1][0]*(x1-matriz[2][2]))/(((matriz[1][1]-x1)*matriz[2][0])-matriz[1][0]*matriz[2][1]))+"z", "z"]
            else:
                vetor1 = []
                VO1 = []

            if matriz[0][0]-x2 != 0:
                vetor2 = [((-1)*(matriz[0][1])-matriz[0][2])/(matriz[0][0]-x2), 1, 1]
                y = str((-1)*(matriz[0][1]))
                z = str((-1)*(matriz[0][2]))        
                VO2 = [y+"y+("+z+")"+"z", "y", "z"]
            elif matriz[1][0] != 0:
                vetor2 = [((x2-matriz[1][1])-matriz[1][2])/matriz[1][0]]
                y = str(x2-matriz[1][1])
                z = str((-1)*(matriz[1][2]))
                VO2 = [y+"y+("+z+")"+"z", "y", "z"]
            elif matriz[2][0] != 0:
                vetor2 = [((-1)*(matriz[2][1])+(x2-matriz[2][2]))/(matriz[2][0]), 1, 1]
                y = str((-1)*(matriz[2][1]))
                z = str(x2-matriz[2][2])
                VO2 = [y+"y+("+z+")"+"z", "y", "z"]
            elif matriz[0][1] != 0:
                vetor2 = [1, (x2-matriz[0][0]-matriz[0][2])/matriz[0][1], 1]
                x = str(x2-matriz[0][0])
                z = str((-1)*matriz[0][2])
                VO2 = [y+"y+("+z+")"+"z", "y", "z"]
            elif matriz[1][1]-x2 != 0:
                vetor2 = [1, ((-1)*(matriz[1][0])-matriz[1][2])/(matriz[1][1]-x2), 1]
                x = str((-1)*(matriz[1][0]))
                z = str((-1)*matriz[1][2])
                VO2 = [y+"y+("+z+")"+"z", "y", "z"]
            elif matriz[2][1] != 0:
                vetor2 = [1, ((-1)*(matriz[2][0])+(x2-matriz[2][2]))/(matriz[2][1]), 1]
                x = str((-1)*(matriz[2][0]))
                z = str(x2-matriz[2][2])
                VO2 = [y+"y+("+z+")"+"z", "y", "z"]
            elif matriz[0][2] != 0:
                vetor2 = [1, 1, (x2-matriz[0][0]-matriz[0][1])/(matriz[0][2])]
                x = str(x2-matriz[0][0])
                y = str((-1)*matriz[0][1])
                VO2 = [y+"y+("+z+")"+"z", "y", "z"]
            elif matriz[1][2] != 0:
                vetor2 = [1, 1, ((-1)*matriz[1][0]+(x2-matriz[1][1]))/(matriz[1][2])]
                x = str((-1)*matriz[1][0])
                y = str(x2-matriz[1][1])
                VO2 = [y+"y+("+z+")"+"z", "y", "z"]
            elif matriz[2][2]-x2 != 0:
                vetor2 = [1, 1, ((-1)*matriz[2][0]-matriz[2][1])/(matriz[2][2]-x2)]
                x = str((-1)*matriz[2][0])
                y = str((-1)*matriz[2][1])
                VO2 = [y+"y+("+z+")"+"z", "y", "z"]
            else:
                vetor2 = []
                VO2 = []

            if matriz[0][0]-x3 != 0:
                vetor3 = [((-1)*(matriz[0][1])-matriz[0][2])/(matriz[0][0]-x3), 1, 1]
                y = str((-1)*(matriz[0][1]))
                z = str((-1)*(matriz[0][2]))        
                VO3 = [y+"y+("+z+")"+"z", "y", "z"]
            elif matriz[1][0] != 0:
                vetor3 = [((x3-matriz[1][1])-matriz[1][2])/matriz[1][0]]
                y = str(x3-matriz[1][1])
                z = str((-1)*(matriz[1][2]))
                VO3 = [y+"y+("+z+")"+"z", "y", "z"]
            elif matriz[2][0] != 0:
                vetor3 = [((-1)*(matriz[2][1])+(x3-matriz[2][2]))/(matriz[2][0]), 1, 1]
                y = str((-1)*(matriz[2][1]))
                z = str(x3-matriz[2][2])
                VO3 = [y+"y+("+z+")"+"z", "y", "z"]
            elif matriz[0][1] != 0:
                vetor3 = [1, (x3-matriz[0][0]-matriz[0][2])/matriz[0][1], 1]
                x = str(x3-matriz[0][0])
                z = str((-1)*matriz[0][2])
                VO3 = [y+"y+("+z+")"+"z", "y", "z"]
            elif matriz[1][1]-x3 != 0:
                vetor3 = [1, ((-1)*(matriz[1][0])-matriz[1][2])/(matriz[1][1]-x3), 1]
                x = str((-1)*(matriz[1][0]))
                z = str((-1)*matriz[1][2])
                VO3 = [y+"y+("+z+")"+"z", "y", "z"]
            elif matriz[2][1] != 0:
                vetor3 = [1, ((-1)*(matriz[2][0])+(x3-matriz[2][2]))/(matriz[2][1]), 1]
                x = str((-1)*(matriz[2][0]))
                z = str(x3-matriz[2][2])
                VO3 = [y+"y+("+z+")"+"z", "y", "z"]
            elif matriz[0][2] != 0:
                vetor3 = [1, 1, (x3-matriz[0][0]-matriz[0][1])/(matriz[0][2])]
                x = str(x3-matriz[0][0])
                y = str((-1)*matriz[0][1])
                VO3 = [y+"y+("+z+")"+"z", "y", "z"]
            elif matriz[1][2] != 0:
                vetor3 = [1, 1, ((-1)*matriz[1][0]+(x3-matriz[1][1]))/(matriz[1][2])]
                x = str((-1)*matriz[1][0])
                y = str(x3-matriz[1][1])
                VO3 = [y+"y+("+z+")"+"z", "y", "z"]
            elif matriz[2][2]-x3 != 0:
                vetor3 = [1, 1, ((-1)*matriz[2][0]-matriz[2][1])/(matriz[2][2]-x3)]
                x = str((-1)*matriz[2][0])
                y = str((-1)*matriz[2][1])
                VO3 = [y+"y+("+z+")"+"z", "y", "z"]
            else:
                vetor3 = []
                VO3 = []
                
        impressao_ordem_tres(matriz, vetor1, vetor2, vetor3, VO1, VO2, VO3, autoval)
        propriedade_diagonalizavel(matriz, vetor1, vetor2, vetor3, autoval, n)
        propriedade_soma(autoval, matriz)
        propriedade_produto(autoval, matriz)
        propriedade_determinante(autoval, matriz)
main()
