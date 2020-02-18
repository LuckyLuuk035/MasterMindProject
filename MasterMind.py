import random

index = []
allOptions = [] 
for a in range(1,7):
    for b in range(1,7):
        for c in range(1,7):
            for d in range(1,7):
                allOptions.append(str(a)+str(b)+str(c)+str(d))
trueKey = allOptions[random.randint(0,1296)] 

def checkKey(secretKey, question):
    g = 0 
    b = 0 
    tempQ = [] 
    tempK = [] 
    result = []
    for i in range(4):
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

    
def computer():
    trueKey = input('Vul een combinatie naar keuze in: ')
    ronde = 0
    while True:
        ronde += 1
        for i in allOptions:
            if checkKey(trueKey, allOptions[0]) != checkKey(allOptions[0], i):
                index.append(allOptions.index(i))
        a = 0
        for i in index:
            allOptions.remove(allOptions[i - a])
            a += 1
        index.clear()
        if len(allOptions) == 1:
            print('het antwoord: '+ allOptions[0] + ' is in ' + str(ronde) + ' rondes gevonden')
            break
    


computer()
