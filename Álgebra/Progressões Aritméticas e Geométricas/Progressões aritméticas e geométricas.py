from tkinter import *
from functools import partial

def PG3(vetor):
    if vetor[len(vetor)-1] == "PA1":
        frPA1.grid_forget()
    elif vetor[len(vetor)-1] == "PA2":
        frPA2.grid_forget()
    elif vetor[len(vetor)-1] == "PA3":
        frPA3.grid_forget()
    elif vetor[len(vetor)-1] == "PG1":
        frPG1.grid_forget()
    elif vetor[len(vetor)-1] == "PG2":
        frPG2.grid_forget()
    elif vetor[len(vetor)-1] == "PG3":
        frPG3.grid_forget()
    vetor.append("PG3")
    frPG3.grid(row = 1, column = 0)

def PG2(vetor):
    if vetor[len(vetor)-1] == "PA1":
        frPA1.grid_forget()
    elif vetor[len(vetor)-1] == "PA2":
        frPA2.grid_forget()
    elif vetor[len(vetor)-1] == "PA3":
        frPA3.grid_forget()
    elif vetor[len(vetor)-1] == "PG1":
        frPG1.grid_forget()
    elif vetor[len(vetor)-1] == "PG2":
        frPG2.grid_forget()
    elif vetor[len(vetor)-1] == "PG3":
        frPG3.grid_forget()
    vetor.append("PG2")
    frPG2.grid(row = 1, column = 0)

def PG1(vetor):
    if vetor[len(vetor)-1] == "PA1":
        frPA1.grid_forget()
    elif vetor[len(vetor)-1] == "PA2":
        frPA2.grid_forget()
    elif vetor[len(vetor)-1] == "PA3":
        frPA3.grid_forget()
    elif vetor[len(vetor)-1] == "PG1":
        frPG1.grid_forget()
    elif vetor[len(vetor)-1] == "PG2":
        frPG2.grid_forget()
    elif vetor[len(vetor)-1] == "PG3":
        frPG3.grid_forget()
    vetor.append("PG1")
    frPG1.grid(row = 1, column = 0)

def PA3(vetor):
    if vetor[len(vetor)-1] == "PA1":
        frPA1.grid_forget()
    elif vetor[len(vetor)-1] == "PA2":
        frPA2.grid_forget()
    elif vetor[len(vetor)-1] == "PA3":
        frPA3.grid_forget()
    elif vetor[len(vetor)-1] == "PG1":
        frPG1.grid_forget()
    elif vetor[len(vetor)-1] == "PG2":
        frPG2.grid_forget()
    elif vetor[len(vetor)-1] == "PG3":
        frPG3.grid_forget()
    vetor.append("PA3")
    frPA3.grid(row = 1, column = 0)

def PA2(vetor):
    if vetor[len(vetor)-1] == "PA1":
        frPA1.grid_forget()
    elif vetor[len(vetor)-1] == "PA2":
        frPA2.grid_forget()
    elif vetor[len(vetor)-1] == "PA3":
        frPA3.grid_forget()
    elif vetor[len(vetor)-1] == "PG1":
        frPG1.grid_forget()
    elif vetor[len(vetor)-1] == "PG2":
        frPG2.grid_forget()
    elif vetor[len(vetor)-1] == "PG3":
        frPG3.grid_forget()
    vetor.append("PA2")
    frPA2.grid(row = 1, column = 0)
    
def PA1(vetor):
    if vetor[len(vetor)-1] == "PA1":
        frPA1.grid_forget()
    elif vetor[len(vetor)-1] == "PA2":
        frPA2.grid_forget()
    elif vetor[len(vetor)-1] == "PA3":
        frPA3.grid_forget()
    elif vetor[len(vetor)-1] == "PG1":
        frPG1.grid_forget()
    elif vetor[len(vetor)-1] == "PG2":
        frPG2.grid_forget()
    elif vetor[len(vetor)-1] == "PG3":
        frPG3.grid_forget()
    vetor.append("PA1")
    
    frPA1.grid(row = 1, column = 0)

def PA1_Sequencia(seq_term):
    if seq_term[len(seq_term)-1] == "Termo":
        lbTermoPA1.grid_forget()
        tfTermoPA1.grid_forget()
        btCalcularTermoPA1.grid_forget()
    elif seq_term[len(seq_term)-1] == "Sequencia":
        lbSequenciaPA1.grid_forget()
        tfSequenciaPA1.grid_forget()
        btCalcularSequenciaPA1.grid_forget()
    seq_term.append("Sequencia")
    lbSequenciaPA1.grid(row = 4, column = 0)
    tfSequenciaPA1.grid(row = 4, column = 1)
    btCalcularSequenciaPA1.grid(row = 7, column = 0, columnspan = 2, sticky = W+E)

def PA1_Termo_CalculoTermo(tfR, tfa1, tfn):
    k = int(tfR.get())
    a1 = int(tfa1.get())
    n = int(tfn.get())

    an = a1+(n-1)*k
    lbResultado = Label(frPA1, text = "a"+str(n)+" = "+str(an), bg = "green")
    lbResultado.grid(row = 8, column = 0, columnspan = 2, sticky = W+E)
    

def PA1_Termo(seq_term):
    if seq_term[len(seq_term)-1] == "Termo":
        lbTermoPA1.grid_forget()
        tfTermoPA1.grid_forget()
        btCalcularTermoPA1.grid_forget()
    elif seq_term[len(seq_term)-1] == "Sequencia":
        lbSequenciaPA1.grid_forget()
        tfSequenciaPA1.grid_forget()
        btCalcularSequenciaPA1.grid_forget()
    seq_term.append("Termo")
    lbTermoPA1.grid(row = 4, column = 0)
    tfTermoPA1.grid(row = 4, column = 1)
    btCalcularTermoPA1.grid(row = 7, column = 0, columnspan = 2, sticky = W+E)
    

janela = Tk()

frToolBar = Frame(janela, bg = "gray")

global vetor
vetor = [""]

global seq_term
seq_term = [""]


btPA1 = Button(frToolBar, text = "PA1", width = 5, command = partial(PA1, vetor))
btPA2 = Button(frToolBar, text = "PA2", width = 5, command = partial(PA2, vetor))
btPA3 = Button(frToolBar, text = "PA3", width = 5, command = partial(PA3, vetor))
btPG1 = Button(frToolBar, text = "PG1", width = 5, command = partial(PG1, vetor))
btPG2 = Button(frToolBar, text = "PG2", width = 5, command = partial(PG2, vetor))
btPG3 = Button(frToolBar, text = "PG3", width = 5, command = partial(PG3, vetor))

#PA1
frPA1 = Frame(janela)
lbVazio1 = Label(frPA1)
lbVazio2 = Label(frPA1)
lbVazio3 = Label(frPA1)

lbTipo = Label(frPA1, text = "Progressão aritmética de primeira ordem")
lbRazao = Label(frPA1, text = "Razão (k)")
tfRazao = Entry(frPA1)
lba1PA1 = Label(frPA1, text = "a1")
tfa1PA1 = Entry(frPA1)
btTermoPA1 = Button(frPA1, text = "Termo", command = partial(PA1_Termo, seq_term))
btSequenciaPA1 = Button(frPA1, text = "Sequência", command = partial(PA1_Sequencia, seq_term))

lbTermoPA1 = Label(frPA1, text = "Termo da sequência")
tfTermoPA1 = Entry(frPA1)

lbSequenciaPA1 = Label(frPA1, text = "Número de termos")
tfSequenciaPA1 = Entry(frPA1)

btCalcularTermoPA1 = Button(frPA1, text = "Calcular", command = partial(PA1_Termo_CalculoTermo, tfRazao, tfa1PA1, tfTermoPA1))
btCalcularSequenciaPA1 = Button(frPA1, text = "Calcular")

lbTipo.grid(row = 0, column = 0)
lbVazio1.grid(row = 1, column = 0)
lbRazao.grid(row = 2, column = 0)
tfRazao.grid(row = 2, column = 1)
lba1PA1.grid(row = 3, column = 0)
tfa1PA1.grid(row = 3, column = 1)
lbVazio2.grid(row = 4, column = 0)
lbVazio3.grid(row = 5, column = 0)
btTermoPA1.grid(row = 6, column = 0)
btSequenciaPA1.grid(row = 6, column = 1)

#PA2
frPA2 = Frame(janela)
lbVazio1 = Label(frPA2)
lbVazio2 = Label(frPA2)
lbVazio3 = Label(frPA2)

lbTipo = Label(frPA2, text = "Progressão aritmética de segunda ordem")
lbRazao = Label(frPA2, text = "Razão (k)")
tfRazao = Entry(frPA2)
lba1PA2 = Label(frPA2, text = "a1")
tfa1PA2 = Entry(frPA2)
lba2PA2 = Label(frPA2, text = "a2")
tfa2PA2 = Entry(frPA2)
btTermoPA2 = Button(frPA2, text = "Termo")
btSequenciaPA2 = Button(frPA2, text = "Sequência")

lbTipo.grid(row = 0, column = 0)
lbVazio1.grid(row = 1, column = 0)
lbRazao.grid(row = 2, column = 0)
tfRazao.grid(row = 2, column = 1)
lba1PA2.grid(row = 3, column = 0)
tfa1PA2.grid(row = 3, column = 1)
lba2PA2.grid(row = 4, column = 0)
tfa2PA2.grid(row = 4, column = 1)
lbVazio2.grid(row = 5, column = 0)
lbVazio3.grid(row = 6, column = 0)
btTermoPA2.grid(row = 7, column = 0)
btSequenciaPA2.grid(row = 7, column = 1)

#PA3
frPA3 = Frame(janela)
lbVazio1 = Label(frPA3)
lbVazio2 = Label(frPA3)
lbVazio3 = Label(frPA3)

lbTipo = Label(frPA3, text = "Progressão aritmética de terceira ordem")
lbRazao = Label(frPA3, text = "Razão (k)")
tfRazao = Entry(frPA3)
lba1PA3 = Label(frPA3, text = "a1")
tfa1PA3 = Entry(frPA3)
lba2PA3 = Label(frPA3, text = "a2")
tfa2PA3 = Entry(frPA3)
lba3PA3 = Label(frPA3, text = "a3")
tfa3PA3 = Entry(frPA3)
btTermoPA3 = Button(frPA3, text = "Termo")
btSequenciaPA3 = Button(frPA3, text = "Sequência")

lbTipo.grid(row = 0, column = 0)
lbVazio1.grid(row = 1, column = 0)
lbRazao.grid(row = 2, column = 0)
tfRazao.grid(row = 2, column = 1)
lba1PA3.grid(row = 3, column = 0)
tfa1PA3.grid(row = 3, column = 1)
lba2PA3.grid(row = 4, column = 0)
tfa2PA3.grid(row = 4, column = 1)
lba3PA3.grid(row = 5, column = 0)
tfa3PA3.grid(row = 5, column = 1)
lbVazio2.grid(row = 6, column = 0)
lbVazio3.grid(row = 7, column = 0)
btTermoPA3.grid(row = 8, column = 0)
btSequenciaPA3.grid(row = 8, column = 1)

#PG1
frPG1 = Frame(janela)
lbVazio1 = Label(frPG1)
lbVazio2 = Label(frPG1)
lbVazio3 = Label(frPG1)

lbTipo = Label(frPG1, text = "Progressão geométrica de primeira ordem")
lbRazao = Label(frPG1, text = "Razão (k)")
tfRazao = Entry(frPG1)
lba1PG1 = Label(frPG1, text = "a1")
tfa1PG1 = Entry(frPG1)
btTermoPG1 = Button(frPG1, text = "Termo")
btSequenciaPG1 = Button(frPG1, text = "Sequência")

lbTipo.grid(row = 0, column = 0)
lbVazio1.grid(row = 1, column = 0)
lbRazao.grid(row = 2, column = 0)
tfRazao.grid(row = 2, column = 1)
lba1PG1.grid(row = 3, column = 0)
tfa1PG1.grid(row = 3, column = 1)
lbVazio2.grid(row = 4, column = 0)
lbVazio3.grid(row = 5, column = 0)
btTermoPG1.grid(row = 6, column = 0)
btSequenciaPG1.grid(row = 6, column = 1)

#PG2
frPG2 = Frame(janela)
lbVazio1 = Label(frPG2)
lbVazio2 = Label(frPG2)
lbVazio3 = Label(frPG2)

lbTipo = Label(frPG2, text = "Progressão aritmética de segunda ordem")
lbRazao = Label(frPG2, text = "Razão (k)")
tfRazao = Entry(frPG2)
lba1PG2 = Label(frPG2, text = "a1")
tfa1PG2 = Entry(frPG2)
lba2PG2 = Label(frPG2, text = "a2")
tfa2PG2 = Entry(frPG2)
btTermoPG2 = Button(frPG2, text = "Termo")
btSequenciaPG2 = Button(frPG2, text = "Sequência")

lbTipo.grid(row = 0, column = 0)
lbVazio1.grid(row = 1, column = 0)
lbRazao.grid(row = 2, column = 0)
tfRazao.grid(row = 2, column = 1)
lba1PG2.grid(row = 3, column = 0)
tfa1PG2.grid(row = 3, column = 1)
lba2PG2.grid(row = 4, column = 0)
tfa2PG2.grid(row = 4, column = 1)
lbVazio2.grid(row = 5, column = 0)
lbVazio3.grid(row = 6, column = 0)
btTermoPG2.grid(row = 7, column = 0)
btSequenciaPG2.grid(row = 7, column = 1)

btPA1.grid(row = 0, column = 0, padx = 5)
btPA2.grid(row = 0, column = 1, padx = 5)
btPA3.grid(row = 0, column = 2, padx = 5)
btPG1.grid(row = 0, column = 3, padx = 5)
btPG2.grid(row = 0, column = 4, padx = 5)
btPG3.grid(row = 0, column = 5, padx = 5)

#PG3
frPG3 = Frame(janela)
lbVazio1 = Label(frPG3)
lbVazio2 = Label(frPG3)
lbVazio3 = Label(frPG3)

lbTipo = Label(frPG3, text = "Progressão aritmética de terceira ordem")
lbRazao = Label(frPG3, text = "Razão (k)")
tfRazao = Entry(frPG3)
lba1PG3 = Label(frPG3, text = "a1")
tfa1PG3 = Entry(frPG3)
lba2PG3 = Label(frPG3, text = "a2")
tfa2PG3 = Entry(frPG3)
lba3PG3 = Label(frPG3, text = "a3")
tfa3PG3 = Entry(frPG3)
btTermoPG3 = Button(frPG3, text = "Termo")
btSequenciaPG3 = Button(frPG3, text = "Sequência")

lbTipo.grid(row = 0, column = 0)
lbVazio1.grid(row = 1, column = 0)
lbRazao.grid(row = 2, column = 0)
tfRazao.grid(row = 2, column = 1)
lba1PG3.grid(row = 3, column = 0)
tfa1PG3.grid(row = 3, column = 1)
lba2PG3.grid(row = 4, column = 0)
tfa2PG3.grid(row = 4, column = 1)
lba3PG3.grid(row = 5, column = 0)
tfa3PG3.grid(row = 5, column = 1)
lbVazio2.grid(row = 6, column = 0)
lbVazio3.grid(row = 7, column = 0)
btTermoPG3.grid(row = 8, column = 0)
btSequenciaPG3.grid(row = 8, column = 1)

frToolBar.grid(row = 0, column = 0, sticky = W+E)

janela.mainloop()

