
class PerfectNumber:
    def __init__(self, *args):
        self.var = args

    def findingPerfectNum(self):
        a = self.var[0]
        b = self.var[1]
        c = self.var[2]

        df = open("result.txt", "w")


        sum = 0
        for i in range(1, a):
            if a % i == 0:
                sum += i
        if (sum == a):
            st = (str(a) + " is perfect num ")
            df.write(st + "\n")
        else:
            st = (str(a) + " is not perfect num ")
            df.write(st + "\n")



        sum2 = 0
        for k in range(1, b):
            if b % k == 0:
                sum2 += k
        if (sum2 == b):
            st2 = (str(b) + " is perfect num ")
            df.write(st2 + "\n")
        else:
            st2 = (str(b) + " is not perfect num ")
            df.write(st2 + "\n")



        sum3 = 0
        for g in range(1, c):
            if c % g == 0:
                sum3 += g
        if (sum3 == c):
            st3 = (str(c) + " is perfect num ")
            df.write(st3 + "\n")
        else:
            st3 = (str(c) + " is not perfect num ")
            df.write(st3 + "\n")





        df.close()


def main():
    print ("Enter three numbers i will tell which one is a perfect number")
    firstUserIn = (raw_input("Enter first number"))
    secondNum = (raw_input("Enter second num"))
    thirdNum = (raw_input("Enter third number"))

    df = open("userInput.txt", "w")
    df.write(firstUserIn + "\n")
    df.write(secondNum + "\n")
    df.write(thirdNum + "\n")
    df.close()

    obj = PerfectNumber( int (firstUserIn), int(secondNum), int(thirdNum))
    obj.findingPerfectNum()




if __name__ == "__main__": main()