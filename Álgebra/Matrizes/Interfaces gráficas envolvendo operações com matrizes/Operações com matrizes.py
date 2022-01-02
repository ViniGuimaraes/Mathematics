from tkinter import *
from functools import partial
import numpy as np

class Quadradas:
    def __init__(self, janela_operacoes, ordem, operation):
        def retorno():
            janela_operacoes.destroy()
            jp = Tk()
            JP = GUI_matrizes(jp)
            jp.mainloop()
            
        def nao_e_possivel():
            janela_operacoes.destroy()
            jp = Tk()
            JP = GUI_matrizes(jp)
            jp.mainloop()
            
        def preencher(botoesE, confirmar):
            confirmar.destroy()
            for i in range(0, ordem):
                l = []
                for j in range(0, ordem):
                    l.append(0)
                matriz.append(l)

            position = 0
            f1 = 0
            f2 = 0

            for i in range(0, ordem):
                for j in range(0, ordem):
                    if "/" in botoesE[i][j].get():
                        for a in range(0, len(botoesE[i][j].get())):
                            if botoesE[i][j].get()[a] == "/":
                                position = a
                                break
                        f1 = float(botoesE[i][j].get()[0:position])
                        f2 = float(botoesE[i][j].get()[position+1:len(botoesE[i][j].get())])
                        matriz[i][j] = f1/f2
                    else:          
                        matriz[i][j] = int(botoesE[i][j].get())

            if operation == "determinante":
                resultado = np.linalg.det(matriz)
                det = Label(janela_operacoes, text = "det(A) = "+str(round(resultado, 2)))
                det.configure(font = ("Kravitz Extra Thermal",16, "bold"))
                det.place(relx = 0.5, rely = 0.75, anchor = CENTER)

                botao_final = Button(janela_operacoes, text = "OK", width = 15, height = 2, command = retorno)
                botao_final.place(relx = 0.5, rely = 0.85, anchor = CENTER)

            if operation == "inversa":
                if abs(np.linalg.det(matriz))<10**(-5):
                    aviso = Label(janela_operacoes, text = "A matriz não admite inversa\npois seu determinante é igual a zero")
                    aviso.configure(font=("Kravitz Extra Thermal", 16, "bold"))
                    aviso.place(relx = 0.7, rely = 0.5, anchor = CENTER)
                    botao_final = Button(janela_operacoes, text = "OK", width = 15, height = 2, command = nao_e_possivel)
                    botao_final.place(relx = 0.5, rely = 0.85, anchor = CENTER)
                else:
                    inverse = np.linalg.inv(matriz)
                    Lbs = []
                    for i in range(0, ordem):
                        l = []
                        for j in range(0, ordem):
                            l.append(0)
                        Lbs.append(l)

                    for i in range(0, ordem):
                        for j in range(0, ordem):
                            Lbs[i][j] = Label(janela_operacoes, text = str(round(inverse[i][j], 2)))
                            Lbs[i][j].configure(font=("Kravitz Extra Thermal", 16, "bold"))

                    linhas = ordem
                    colunas = ordem

                    colun = [0.7, 0.67, 0.64, 0.61, 0.58, 0.55]
                    lin = [0.45, 0.4, 0.35, 0.3, 0.25, 0.22]
                
                    sl = lin[linhas-1]
                    sc = colun[colunas-1]

                    for i in range(0, linhas):
                        sc = colun[colunas-1]
                        if i != 0:
                            sl+=0.085
                        for j in range(0, colunas):
                            Lbs[i][j].place(relx = sc, rely = sl, anchor = CENTER)
                            sc+=0.06

                    botao_final = Button(janela_operacoes, text = "OK", width = 15, height = 2, command = retorno)
                    botao_final.place(relx = 0.5, rely = 0.85, anchor = CENTER)
                
            
        self.janela_operacoes = janela_operacoes
        self.janela_operacoes.state('normal')
        self.janela_operacoes.title("Operações com matrizes")

        tit = Label(janela_operacoes, text = "DIGITE OS ELEMENTOS")
        tit.configure(font = ("Kravitz Extra Thermal",24, "bold"))
        tit.place(relx = 0.5, rely = 0.07, anchor = CENTER)

        botoesE = []
        matriz = []

        for i in range(0, ordem):
            linha = []
            for j in range(0, ordem):
                linha.append(0)
            botoesE.append(linha)

        for i in range(0, ordem):
            for j in range(0, ordem):
                botoesE[i][j] = Entry(janela_operacoes, width = 2)
                botoesE[i][j].configure(font = ("Kravitz Extra Thermal", 18, "bold"))
                botoesE[i][j].insert(END, "")
                
        linhas = ordem
        colunas = ordem

        if operation == "determinante":
            colun = [0.5, 0.47, 0.44, 0.41, 0.38, 0.35]
            lin = [0.45, 0.4, 0.35, 0.3, 0.25, 0.22]
            
            sl = lin[linhas-1]
            sc = colun[colunas-1]


            for i in range(0, linhas):
                sc = colun[colunas-1]
                if i!=0:
                    sl+=0.085
                for j in range(0, colunas):
                    botoesE[i][j].place(relx = sc, rely = sl, anchor = CENTER)
                    sc+=0.06
                    
        if operation == "inversa":
            colun = [0.3, 0.27, 0.24, 0.21, 0.18, 0.15]
            lin = [0.45, 0.4, 0.35, 0.3, 0.25, 0.22]
            
            sl = lin[linhas-1]
            sc = colun[colunas-1]

            for i in range(0, linhas):
                sc = colun[colunas-1]
                if i!=0:
                    sl+=0.085
                for j in range(0, colunas):
                    botoesE[i][j].place(relx = sc, rely = sl, anchor = CENTER)
                    sc+=0.06
                    
        confirmar = Button(janela_operacoes, text = "OK", width = 15, height = 2)
        confirmar.place(relx = 0.5, rely = 0.85, anchor = CENTER)
        confirmar["command"] = partial(preencher, botoesE, confirmar)

class Transposta:
    def __init__(self, janela_operacoes, linhas, colunas):
        def retorno():
            janela_operacoes.destroy()
            jp = Tk()
            JP = GUI_matrizes(jp)
            jp.mainloop()
            
        def preencher(botoesE):
            m = []
            Lbs = []
            
            for i in range(0, linhas):
                l = []
                for j in range(0, colunas):
                    l.append(0)
                matriz.append(l)

            position = 0
            f1 = 0
            f2 = 0

            for i in range(0, linhas):
                for j in range(0, colunas):
                    if "/" in botoesE[i][j].get():
                        for a in range(0, len(botoesE[i][j].get())):
                            if botoesE[i][j].get()[a] == "/":
                                position = a
                                break
                        f1 = float(botoesE[i][j].get()[0:position])
                        f2 = float(botoesE[i][j].get()[position+1:len(botoesE[i][j].get())])
                        matriz[i][j] = f1/f2
                    else:          
                        matriz[i][j] = int(botoesE[i][j].get())

            for i in range(0, colunas):
                l = []
                for j in range(0, linhas):
                    l.append(0)
                m.append(l)

            for i in range(0, colunas):
                l = []
                for j in range(0, linhas):
                    l.append(0)
                Lbs.append(l)

            for i in range(0, linhas):
                for j in range(0, colunas):
                    m[j][i] = matriz[i][j]

            for i in range(0, colunas):
                for j in range(0, linhas):
                    Lbs[i][j] = Label(janela_operacoes, text = str(round(m[i][j], 2)))
                    Lbs[i][j].configure(font = ("Kravitz Extra Thermal",16, "bold"))

            colun = [0.7, 0.67, 0.64, 0.61, 0.58, 0.55]
            lin = [0.45, 0.4, 0.35, 0.3, 0.25, 0.22]
            
            sl = lin[linhas-1]
            sc = colun[colunas-1]

            for i in range(0, colunas):
                sc = colun[colunas-1]
                if i != 0:
                    sl+=0.085
                for j in range(0, linhas):
                    Lbs[i][j].place(relx = sc, rely = sl, anchor = CENTER)
                    sc+=0.06

            botao_final = Button(janela_operacoes, text = "OK", width = 15, height = 2, command = retorno)
            botao_final.place(relx = 0.5, rely = 0.85, anchor = CENTER)

        def destruir(botao):
            botao.destroy()
            
        self.janela_operacoes = janela_operacoes
        self.janela_operacoes.state('normal')
        self.janela_operacoes.title("Operações com matrizes")

        tit = Label(janela_operacoes, text = "DIGITE OS ELEMENTOS")
        tit.configure(font = ("Kravitz Extra Thermal",24, "bold"))
        tit.place(relx = 0.5, rely = 0.07, anchor = CENTER)

        botoesE = []
        matriz = []

        for i in range(0, linhas):
            linha = []
            for j in range(0, colunas):
                linha.append(0)
            botoesE.append(linha)

        for i in range(0, linhas):
            for j in range(0, colunas):
                botoesE[i][j] = Entry(janela_operacoes, width = 2)
                botoesE[i][j].configure(font = ("Kravitz Extra Thermal", 18, "bold"))
                botoesE[i][j].insert(END, "")

        colun = [0.3, 0.27, 0.24, 0.21, 0.18, 0.15]
        lin = [0.45, 0.4, 0.35, 0.3, 0.25, 0.22]
        
        sl = lin[linhas-1]
        sc = colun[colunas-1]

        for i in range(0, linhas):
            sc = colun[colunas-1]
            if i!=0:
                sl+=0.085
            for j in range(0, colunas):
                botoesE[i][j].place(relx = sc, rely = sl, anchor = CENTER)
                sc+=0.06

        confirmar = Button(janela_operacoes, text = "OK", width = 15, height = 2)
        confirmar.place(relx = 0.5, rely = 0.85, anchor = CENTER)
        confirmar["command"] = partial(preencher, botoesE)
        
class Multiplicacao:
    def __init__(self, janela_operacoes, l1, c1, l2, c2, matriz1, matriz2):
        def retorno():
            janela_operacoes.destroy()
            jp = Tk()
            JP = GUI_matrizes(jp)
            jp.mainloop()
            
        def preencher(botoesE1, botoesE2, confirmar):
            confirmar.destroy()

            confirmar = Button(janela_operacoes, text = "OK", width = 15, height = 2, command = retorno)
            confirmar.place(relx = 0.5, rely = 0.925, anchor = CENTER)
            
            m1 = []
            m2 = []
            mr = []
            
            for i in range(0, l1):
                linha = []
                for j in range(0, c1):
                    linha.append(0)
                m1.append(linha)

            for i in range(0, l2):
                linha = []
                for j in range(0, c2):
                    linha.append(0)
                m2.append(linha)

            position = 0
            f1 = 0
            f2 = 0

            for i in range(0, l1):
                for j in range(0, c1):
                    if "/" in botoesE1[i][j].get():
                        for a in range(0, len(botoesE1[i][j].get())):
                            if botoesE1[i][j].get()[a] == "/":
                                position = a
                                break
                        f1 = float(botoesE1[i][j].get()[0:position])
                        f2 = float(botoesE1[i][j].get()[position+1:len(botoesE1[i][j].get())])
                        m1[i][j] = f1/f2
                    else:          
                        m1[i][j] = int(botoesE1[i][j].get())

            position = 0
            f1 = 0
            f2 = 0

            for i in range(0, l2):
                for j in range(0, c2):
                    if "/" in botoesE2[i][j].get():
                        for a in range(0, len(botoesE2[i][j].get())):
                            if botoesE2[i][j].get()[a] == "/":
                                position = a
                                break
                        f1 = float(botoesE2[i][j].get()[0:position])
                        f2 = float(botoesE2[i][j].get()[position+1:len(botoesE2[i][j].get())])
                        m2[i][j] = f1/f2
                    else:          
                        m2[i][j] = int(botoesE2[i][j].get())
                        
            mr = np.matmul(m1, m2)

            Lbs = []

            for i in range(0, len(mr)):
                l = []
                for j in range(0, len(mr[0])):
                    l.append(0)
                Lbs.append(l)

            for i in range(0, len(mr)):
                for j in range(0, len(mr[0])):
                    Lbs[i][j] = Label(janela_operacoes, text = str(round(mr[i][j], 2)))
                    Lbs[i][j].configure(font = ("Kravitz Extra Thermal",16, "bold"))

            colun = [0.5, 0.48, 0.457, 0.436, 0.43, 0.4]
            lin = [0.65, 0.6, 0.65, 0.6, 0.55, 0.52]

            sl = lin[len(mr)-1]
            sc = colun[len(mr[0])-1]

            for i in range(0, len(mr)):
                sc = colun[len(mr[0])-1]
                if i!=0:
                    sl+=0.065
                for j in range(0, len(mr[0])):
                    Lbs[i][j].place(relx = sc, rely = sl, anchor = CENTER)
                    sc+=0.04
            
        self.janela_operacoes = janela_operacoes
        self.janela_operacoes.state('normal')
        self.janela_operacoes.title("Operações com matrizes")

        tit = Label(janela_operacoes, text = "DIGITE OS ELEMENTOS")
        tit.configure(font = ("Kravitz Extra Thermal",24, "bold"))
        tit.place(relx = 0.5, rely = 0.07, anchor = CENTER)

        botoesL1 = []
        botoesE1 = []
        botoesL2 = []
        botoesE2 = []

        sl = 0.28

        for i in range(0, l1):
            linha = []
            for j in range(0, c1):
                linha.append(0)
            botoesE1.append(linha)

        for i in range(0, l2):
            linha = []
            for j in range(0, c2):
                linha.append(0)
            botoesE2.append(linha)

        for i in range(0, l1):
            for j in range(0, c1):
                botoesE1[i][j] = Entry(janela_operacoes, width = 2)
                botoesE1[i][j].configure(font = ("Kravitz Extra Thermal", 18, "bold"))
                botoesE1[i][j].insert(END, "")

        for i in range(0, l2):
            for j in range(0, c2):
                botoesE2[i][j] = Entry(janela_operacoes, width = 2)
                botoesE2[i][j].configure(font = ("Kravitz Extra Thermal", 18, "bold"))
                botoesE2[i][j].insert(END, "")

        colun = [0.3, 0.27, 0.24, 0.21, 0.18, 0.15]
        lin = [0.28, 0.25, 0.22, 0.19, 0.16, 0.13]
        
        sl = lin[l1-1]
        sc = colun[c1-1]

        for i in range(0, l1):
            sc = colun[c1-1]
            if i!=0:
                sl+=0.065
            for j in range(0, c1):
                botoesE1[i][j].place(relx = sc, rely = sl, anchor = CENTER)
                sc+=0.04

        colun = [0.675, 0.675, 0.675, 0.675, 0.66, 0.65]

        sl = lin[l2-1]
        sc = colun[c2-1]

        for i in range(0, l2):
            sc = colun[c2-1]
            if i!=0:
                sl+=0.065
            for j in range(0, c2):
                botoesE2[i][j].place(relx = sc, rely = sl, anchor = CENTER)
                sc+=0.04
                    
        confirmar = Button(janela_operacoes, text = "OK", width = 15, height = 2)
        confirmar.place(relx = 0.5, rely = 0.925, anchor = CENTER)
        confirmar["command"] = partial(preencher, botoesE1, botoesE2, confirmar)

class Operacoes:
    def __init__(self, janela_operacoes, linhas, colunas, array, operation):
        def retorno():
            janela_operacoes.destroy()
            jp = Tk()
            JP = GUI_matrizes(jp)
            jp.mainloop()
            
        def preencher(botoesE1, botoesE2):
            confirmar = Button(janela_operacoes, text = "OK", width = 15, height = 2, command = retorno)
            confirmar.place(relx = 0.5, rely = 0.925, anchor = CENTER)
            
            Lbs = []
            for i in range(0, linhas):
                l = []
                for j in range(0, colunas):
                    l.append(0)
                matriz1.append(l)

            for i in range(0, linhas):
                l = []
                for j in range(0, colunas):
                    l.append(0)
                matriz2.append(l)

            position = 0
            f1 = 0
            f2 = 0

            for i in range(0, linhas):
                for j in range(0, colunas):
                    if "/" in botoesE1[i][j].get():
                        for a in range(0, len(botoesE1[i][j].get())):
                            if botoesE1[i][j].get()[a] == "/":
                                position = a
                                break
                        f1 = float(botoesE1[i][j].get()[0:position])
                        f2 = float(botoesE1[i][j].get()[position+1:len(botoesE1[i][j].get())])
                        matriz1[i][j] = f1/f2
                    else:          
                        matriz1[i][j] = int(botoesE1[i][j].get())

            position = 0
            f1 = 0
            f2 = 0

            for i in range(0, linhas):
                for j in range(0, colunas):
                    if "/" in botoesE2[i][j].get():
                        for a in range(0, len(botoesE2[i][j].get())):
                            if botoesE2[i][j].get()[a] == "/":
                                position = a
                                break
                        f1 = float(botoesE2[i][j].get()[0:position])
                        f2 = float(botoesE2[i][j].get()[position+1:len(botoesE2[i][j].get())])
                        matriz2[i][j] = f1/f2
                    else:          
                        matriz2[i][j] = int(botoesE2[i][j].get())


            array.append(matriz1)
            array.append(matriz2)

            for i in range(0, linhas):
                l = []
                for j in range(0, colunas):
                    l.append(0)
                m.append(l)

                
            if operation == "soma":
                for a in range(len(array)):
                    for i in range(0, linhas):
                        for j in range(0, colunas):
                            m[i][j]+=array[a][i][j]

            if operation == "subtracao":
                for a in range(len(array)):
                    for i in range(0, linhas):
                        for j in range(0, colunas):
                            if a == 0:
                                m[i][j]+=array[a][i][j]
                            else:
                                m[i][j]-=array[a][i][j]

            for i in range(0, linhas):
                l = []
                for j in range(0, colunas):
                    l.append(0)
                m.append(l)

            for i in range(0, linhas):
                l = []
                for j in range(0, colunas):
                    l.append(0)
                Lbs.append(l)

            for i in range(0, linhas):
                for j in range(0, colunas):
                    Lbs[i][j] = Label(janela_operacoes, text = str(round(m[i][j], 2)))
                    Lbs[i][j].configure(font = ("Kravitz Extra Thermal",16, "bold"))

            colun = [0.5, 0.48, 0.457, 0.436, 0.43, 0.4]
            lin = [0.65, 0.6, 0.65, 0.6, 0.55, 0.52]

            sl = lin[linhas-1]
            sc = colun[colunas-1]

            for i in range(0, linhas):
                sc = colun[colunas-1]
                if i!=0:
                    sl+=0.065
                for j in range(0, colunas):
                    Lbs[i][j].place(relx = sc, rely = sl, anchor = CENTER)
                    sc+=0.04
                    
        def destruir(botao):
            botao.destroy()

        self.janela_operacoes = janela_operacoes
        self.janela_operacoes.state('normal')
        self.janela_operacoes.title("Operações com matrizes")

        tit = Label(janela_operacoes, text = "DIGITE OS ELEMENTOS")
        tit.configure(font = ("Kravitz Extra Thermal",24, "bold"))
        tit.place(relx = 0.5, rely = 0.07, anchor = CENTER)

        botoesE1 = []
        botoesE2 = []
        matriz1 = []
        matriz2 = []
        m = []

        for i in range(0, linhas):
            linha = []
            for j in range(0, colunas):
                linha.append(0)
            botoesE1.append(linha)

        for i in range(0, linhas):
            linha = []
            for j in range(0, colunas):
                linha.append(0)
            botoesE2.append(linha)

        for i in range(0, linhas):
            for j in range(0, colunas):
                botoesE1[i][j] = Entry(janela_operacoes, width = 2)
                botoesE1[i][j].configure(font = ("Kravitz Extra Thermal", 18, "bold"))
                botoesE1[i][j].insert(END, "")

        for i in range(0, linhas):
            for j in range(0, colunas):
                botoesE2[i][j] = Entry(janela_operacoes, width = 2)
                botoesE2[i][j].configure(font = ("Kravitz Extra Thermal", 18, "bold"))
                botoesE2[i][j].insert(END, "")

        colun = [0.3, 0.27, 0.24, 0.21, 0.18, 0.15]
        lin = [0.28, 0.25, 0.22, 0.19, 0.16, 0.13]
        
        sl = lin[linhas-1]
        sc = colun[colunas-1]

        for i in range(0, linhas):
            sc = colun[colunas-1]
            if i!=0:
                sl+=0.065
            for j in range(0, colunas):
                botoesE1[i][j].place(relx = sc, rely = sl, anchor = CENTER)
                sc+=0.04

        colun = [0.675, 0.675, 0.675, 0.675, 0.66, 0.65]

        sl = lin[linhas-1]
        sc = colun[colunas-1]

        for i in range(0, linhas):
            sc = colun[colunas-1]
            if i!=0:
                sl+=0.065
            for j in range(0, colunas):
                botoesE2[i][j].place(relx = sc, rely = sl, anchor = CENTER)
                sc+=0.04
                
        if operation == "soma":
            tit2 = Button(janela_operacoes, text = "+", width = 15, height = 2)
            tit2.place(relx = 0.5, rely = 0.25, anchor = CENTER)
            tit2["command"] = partial(preencher, botoesE1, botoesE2)
        if operation == "subtracao":
            tit2 = Button(janela_operacoes, text = "-", width = 15, height = 2)
            tit2.place(relx = 0.5, rely = 0.25, anchor = CENTER)
            tit2["command"] = partial(preencher, botoesE1, botoesE2)

class GUI_matrizes:
    def __init__(self, janela):
        self.janela = janela
        self.janela.state('normal')
        self.janela.title("Operações com matrizes")

        self.janela.texto_selecione = Label(janela, text = "OPERAÇÕES COM MATRIZES: SELECIONE A OPERAÇÃO")
        self.janela.texto_selecione.configure(font = ("Kravitz Extra Thermal",24, "bold"))
        self.janela.texto_selecione.place(relx = 0.5, rely = 0.05, anchor = CENTER)

        self.janela.soma = Button(janela, text = "SOMAR", command = self.botao_soma)
        self.janela.subtracao = Button(janela, text = "SUBTRAIR", command = self.botao_subtracao)
        self.janela.multiplicacao = Button(janela, text = "MULTIPLICAR", command = self.botao_multiplicacao)
        self.janela.determinante = Button(janela, text = "DETERMINANTE", command = self.botao_determinante)
        self.janela.inversa = Button(janela, text = "INVERSA", command = self.botao_inversa)
        self.janela.transposta = Button(janela, text = "TRANSPOSTA", command = self.botao_transposta)

        self.janela.soma.place(relx = 0.5, rely = 0.18, width = 400, height = 90, anchor = CENTER)
        self.janela.subtracao.place(relx = 0.5, rely = 0.31, width = 400, height = 90, anchor = CENTER)
        self.janela.multiplicacao.place(relx = 0.5, rely = 0.44, width = 400, height = 90, anchor = CENTER)
        self.janela.determinante.place(relx = 0.5, rely = 0.57, width = 400, height = 90, anchor = CENTER)
        self.janela.inversa.place(relx = 0.5, rely = 0.7, width = 400, height = 90, anchor = CENTER)
        self.janela.transposta.place(relx = 0.5, rely = 0.83, width = 400, height = 90, anchor = CENTER)

    def botao_soma(self):
        operation = "soma"
        self.janela.soma.destroy()
        self.janela.linhaL = Label(self.janela, text = "Número de linhas:")
        self.janela.colunaL = Label(self.janela, text = "Número de colunas:")

        self.janela.linhaE = Entry(self.janela)
        self.janela.colunaE = Entry(self.janela)

        self.janela.OK = Button(self.janela, text = "OK", width = 10)
        self.janela.OK["command"] = partial(self.get_parametros, self.janela.linhaE, self.janela.colunaE, operation)

        self.janela.linhaL.place(relx = 0.39, rely = 0.165, anchor = CENTER)
        self.janela.colunaL.place(relx = 0.394, rely = 0.195, anchor = CENTER)

        self.janela.linhaE.place(relx = 0.49, rely = 0.165, anchor = CENTER)
        self.janela.colunaE.place(relx = 0.49, rely = 0.195, anchor = CENTER)

        self.janela.OK.place(relx = 0.6, rely = 0.18, anchor = CENTER)

    def botao_subtracao(self):
        operation = "subtracao"
        self.janela.subtracao.destroy()
        self.janela.linhaL = Label(self.janela, text = "Número de linhas:")
        self.janela.colunaL = Label(self.janela, text = "Número de colunas:")

        self.janela.linhaE = Entry(self.janela)
        self.janela.colunaE = Entry(self.janela)

        self.janela.OK = Button(self.janela, text = "OK", width = 10)
        self.janela.OK["command"] = partial(self.get_parametros, self.janela.linhaE, self.janela.colunaE, operation)

        self.janela.linhaL.place(relx = 0.39, rely = 0.285, anchor = CENTER)
        self.janela.colunaL.place(relx = 0.394, rely = 0.315, anchor = CENTER)

        self.janela.linhaE.place(relx = 0.49, rely = 0.285, anchor = CENTER)
        self.janela.colunaE.place(relx = 0.49, rely = 0.315, anchor = CENTER)

        self.janela.OK.place(relx = 0.6, rely = 0.3, anchor = CENTER)

    def botao_multiplicacao(self):
        def retorno(erro):
            erro.destroy()
            jp = Tk()
            JP = GUI_matrizes(jp)
            jp.mainloop()
            
        def multiplicacao_possivel():
            c1 = int(self.janela.matrizesE2.get())
            l2 = int(self.janela.matrizesE3.get())
            if c1==l2:
                l1 = int(self.janela.matrizesE1.get())
                c1 = int(self.janela.matrizesE2.get())
                l2 = int(self.janela.matrizesE3.get())
                c2 = int(self.janela.matrizesE4.get())

                matriz1 = []
                matriz2 = []

                for i in range(0, l1):
                    linha = []
                    for j in range(0, c1):
                        linha.append(0)
                    matriz1.append(linha)

                for i in range(0, l2):
                    linha = []
                    for j in range(0, c2):
                        linha.append(0)
                    matriz2.append(linha)
                    
                self.janela.destroy()
                op_m = Tk()
                OP_M = Multiplicacao(op_m, l1, c1, l2, c2, matriz1, matriz2)
                op_m.mainloop()
                
            else:
                self.janela.destroy()
                erro = Tk()
                erro.state('normal')
                erro.title("Erro")
                Aviso_1 = Label(erro, text = "AVISO")
                Aviso_2 = Label(erro, text = "O número de colunas da primeira matriz\ndeve ser igual ao número de linhas da segunda matriz")
                Aviso_1.configure(font = ("Kravitz Extra Thermal",24, "bold"))
                Aviso_2.configure(font=("Kravitz Extra Thermal", 16, "bold"))
                Aviso_1.place(relx = 0.5, rely = 0.05, anchor = CENTER)
                Aviso_2.place(relx = 0.5, rely = 0.5, anchor = CENTER)

                confirmar = Button(erro, text = "OK", width = 15, height = 2)
                confirmar.place(relx = 0.5, rely = 0.85, anchor = CENTER)
                confirmar["command"] = partial(retorno, erro)

                erro.mainloop()

        self.janela.multiplicacao.destroy()
        self.janela.matrizesL1 = Label(self.janela, text = "Número de linhas: ")
        self.janela.matrizesC1 = Label(self.janela, text = "Número de colunas: ")
        self.janela.matrizesL2 = Label(self.janela, text = "Número de linhas: ")
        self.janela.matrizesC2 = Label(self.janela, text = "Número de colunas: ")

        self.janela.matrizesE1 = Entry(self.janela)
        self.janela.matrizesE2 = Entry(self.janela)
        self.janela.matrizesE3 = Entry(self.janela)
        self.janela.matrizesE4 = Entry(self.janela)

        self.janela.OK = Button(self.janela, text = "OK", width = 10, command = multiplicacao_possivel)
        
        self.janela.matrizesL1.place(relx = 0.39, rely = 0.39, anchor = CENTER)
        self.janela.matrizesE1.place(relx = 0.49, rely = 0.39, anchor = CENTER)
        
        self.janela.matrizesC1.place(relx = 0.39, rely = 0.42, anchor = CENTER)
        self.janela.matrizesE2.place(relx = 0.49, rely = 0.42, anchor = CENTER)

        self.janela.matrizesL2.place(relx = 0.39, rely = 0.45, anchor = CENTER)
        self.janela.matrizesE3.place(relx = 0.49, rely = 0.45, anchor = CENTER)

        self.janela.matrizesC2.place(relx = 0.39, rely = 0.48, anchor = CENTER)
        self.janela.matrizesE4.place(relx = 0.49, rely = 0.48, anchor = CENTER)
        self.janela.OK.place(relx = 0.6, rely = 0.44, anchor = CENTER)

    def botao_determinante(self):
        operation = "determinante"
        self.janela.determinante.destroy()
        self.janela.ordemL = Label(self.janela, text = "Ordem da matriz:")

        self.janela.ordemE = Entry(self.janela)

        self.janela.OK = Button(self.janela, text = "OK", width = 10)
        self.janela.OK["command"] = partial(self.get_parametros_quadradas, self.janela.ordemE, operation)

        self.janela.ordemL.place(relx = 0.39, rely = 0.57, anchor = CENTER)

        self.janela.ordemE.place(relx = 0.49, rely = 0.57, anchor = CENTER)

        self.janela.OK.place(relx = 0.6, rely = 0.57, anchor = CENTER)

    def botao_inversa(self):
        operation = "inversa"
        self.janela.inversa.destroy()
        self.janela.ordemL = Label(self.janela, text = "Ordem da matriz:")

        self.janela.ordemE = Entry(self.janela)

        self.janela.OK = Button(self.janela, text = "OK", width = 10)
        self.janela.OK["command"] = partial(self.get_parametros_quadradas, self.janela.ordemE, operation)

        self.janela.ordemL.place(relx = 0.39, rely = 0.701, anchor = CENTER)

        self.janela.ordemE.place(relx = 0.49, rely = 0.701, anchor = CENTER)

        self.janela.OK.place(relx = 0.6, rely = 0.701, anchor = CENTER)

    def botao_transposta(self):
        self.janela.transposta.destroy()
        self.janela.linhaL = Label(self.janela, text = "Número de linhas:")
        self.janela.colunaL = Label(self.janela, text = "Número de colunas:")

        self.janela.linhaE = Entry(self.janela)
        self.janela.colunaE = Entry(self.janela)

        self.janela.OK = Button(self.janela, text = "OK", width = 10)
        self.janela.OK["command"] = partial(self.get_parametros_transposta, self.janela.linhaE, self.janela.colunaE)

        self.janela.linhaL.place(relx = 0.39, rely = 0.81, anchor = CENTER)
        self.janela.colunaL.place(relx = 0.394, rely = 0.84, anchor = CENTER)

        self.janela.linhaE.place(relx = 0.49, rely = 0.81, anchor = CENTER)
        self.janela.colunaE.place(relx = 0.49, rely = 0.84, anchor = CENTER)

        self.janela.OK.place(relx = 0.6, rely = 0.825, anchor = CENTER)

    def get_parametros(self, linhaE, colunaE, operation):
        array = []
        linhas = int(linhaE.get())
        colunas = int(colunaE.get())

        self.janela.destroy()

        op = Tk()
        OP = Operacoes(op, linhas, colunas, array, operation)
        op.mainloop()           

    def get_parametros_transposta(self, linhaE, colunaE):
        linhas = int(linhaE.get())
        colunas = int(colunaE.get())

        self.janela.destroy()

        op_t = Tk()
        OP_T = Transposta(op_t, linhas, colunas)
        op_t.mainloop()

    def get_parametros_quadradas(self, ordemE, operation):
        ordem = int(ordemE.get())

        self.janela.destroy()

        op_q = Tk()
        OP_Q = Quadradas(op_q, ordem, operation)
        op_q.mainloop()

janela_principal = Tk()
GUI = GUI_matrizes(janela_principal)
janela_principal.mainloop()

