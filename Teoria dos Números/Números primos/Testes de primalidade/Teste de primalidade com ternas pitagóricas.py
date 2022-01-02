def mdc(a, b):
    return a if not b else mdc(b, a % b)

a = int(input("Digite o valor de x+1: "))
if a%2 == 0:
    print(a, " é número composto")
else:
    n = int((a-1)/2)
    x = 2*n
    v = int(((x+1)**(1/2))/2)
    b = True
    for j in range(1, v+2):
        if j%3==5 and j%5==13:
            continue
        else:
            h = 4*j**2+4*x*j+2*x**2+2*x+1
            c1 = 4*j**2+4*x*j-(2*x+1)
            c2 = (4*x+4)*j+(2*x**2+2*x)
            boolean = mdc(h, mdc(c1, c2))
            if boolean!=1:
                print(x+1, " é número composto")
                b = False
                break
    if b == True:
        print(x+1, " é número primo")

