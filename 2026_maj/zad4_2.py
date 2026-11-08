file = open("korpo.txt", "r")
przyklad = open("korpo_przyklad.txt", "r")
ans = open("wyniki4.txt", "a")

hm = {}
counter = 0


def zad(hm):
    lines = file.readlines()
    for i in range(0, len(lines)):
        line = lines[i].strip()
        if line not in hm:
            hm[line] = 0
        hm[line] += 1
    global counter
    counter = len(lines) - len(hm.keys()) + 1


zad(hm)
print(hm, counter)
ans.write(str(counter))
