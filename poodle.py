def numeroResult(N, P):
    if N % P == 0:
        return N/P
    else:
        return (N/P) + 1

def organizaLetras(N, P):

    resultado = numeroResult(N,P)
    if(resultado <= 6):
        return "Poogle"
    elif(resultado >= 20):
        return "Poooooooooooooooodle"
    else:
        a = resultado - 4
        b = ""
        for i in range(a):
            b=b+"o"
        return "P"+b+"dle"

def confirmando(N,P):
    if(N==0 and P==0):
        return 0
    else:
        print organizaLetras(N, P)
        return 1

inicio = 1

while inicio == 1:
    N = int(raw_input())
    P = int(raw_input())
    inicio = confirmando(N, P)
