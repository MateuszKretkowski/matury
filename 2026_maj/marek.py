plik = open("korpo_przyklad.txt", "r")

# tab = [0] * 50_000
# print(tab[0:5])

# for line in plik:
#     line = int(line.rstrip())
#     tab[line - 1] += 1

# counter = 0

# for i in range(len(tab)):
#     if tab[i] == 0:
#         counter += 1

# print(tab[0:5])
# print(counter + 1)  # 2

# index = -1
# count = 0

# for i in range(len(tab)):
#     if index == -1 or count < tab[i]:
#         index = i
#         count = tab[i]

# print(index + 1)
# print(count)


tab = []

for line in plik:
    line = int(line.rstrip())
    tab.append(line - 1)

max_powiazanie = 0
pracownik = 0

# 0
# 1
# 1
#

for i in range(len(tab)):
    licznik = 0
    indeks = i
    while indeks != 0:
        indeks = tab[indeks]
        licznik += 1

    if licznik > max_powiazanie:
        pracownik = indeks + 1
        max_powiazanie = licznik

counter = 0
for i in range(len(tab)):
    licznik = 0
    indeks = i
    while indeks != 0:
        indeks = tab[indeks]
        licznik += 1

    if licznik == max_powiazanie:
        counter += 1

print(pracownik)
print(counter)
