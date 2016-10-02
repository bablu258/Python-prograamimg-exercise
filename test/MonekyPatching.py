
class Addition():
    def add (self, x, y):
        return x + y

def malt(self, x, y):
    return x * y


def main():
    print ("Enter two numbers to view the Monkey patching")
    fnum = int(raw_input("Enter first number"))
    snum = int (raw_input("Enter second number"))

    # class implementation
    obj1 = Addition()
    basicAdd= obj1.add(fnum,snum)
    print ("*****Printing the output from Addition class******")
    print (basicAdd)

    # monkey patching impplementation
    Addition.add = malt
    monkey = obj1.add(fnum,snum)
    print ("*****Printing the output from monkey patching method ******")
    print (monkey)


if __name__== "__main__" :main()