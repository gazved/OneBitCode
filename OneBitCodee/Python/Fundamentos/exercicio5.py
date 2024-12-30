def numMaiusculas(str):
    qtdM =0
    for x in str:
        if x.isupper():
            qtdM +=1
    return qtdM

palavra = "oiOO"

print(numMaiusculas(palavra))


def SepararEven(*num):
    Pares = []
    Impar = []
    for x in num:
        if x%2 ==0:
            Pares.append(x)
        else:
            Impar.append(x)
    print(Pares)
    print(Impar)            