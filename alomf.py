import re

def replaceStringReverse(string,num):
    if num == 0: return string
    stringInReverse = string[:-num] + "B"*num
    return stringInReverse

def replaceStringForward(string,num):
    stringForward = string
    stringForward = "B"*num + stringForward[num:]
    return stringForward

def replaceStringToA(string,num):
    replacedString = string
    replacedString = string[:num] + "A" + string[num+1:]
    return replacedString

def stringAB(n,k):
    dapAn = []
    dapAnDung = []
    dapAnDung = []
    fullAString = "A"*n
    dapAn.append(fullAString)
    for i in range(n-k+1):
        subjectString = fullAString
        subjectString = replaceStringReverse(subjectString,(n-k)-i)
        subjectString = replaceStringForward(subjectString,i)
        dapAn.append(subjectString)

    for i in dapAn:
        for j in range(len(i)):
            if i[j] == "B" :
                dapAn.append(replaceStringToA(i,j))
    dapAn = list(set(dapAn))
    for i in dapAn:
        if "A"*(k+1) not in i and i.count("A"*k) == 1:
            dapAnDung.append(i)
    return sorted(dapAnDung)
    asd
print(stringAB(7,4))