file = open("korpo.txt", "r")
przyklad = open("korpo_przyklad.txt", "r")
ans = open("wyniki4.txt", "a")

hm = {}
max = None
def zad(hm):
    lines = file.readlines()
    for i in range(0, len(lines)):
        line = lines[i].strip()
        if line not in hm:
            hm[line] = 0
        hm[line] += 1
    global max
    for i in hm.keys():
        if max is None or hm[i] > hm[max]:
            max = i
zad(hm)
ans.write(str(max) + '\n')
print(hm, max)