with open("./Dane_2305/pi.txt", "r") as plik:
    linie = plik.readlines()

def zad3_1():
    lista = []
    for i in range(1, len(linie)):
        prev = linie[i-1].rstrip()
        linia = linie[i].rstrip()
        print(prev, linia)
        stringa = str(prev + linia)
        print(stringa)
        lista.append(int(stringa))
    counter = 0
    for i in lista:
        if i > 90:
            counter += 1
    return counter

def zad3_2():
    hm = {}
    for i in range(1, len(linie)):
        prev = linie[i-1].rstrip()
        linia = linie[i].rstrip()
        liczba = str(prev + linia)
        liczba = int(liczba)
        print(liczba)
        if not hm.__contains__(liczba):
            hm[liczba] = 1
        else:
            hm[liczba] += 1
    for i in range(0, 99):
        if not hm.__contains__(i):
            hm[i] = 0
    mini = 0
    miniCont = 100000000
    maxi = 0
    maxiCount = 0
    for i in hm.keys():
        if hm[i]>maxiCount:
            maxi = i
            maxiCount = hm[i]
        if hm[i]<miniCont:
            mini = i
            miniCont = hm[i]
    return mini, miniCont, maxi, maxiCount

def sprawdzCiag(ciag):
    index = 0
    jestMal = False
    jestRos = False
    breaked = False
    while index<len(ciag)-1:
        i = int(ciag[index])
        j = int(ciag[index+1])
        print(i, j, index)
        if j > i:
            jestRos = True
        if j < i:
            jestMal = True
            
        if jestMal and jestRos == False:
            breaked = True
            break
        if i == j and (jestMal and jestRos):
            breaked = True
            break
        if index <= 1 and j < i:
            breaked = True
            break
        if jestMal == True and j > i:
            breaked = True
            break
        index += 1
    if jestRos == True and jestMal == True and breaked == False:
        return True
    return False
    

def zad3_3():
    counter = 0
    for i in range(0, len(linie)-5):
        ciag = [linie[i].rstrip(), linie[i+1].rstrip(), linie[i+2].rstrip(), linie[i+3].rstrip(), linie[i+4].rstrip(), linie[i+5].rstrip()]
        print(ciag)
        if sprawdzCiag(ciag) == True:
            print("jest!!!")
            counter += 1
    return counter
#TUTAJ SKONCZYLEM WYMIAROWY CZAS

def zad3_4():
    ans = 0
    count = 0
    pos = 0
    for i in range(0, len(linie)-5):
        for j in range(i+6, len(linie)-5):
            diff = j - i
            ciag = []
            for x in range(i, j):
                ciag.append(linie[x].rstrip())
            print(ciag)
            if sprawdzCiag(ciag) == True:
                print("jest!!!")
                if diff > count:
                    print(diff)
                    count = diff
                    ans = ciag
                    pos = i
            else:
                break

    return ans, pos

print(zad3_4())
