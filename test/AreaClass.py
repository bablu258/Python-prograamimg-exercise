import math

class Area:


    def __init__(self, *args):
        self.var = args



    def getAreaOfRhombus(self):
        a = self.var[0]
        b = self.var[1]
        ar = float ((a * b) / 2)
        print (ar)

    def getAreOfretangular (self):
        a = self.var[0]
        b = self.var[1]
        ar = float (a * b)
        print (ar)

    def getAreaOfSuare(self):
        a = self.var[0]
        ar = float (pow(a, 2))
        print (ar)


def main ():

    userInput = int (raw_input(" Enter 1 for rhombus, 2 for rectangular, 3 for square"))

    if (userInput == 1):

        fiNum = int(raw_input("Enter first number"))
        seNum = int(raw_input("Enter second number"))
        obj = Area(fiNum,seNum)
        obj.getAreaOfRhombus()

    elif (userInput == 2):
        fiNum = int(raw_input("Enter first number"))
        seNum = int(raw_input("Enter second number"))
        obj = Area(fiNum, seNum)
        obj.getAreOfretangular()
    else:
        fiNum = int(raw_input("Enter a number"))
        obj = Area(fiNum)
        obj.getAreaOfSuare()

if __name__ == "__main__": main()