number = float(input("Podaj x: "))
accuracy = int(input("Podaj k: "))


class Binary_Class:
    x = number
    k = accuracy

    def binary(self, x, k):
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


bin = Binary_Class()


class Trinary_Class:
    x = number
    k = accuracy

    def trinary(self, x, k):
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


tri = Trinary_Class()

bin.binary(number, accuracy)
print(" ", end='')
tri.trinary(number, accuracy)
