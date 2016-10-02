
def commonDivisor (firstNum,secondNum):
    if (firstNum < secondNum):
        if (secondNum % firstNum == 0):
            print("The greatest common divisor is: "
                                      , firstNum)
        else:
            if (firstNum % (secondNum % firstNum) == 0):
                print("The greatest common divisor is: " , (secondNum % firstNum))
            else:
                print ("The greatest common divisor is: 1" )

    if (secondNum < firstNum):

        if (firstNum % secondNum == 0):
            print("The greatest common divisor is: " + secondNum)
        else:
            if (secondNum % (firstNum % secondNum) == 0):
                print("The greatest common divisor is: " , (firstNum % secondNum))
            else:
                print("The greatest common divisor is: 1" )




def main():
    firstNum = 27
    secondNum = 15

    print (commonDivisor (firstNum, secondNum))




if __name__== "__main__" :main()