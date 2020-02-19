import random

def options():
    allOptions = []
    for a in range(1,7):
        for b in range(1,7):
            for c in range(1,7):
                for d in range(1,7):
                    allOptions.append(str(a)+str(b)+str(c)+str(d))
    return allOptions


def checkKey(secretKey, question):
    allOptions = options()
    g, b = 0, 0 #g staat voor goed en b voor bijna goed
    tempQ = []
    tempK = []
    result = []
    
    for i in range(len(allOptions[0])):
        if question[i] == secretKey[i]:
            g += 1
        else:
            tempQ.append(int(question[i]))
            tempK.append(int(secretKey[i]))

    for i in range(len(tempQ)): 
        if tempQ[i] in tempK:
            b += 1
            tempK.remove(tempQ[i])
    result.append(g)
    result.append(b)
    return result

def zelfRaden():
    allOptions = options()
    trueKey = allOptions[random.randint(0,len(allOptions))]
    ronde = 1
    while True:
        question = str(input('ronde '+str(ronde)+' wat is je keuze? '))
        if question == '!^&*#': #Dit is om te kunnen checken wat de question is
            print('Cheat code geactiveerd:\n'+str(trueKey))
            question = str(input('ronde '+str(ronde)+' wat is je keuze? '))
        print(str(checkKey(trueKey, question)[0])+' waren op de juiste plek.\n'+ str(checkKey(trueKey, question)[1])+' waren in de combinatie maar niet op de juiste plek\n')
        if checkKey(trueKey, question)[0] == int(len(allOptions[0])):
            print('je hebt gewonnen in '+str(ronde)+' rondes!')
            break
        else:
            ronde += 1

def simpleStrategy():    
    trueKey = input("Vul een 4 cijfer getal in: ")
    allOptions = options()
    index = []
    ronde = 0
    while True:
        ronde += 1
        if len(allOptions) == 1 or checkKey(trueKey, allOptions[0]) == [4,0]:
            print('De computer heeft de combinatie: ' + allOptions[0] + ' gevonden in ' + str(ronde) + ' rondes.\n')
            break
        print('Ronde: ' + str(ronde) + '\nDe combinatie: ' + trueKey + '\nDe question: ' + allOptions[0] + '\nGoed en bijna goed: ' + str(checkKey(trueKey, allOptions[0])) + '\nOvergebleven opties: ' + str(len(allOptions)) + '\n')
        for i in allOptions:
            if checkKey(trueKey, allOptions[0]) != checkKey(allOptions[0], i):
                index.append(allOptions.index(i))
        a = 0 #a is gemaakt om de error tegen te gaan als je iets verwijdert terwijl je door dezelfde lijst heen gaat.
        for i in index:
            allOptions.remove(allOptions[i - a])
            a += 1
        index.clear()

def worstCase():
    trueKey = input("Vul een 4 cijfer getal in: ")
    allOptions = options()
    index = []
    ronde = 0
    while True:
        ronde += 1
        if ronde == 1:
            if checkKey(trueKey, allOptions[0]) == [4,0]:
                print('De computer heeft de combinatie: 1122 gevonden in ' + str(ronde) + ' ronde.\n')
            print('Ronde: ' + str(ronde) + '\nDe combinatie: ' + trueKey + '\nDe question: 1122 \nGoed en bijna goed: ' + str(checkKey(trueKey, allOptions[0])) + '\nOvergebleven opties: ' + str(len(allOptions)) + '\n')
            for i in allOptions:
                if checkKey(trueKey, '1122') != checkKey('1122', i):
                    index.append(allOptions.index(i))

        else:
            if len(allOptions) == 1 or checkKey(trueKey, allOptions[0]) == [4,0]:
                print('De computer heeft de combinatie: ' + allOptions[0] + ' gevonden in ' + str(ronde) + ' rondes.\n')
                break
            print('Ronde: ' + str(ronde) + '\nDe combinatie: ' + trueKey + '\nDe question: ' + allOptions[0] + '\nGoed en bijna goed: ' + str(checkKey(trueKey, allOptions[0])) + '\nOvergebleven opties: ' + str(len(allOptions)) + '\n')
            for i in allOptions:
                if checkKey(trueKey, allOptions[0]) != checkKey(allOptions[0], i):
                    index.append(allOptions.index(i))
        a = 0 #a is gemaakt om de error tegen te gaan als je iets verwijdert terwijl je door dezelfde lijst heen gaat.
        for i in index:
            allOptions.remove(allOptions[i - a])
            a += 1
        index.clear()

def selfmade():
#Dit is mogelijk sneller dan de eerste strategie doordat je de question laat afwisselen van de middelste uit de lijst en de laatste
#Dit zorgt er voor dat de hogere combinaties sneller word gevonden. helaas is dit niet effectief bij combinaties als 1111
    trueKey = input("Vul een 4 cijfer getal in: ")
    allOptions = options()
    index = []
    ronde = 0
    while True:
        ronde += 1
        if ronde % 2 == 0:
            question = allOptions[-1]
        else:
            question = allOptions[int(len(allOptions)/2)]
        
        if len(allOptions) == 1 or checkKey(trueKey, question) == [4,0]:
            print('De computer heeft de combinatie: ' + question + ' gevonden in ' + str(ronde) + ' rondes.\n')
            break
        print('Ronde: ' + str(ronde) + '\nDe combinatie: ' + trueKey + '\nDe question: ' + question + '\nGoed en bijna goed: ' + str(checkKey(trueKey, question)) + '\nOvergebleven opties: ' + str(len(allOptions)) + '\n')
        
        for i in allOptions:
            if checkKey(trueKey, question) != checkKey(question, i):
                index.append(allOptions.index(i))
        a = 0 #a is gemaakt om de error tegen te gaan als je iets verwijdert terwijl je door dezelfde lijst heen gaat.
        for i in index:
            allOptions.remove(allOptions[i - a])
            a += 1
        index.clear()

while True:
    keuze = int(input('1) Zelf de combinatie raden \n2) Laat de computer de combinatie raden met A Simpele Stretegy \n3) Laat de computer de combinatie raden met Worst Case Strategy \n4) Laat een zelfgemaakt algoritme raden \n5) Sluit het programma af \n(1/2/3/4/5) \n'))
    if keuze == 1:
        zelfRaden()
    elif keuze == 2:
        simpleStrategy()
    elif keuze == 3:
        worstCase()
    elif keuze == 4:
        selfmade()
    elif keuze == 5:
        break
    else:
        print(str(keuze)+' is geen geldige optie \nprobeer opnieuw')


#BRONNEN----------------------------------------------------------------------------
#http://scholar.google.nl/scholar_url?url=https://lirias.kuleuven.be/retrieve/36247&hl=nl&sa=X&scisig=AAGBfm282whxVVZS4jwNytbsoK8ZI7bRUA&nossl=1&oi=scholarr
#-----------------------------------------------------------------------------------
