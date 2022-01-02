from tkinter import *

def criar_triangulo_de_Pascal():
    n = int(tfN.get())
    a = int(tfAlfa.get())
    b = int(tfBeta.get())
    p = []
    s = []
    lbp = []
    lbs = []
    for i in range(n+1):
        aux = []
        for j in range(n+1):
            aux.append(0)
        p.append(aux)
    
    p[0][0] = 1
    p[1][0] = 1
    p[1][1] = 1

    for i in range(2, n+1):
        for j in range(n+1):
            if j == 0 or i == j:
                p[i][j] = 1
            if i>j:
                p[i][j] = p[i-1][j]+p[i-1][j-1]

    lbPascal = Label(janela, text = "Triângulo de Pascal")
    lbPascal.grid(row = 5, column = 0)

    for i in range(n+1):
        aux = []
        for j in range(n+1):
            if p[i][j]!=0:
                aux.append(Label(janela,text = str(p[i][j])))
            else:
                aux.append(Label(janela))
        lbp.append(aux)

    for i in range(n+1):
        for j in range(n+1):
            lbp[i][j].grid(row = 7+i, column = j, padx = 50)

    lbSakashita = Label(janela, text = "Triângulo de Sakashita")
    lbSakashita.grid(row = 8+n, column = 0)

    for i in range(n+1):
        aux = []
        for j in range(n+1):
            aux.append(0)
        s.append(aux)

    for i in range(n+1):
        for j in range(n+1):
            s[i][j] = p[i][j]*((a/b)**i)*((b/a)**j)

    for i in range(n+1):
        aux = []
        for j in range(n+1):
            if s[i][j]!=0:
                aux.append(Label(janela,text = str(s[i][j])))
            else:
                aux.append(Label(janela))
        lbs.append(aux)

    for i in range(n+1):
        for j in range(n+1):
            lbs[i][j].grid(row = 9+n+i, column = j, padx = 50)

janela = Tk()

lbAlfa = Label(janela, text = "Alfa")
tfAlfa = Entry(janela)

lbBeta = Label(janela, text = "Beta")
tfBeta = Entry(janela)

lbN = Label(janela, text = "n")
tfN = Entry(janela)

lbVazio = Label(janela)

btOK = Button(janela, text = "OK", width = 17, command = criar_triangulo_de_Pascal)

lbAlfa.grid(row = 0, column = 0)
tfAlfa.grid(row = 0, column = 1)
lbBeta.grid(row = 1, column = 0)
tfBeta.grid(row = 1, column = 1)
lbN.grid(row = 2, column = 0)
tfN.grid(row = 2, column = 1)
lbVazio.grid(row = 3, column = 0)
btOK.grid(row = 3, column = 1)


janela.mainloop()
