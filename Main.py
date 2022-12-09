x = float(input("Podaj x: "))
k = int(input("Podaj k: "))

def binary(x, k):
    print("0,", end='')
    y = x
    for i in range(k):
        if y >= 1/2:
            print("1", end='')
        else:
            print("0", end='')
        y = y*2
        if y >= 1:
            y = y-1


def trinary(x, k):
    print("0,", end='')
    y = x
    for i in range(k):
        if y >= 2/3:
            print("2", end='')
        elif y >= 2/9:
            print("1", end='')
        elif y >= 2/27:
            print("0", end='')
        y = y * 3
        if y >= 2:
            y = y - 2
        elif y >= 1:
            y = y - 1


binary(x, k)
print(" ", end='')
trinary(x, k)
