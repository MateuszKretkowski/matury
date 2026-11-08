def binarny(a):
    binar = 0
    curr = a
    counter = 0
    if a % 2 != 0:
        binar = 1
        curr = a - 1
    i = a
    while i > 1:
        if jestPotega(i, 1) == False or curr - i < 0:
            i = i-1
            continue
        counter = power(10, jestPotega(i, 0))
        curr = curr - i
        binar = counter + binar
        counter /= 10
        i /= 2
    return binar

def power(n, w):
    for i in range(1, w):
        n = n * 10
    return n

def jestPotega(n, c):
    if n < 2:
        return c
    while True:
        if n%2==0:
            return jestPotega(n/2, c + 1)
        else:
            return False
        
def bloki(binar):
    counter = 1
    i = 2
    curr = (binar % (power(10, i-1)))
    blok = True
    while power(10, i-1) < binar:
        if (binar % (power(10, i))) // power(10, i-1) != curr:
            counter += 1
            print("counter: ", counter)
            blok = False
        elif (binar % (power(10, i))) // power(10, i-1) == curr:
            blok = True
        i += 1
        curr = (binar % (power(10, i-1))) // power(10, i-2)
    return counter

plik = open("./Dane_2305/bin.txt", "r")

def zad2_2():
    counter = 0
    for i in plik:
        i = i.rstrip()
        print(i)
        if bloki(int(i)) <= 2:
            counter += 1
    return counter

def zad2_3():
    liczba = 0
    asci = 0
    for i in plik:
        curr = 0
        i = str(i.rstrip())
        for j in range(len(i)-1, 0, -1):
            curr += int(i[j]) * pow(2, len(i)-j)
        print(curr)
        if curr > liczba:
            asci = i
            liczba = curr
        print((i))
    return liczba, asci

odp = open("./wyniki5.txt", "a")

def zad2_5():
    liczba = 0
    asci = 0
    for i in plik:
        curr = int(i, 2) // 2
        i = str(i.rstrip())
        curr = str(bin(curr))[2:]
        
        print(i, curr)
        wynik = i
        while len(i) != (len(curr)):
            if min(len(i), (len(curr)-2)) == len(i):
                i = '0' + i
            elif min(len(i), (len(curr))) == len(curr):
                curr = '0' + curr
        print(i, curr)
        for x in range(len(i)-1, 0, -1):
            wynik = wynik[:x] + str(int(i[x]) ^ int(curr[x], 2)) + wynik[x+1:]
        print("wynuik:  ", wynik)
        odp.write(wynik)
        odp.write("\n")
zad2_5()