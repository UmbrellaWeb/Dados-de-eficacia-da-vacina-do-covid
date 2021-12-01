ARQ = open('dados.txt', 'r')
linha = ARQ.readlines()
QTD = int(linha[0])
parti = []
for li in linha:
    parti.append(li.replace('\n', ''))
    pessoas = []
    for i in parti:
        if "," in i:
            pessoas.append(i.split(","))
print (pessoas)
ARQ.close()

def Genero ():
    genero =[]
    cont = 0
    for lista in pessoas:
        genero.append(lista[0])
        cont =  cont+1
    quantF = genero.count('F')
    quantM = genero.count('M')
    F = quantF *100/QTD
    M = quantM *100/QTD
    print("-="*30)
    print ("-> O percentual de participantes Femininos é de: {}%\n-> A Percentual de parcipantes Maculinos é de: {}%".format(F,M))
    

def idades():
    idade= []
    for JAV in pessoas:
        idade.append(int(JAV[1]))
    J = A = V = 0
    for i in idade:
        if i <=  19:
            J = J +1
        elif i > 19 and i <= 59:
            A = A +1
        else:
            V = V +1
    J = J*100/QTD
    A = A*100/QTD
    V = V*100/QTD
    print("-="*20)
    print (f'-> A pocentagem de Jovens é de {J}%\n-> A de adulto é {A}%\n-> A de idosos é {V}%')
    

def VacinaPlacebo():
    PV = []
    for vp in pessoas:
        PV.append(vp[2])
        V = PV.count('V')
        P = PV.count('P')
        V = V*100/QTD
        P = P*100/QTD
    print("-="*20)
    print (f'-> A pocentagem de quen recebeu a "Vacina" é de: {V}%\n-> e para os que receberam "Placebo" e de: {P}%')
    

def SecontrauCovid():
    sn = []
    for ns in pessoas:
        sn.append(ns[3])
        s = sn.count('S')
        n = sn.count('N')
        s = s*100/QTD
        n = n*100/QTD
    print("-="*20)
    print (f'-> A pocentagem de infectados é de {s}% para "Sim" e {n}% para "Não"')


def eficaciadaVacina():   
    a = b =  0
    for eficacia in pessoas:
        if eficacia[2]== 'P' and eficacia[3] == 'S':
            a = a +1
        if eficacia[2] == 'V' and eficacia[3] == 'S':
            b = b +1
    eficacia1 = 100 * (a - b) / a
    print("-="*20)
    print (f'-> A eficacia de vacina é de: {round(eficacia1,2)}%')


def pocentagemIdades():
    #Jovem
    Jp = len([id for id in pessoas if int(id[1])<=19 and id[2]== 'P' and id[3]=='S'])
    Jv = len([id for id in pessoas if int(id[1])<=19 and id[2]== 'V' and id[3]=='S'])
    eficaciaJ = 100 * (Jp - Jv) / Jp
    #Adulto
    Ap = len([id for id in pessoas if int(id[1]) > 19 and int(id[1]) <= 59 and id[2]== 'P' and id[3]=='S'])
    Av = len([id for id in pessoas if int(id[1]) > 19 and int(id[1]) <= 59 and id[2]== 'V' and id[3]=='S'])
    eficaciaA = 100 * (Ap - Av) / Ap
    #idoso
    Ip = len([id for id in pessoas if int(id[1]) > 59 and id[2]== 'P' and id[3]=='S'])
    Iv = len([id for id in pessoas if int(id[1]) > 59 and id[2]== 'V' and id[3]=='S'])
    eficaciaI = 100 * (Ip - Iv) / Ip
    print("-="*20)
    print(f'-> A eficaciada da vacina em jovens foi de: {eficaciaJ}%\n-> A eficacia da vacina em Adutos é de: {eficaciaA}%\n-> A eficacia em idosos é de: {eficaciaI}%')







def pocengener():
    #Mulher 
    FP = len([PV for PV in pessoas if PV[0] == 'F' and PV[2] == 'P' and PV[3] == 'S'])    
    FV = len([PV for PV in pessoas if PV[0] == 'F' and PV[2] == 'V' and PV[3] == 'S'])
    #Homem
    MP = len([PV for PV in pessoas if PV[0] == 'M' and PV[2] == 'P' and PV[3] == 'S'])    
    MV = len([PV for PV in pessoas if PV[0] == 'M' and PV[2] == 'V' and PV[3] == 'S'])
    eficaciaF = 100 * (FP - FV) / FP
    eficaciaM = 100 * (MP - MV) / MP
    print("-="*20)
    print (f'-> A eficacia da vacina em mulheres é de: {eficaciaF}%\n-> A eficacia da vacina para homens foi DE: {eficaciaM}%') 