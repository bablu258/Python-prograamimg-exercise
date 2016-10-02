class Area:

    totalArea = float(0)

    def __init__(self, *args):
        self.var = args


    def getAreaOfRhombus(self):
        a = self.var[0]
        b = self.var[1]
        ar = float ((a * b) / 2)
        Area.totalArea += ar

    def getAreaOfSuare(self):
        a = self.var[0]
        ar = float (pow(a, 2))
        Area.totalArea += ar

    def getAreOfPara (self):
        a = self.var[0]
        b = self.var[1]
        ar = float (a * b)
        Area.totalArea += ar

    def getAreOfQuadrilater (self):
        a = self.var[0]
        b = self.var[1]
        ar = float (a * b)
        Area.totalArea += ar

    def getAreOfCircle(self):
        a = self.var[0]
        ar = float (3.14 * (a**2))
        Area.totalArea += ar

class Parallegram (Area):


    def display (self):
        print " Total area of parallogram is " ,Area.totalArea


class Rhombus(Area):


    def display(self):
      print " Total area of Rhombus is " , Area.totalArea

class Quadrli (Area):

    def display(self):
        print " Total area of quadrilateral is ", Area.totalArea

class Square (Area):

    def display(self):
        print " Total area of square is ",Area.totalArea

class Cicle (Area):

    def display(self):
        print " Total area of circle is ", Area.totalArea


def main ():

    userInput = int (raw_input(" Enter 1 for rhombus, 2 for paralleogram, 3 for square, 4 for circle and 5 for quadrilateral "))

    if (userInput == 1):

        fiNum = int(raw_input("Enter first number"))
        seNum = int(raw_input("Enter second number"))
        obj = Rhombus(fiNum, seNum)
        obj.display()

    elif (userInput == 2):
        fiNum = int(raw_input("Enter first number"))
        seNum = int(raw_input("Enter second number"))
        obj = Parallegram(fiNum, seNum)
        obj.display()

    elif (userInput == 3):
        fiNum = int(raw_input("Enter a number"))
        obj = Square(fiNum)
        obj.display()

    elif (userInput == 4):
        fiNum = int(raw_input("Enter a number"))
        obj = Cicle(fiNum)
        obj.display()

    elif (userInput == 5):
        fiNum = int(raw_input("Enter first number"))
        seNum = int(raw_input("Enter second number"))
        obj = Quadrli(fiNum, seNum)
        obj.display()

    else:
        print ("You have entered wrong input")

if __name__ == "__main__": main()
