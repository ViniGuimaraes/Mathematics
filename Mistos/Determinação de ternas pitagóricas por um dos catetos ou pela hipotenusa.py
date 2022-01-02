def escolhas_catetos2(a):
    for d in range(1, a, 2):
        if a**2%d == 0 and ((a**2)/d) % 2 != 0:
            b = (a**2-d**2)/(2*d)
            c = (a**2+d**2)/(2*d)
            c1, c2, h = ordenacao(a, b, c)
            tipo = mdc(c1, c2, h)
            if tipo == 1:
                simetrico = simetria(c1, c2, h)
                if simetrico == True:
                    print(c1, c2, h, "TERNA PRIMITIVA E SIMÉTRICA\n")
                else:
                    print(c1, c2, h, "TERNA PRIMITIVA E NÃO SIMÉTRICA\n")
            else:
                simetrico = simetria(c1, c2, h)
                if simetrico == True:
                    print(c1, c2, h, "TERNA SECUNDÁRIA E SIMÉTRICA\n")
                else:
                    print(c1, c2, h, "TERNA SECUNDÁRIA E NÃO SIMÉTRICA\n")

def escolhas_catetos1(a):
    for d in range(2, a, 2):
        if (a**2)%d == 0 and ((a**2)/d) % 2 == 0:
            b = (a**2-d**2)/(2*d)
            c = (a**2+d**2)/(2*d)
            c1, c2, h = ordenacao(a, b, c)
            tipo = mdc(c1, c2, h)
            if tipo == 1:
                simetrico = simetria(c1, c2, h)
                if simetrico == True:
                    print(c1, c2, h, "TERNA PRIMITIVA E SIMÉTRICA\n")
                else:
                    print(c1, c2, h, "TERNA PRIMITIVA E NÃO SIMÉTRICA\n")
            else:
                simetrico = simetria(c1, c2, h)
                if simetrico == True:
                    print(c1, c2, h, "TERNA SECUNDÁRIA E SIMÉTRICA\n")
                else:
                    print(c1, c2, h, "TERNA SECUNDÁRIA E NÃO SIMÉTRICA\n")
                    
def alg(c, n, a, b):
    q = n/c
    a, b, c = ordenacao(a, b, c)
    a = a*q
    b = b*q
    c = c*q
    return a, b, c

def last(c):
    a = 0
    b = 0
    n = 0
    k = 0
    while 4*n**2+4*n*k+12*n+2*k**2+10*k+13 <= c:
        k = 0
        while 4*n**2+4*n*k+12*n+2*k**2+10*k+13 <= c:
            if c == 4*n**2+4*n*k+12*n+2*k**2+10*k+13:
                a = 4*k*n+2*k+4*n**2+12*n+5
                b = (4+2*k)*(k**2+4*k*n+6*k+4*n**2+12*n+9)**(1/2)
                return True, a, b, c
            k+=1
        k = 0
        n+=1
    return False, 0, 0, 0

def escolhas1(c):
    h = 0
    z = triangular(c)
    if z == True:
       a = (2*c-1)**(1/2)
       b = c-1
       return True, a, b, c
 
    else:
        z = quadrado(c)
        if z == True:
            a = 2*(c-1)**(1/2)
            b = c - 2
            if mdc(a, b, c) == 1:
                return True, a, b, c

        else:
            z, n, k = polinomio(c)
            if z == True:
                a = 4*k*n+2*k+4*n**2+12*n+5
                b = (4+2*k)*(k**2+4*k*n+6*k+4*n**2+12*n+9)**(1/2)
                return True, a, b, c
            else:
                return False, 0, 0, 0


def impar(n, fat):
    ternas = []
    a = 0
    b = 0
    c = 0
    x = 0
    y = 0
    z = 0
    if len(fat)>1:                
        for i in range(0, len(fat)):
            if fat[i] == c:
                continue
            else:
                k, a, b, c = escolhas1(fat[i])
                if k == True:
                    x, y, z = alg(fat[i], n, a, b)
                    ternas.extend([x, y, z])
                else:
                    k, a, b, c = last(fat[i])
                    if k == True:
                        x, y, z = alg(fat[i], n, a, b)
                        ternas.extend([x, y, z])
        if len(ternas) == 0:
            return False, ternas
        else:
            return True, ternas
    return False, ternas
               
def fatores(n):
    b = 0
    ternas = []
    h = n
    x = 0
    y = 0
    z = 0
    fat = []
    d = 2
    while n>1:
        if n%d == 0:
            n=n/d
            fat.append(d)
        else:
            d+=1
    b, ternas = impar(h, fat)
    return b, ternas

def polinomiol1(c, n, k):
    k+=1
    if 4*n**2+4*n*k+12*n+2*k**2+10*k+13 >= c:
        if 4*n**2+4*n*k+12*n+2*k**2+10*k+13 == c:
            c1 = 4*k*n+2*k+4*n**2+12*n+5
            b = (4+2*k)*(k**2+4*k*n+6*k+4*n**2+12*n+9)**(1/2)
            c1, b, c = ordenacao(c1, b, c)
            escolhas(c1, b, c)
        else:
            n+=1
            k = 0
            while 4*n**2+4*n*k+12*n+2*k**2+10*k+13 <= c:
                k = 0
                while 4*n**2+4*n*k+12*n+2*k**2+10*k+13 <= c:
                    if c == 4*n**2+4*n*k+12*n+2*k**2+10*k+13:
                        c1 = 4*k*n+2*k+4*n**2+12*n+5
                        b = (4+2*k)*(k**2+4*k*n+6*k+4*n**2+12*n+9)**(1/2)
                        c1, b, c = ordenacao(c1, b, c)
                        escolhas(c1, b, c)
                    k+=1
                k = 0
                n+=1
            return False, k, n
                
def polinomiol(c, a):
    c1 = 0
    b = 0
    n = 0
    k = 0
    while 4*n**2+4*n*k+12*n+2*k**2+10*k+13 <= c:
        k = 0
        while 4*n**2+4*n*k+12*n+2*k**2+10*k+13 <= c:
            if c == 4*n**2+4*n*k+12*n+2*k**2+10*k+13:
                c1 = 4*k*n+2*k+4*n**2+12*n+5
                if c1 == a:
                    pass
                else:
                    b = (4+2*k)*(k**2+4*k*n+6*k+4*n**2+12*n+9)**(1/2)
                    c1, b, c = ordenacao(c1, b, c)
                    escolhas(c1, b, c)
            k+=1
        k = 0
        n+=1
    return False, k, n

def simetria(a, b, c):
    if b == (a+c)/2:
        return True
    else:
        return False
    
def mdc(a, b, c):
    mdc = b
    while b % mdc != 0 or c % mdc != 0:
        mdc-=1
    mdc2 = a
    while a % mdc2 != 0 or mdc % mdc2 != 0:
        mdc2-=1
    return mdc2

def ordenacao(a, b, c):
    c2 = 0
    vetor = [a, b, c]
    h = max(vetor)
    c1 = min(vetor)
    for i in range(0, 2):
        if vetor[i]!=h and vetor[i]!=c1:
            c2 = vetor[i]
    return c1, c2, h

def escolhas(a, b, c):
    x = 0
    a, b, c = ordenacao(a, b, c)
    tipo = mdc(a, b, c)
    if tipo == 1:
        x = simetria(a, b, c)
        if x == True:
            print(a, b, c, "TERNA PRIMITIVA E SIMÉTRICA\n")
        else:
            print(a, b, c, "TERNA PRIMITIVA E NÃO SIMÉTRICA\n")
    else:
        x = simetria(a, b, c)
        if x == True:
            print(a, b, c, "TERNA SECUNDÁRIA E SIMÉTRICA\n")
        else:
            print(a, b, c, "TERNA SECUNDÁRIA E NÃO SIMÉTRICA\n")
            
def polinomio(c):
    n = 0
    k = 0
    while 4*n**2+4*n*k+12*n+2*k**2+10*k+13 <= c:
        k = 0
        while 4*n**2+4*n*k+12*n+2*k**2+10*k+13 <= c:
            if c == 4*n**2+4*n*k+12*n+2*k**2+10*k+13:
                return True, n, k
            k+=1
        k = 0
        n+=1
    return False, k, n

def quadrado(c):
    a = 0
    i = 1
    n = 0
    while 5+4*(i-1)<=c:
        if 5+4*(i-1) == c:
            a = True
            break
        i+=1
    if a == True:
        for n in range(1, i+1):
            if i == n**2:
                return True
        return False
    else:
        return False
def triangular(c):
    a = 0
    i = 1
    n = 0
    while 5+4*(i-1)<=c:
        if 5+4*(i-1) == c:
            a = True
            break
        i+=1
    if a == True:
        for n in range(1, i+1):
            if i == (n**2+n)/2:
                return True
        return False
    else:
        return False

def op2(c, i):
   ternas = [] 
   j = True 
   h = c
   a, ternas = fatores(c)
   if a != False:
       j = False
       for g in range(0, len(ternas), 3):
           a = ternas[g]*2**i
           b = ternas[g+1]*2**i
           h = ternas[g+2]*2**i
           escolhas(a, b, h)
   if j == True:
       z = triangular(c)
       if z == True:
          a = (2**i)*((2*c-1)**(1/2))
          b = (2**i)*(c-1)
          c = (2**i)*c
          z = polinomiol(c, a)
          escolhas(a, b, c)
       else:
            z = quadrado(c)
            if z == True:
                a = (2**i)*(2*(c-1)**(1/2))
                b = (2**i)*(c - 2)
                c = (2**i)*c
                z = polinomiol(c, a)
                escolhas(a, b, c)
            else:
                z, n, k = polinomio(c)
                if z == True:
                    a = (2**i)*(4*k*n+2*k+4*n**2+12*n+5)
                    b = (2**i)*((4+2*k)*(k**2+4*k*n+6*k+4*n**2+12*n+9)**(1/2))
                    c = (2**i)*c
                    z = polinomiol1(c, n, k)
                    escolhas(a, b, c)
                else:
                    print("NÃO EXISTE TERNA PITAGÓRICA COM ESSA HIPOTENUSA\n")
              
def op1(c):
    ternas = []
    a = 0
    b = 0
    z = triangular(c)
    if z == True:
       a = (2*c-1)**(1/2)
       b = c-1
       z = polinomiol(c, a)
       escolhas(a, b, c)
       a, ternas = fatores(c)
       if a!=False:
           for i in range(0, len(ternas), 3):
               a = ternas[i]
               b = ternas[i+1]
               c = ternas[i+2]
               escolhas(a, b, c)
    else:
        z = quadrado(c)
        if z == True:
            a = 2*(c-1)**(1/2)
            b = c - 2
            z = polinomiol(c, a)
            escolhas(a, b, c)
            a, ternas = fatores(c)
            if a!= False:
                for i in range(0, len(ternas), 3):
                    a = ternas[i]
                    b = ternas[i+1]
                    c = ternas[i+2]
                    escolhas(a, b, c)
        else:
            z, n, k = polinomio(c)
            if z == True:
                a = 4*k*n+2*k+4*n**2+12*n+5
                b = (4+2*k)*(k**2+4*k*n+6*k+4*n**2+12*n+9)**(1/2)
                z = polinomiol1(c, n, k)
                escolhas(a, b, c)
                a, ternas = fatores(c)
                if a != False:
                    if ternas[1] != b:
                        for i in range(0, len(ternas), 3):
                            a = ternas[i]
                            b = ternas[i+1]
                            c = ternas[i+2]
                            escolhas(a, b, c)
            else:
                l = 0
                a, ternas = fatores(c)
                if a!= False:
                    for i in range(0, len(ternas), 3):
                        a = ternas[i]
                        b = ternas[i+1]
                        c = ternas[i+2]
                        escolhas(a, b, c)
                else:
                    print("NÃO EXISTE TERNA PITAGÓRICA COM ESSA HIPOTENUSA\n")

def paridade(c):
    n = 0
    h = 0
    if c%2 == 0:
        while c%2 == 0:
            c/=2
            n+=1
        return c, n
    else:
        return c, False
   
def main():
    n = 0
    i = 0
    while True:
        print("I - CATETO\nII - HIPOTENUSA\n")
        i = input("Escolha uma das opções e digite um valor para: ")
        partes = i.split()
        if len(partes) != 2:
            print("ENTRADA INVÁLIDA. TENTE NOVAMENTE\n")
        if not(partes[0].isnumeric()) and partes[1].isnumeric():
            opcao = partes[0]
            c = int(partes[1])
            a = int(partes[1])

            if opcao == "Hipotenusa" or opcao == "hipotenusa" or opcao == "h" or opcao == "II" or opcao == "ii":
                if c <= 0:
                    print("NÃO EXISTE TERNA PITAGÓRICA COM ESSA HIPOTENUSA\n")
                else:
                    c, n = paridade(c)
                    if n == False:
                        op1(c)
                    else:
                        op2(c, n)
            elif opcao == "Cateto" or opcao == "cateto" or opcao == "c" or opcao == "I" or opcao == "i":
                if a<=2:
                    print("NÃO EXISTE TERNA PITAGÓRICA COM ESSE CATETO\n")
                else:
                    n, p = paridade(a)
                    if p != False:
                        escolhas_catetos1(a)
                    else:
                        escolhas_catetos2(a)       
            else:
                print("COMANDO INVÁLIDO. ESCREVA NOVAMENTE\n")
        else:
            print("ENTRADA INVÁLIDA. TENTE NOVAMENTE\n")
main()

