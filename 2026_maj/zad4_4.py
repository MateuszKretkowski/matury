with open("korpo.txt", "r") as f:
    lines = [l.rstrip() for l in f.readlines()]
przyklad = open("korpo_przyklad.txt", "r")
ans = open("wyniki4.txt", "a")

max = 0
max_counter = 0


def zad():
    global max, max_counter
    for i in range(0, len(lines)):
        line = lines[i].rstrip()
        curr = get_przelozonych(line, 0)
        print("counter: ", curr)
        if curr > max:
            max = curr
            max_counter = 1
        else:
            max_counter += 1


def get_przelozonych(line, counter):
    if int(line) == 0:
        return counter
    counter += 1
    print(line)
    przelozony = lines[int(lines[int(line) - 1])]
    return get_przelozonych(przelozony, counter)


zad()
print(max, max_counter)
