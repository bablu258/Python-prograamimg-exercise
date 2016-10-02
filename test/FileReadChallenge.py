def showEntireFile():
    rd = open("assignmentFile.txt", "r+")
    print (rd.read())
    rd.close()

def appendingOnTheFile():
    rd = open("appendFile.txt", "a")
    st = raw_input("Enter what you want to add")
    rd.write(st)
    rd.close()
    rd1 = open("appendFile.txt", "r")
    print (rd1.read())
    rd1.close()

def deleteContentsFromTheFile ():
    infile = open('philosophers.txt', 'r+')
    print ("Before deletion")
    keepGoing = True

    #while (keepGoing == True):
    print (infile.read())
    infile.close()
    userIn= int(raw_input("how many char you want to save after deletion"))
    infil = open('philosophers.txt', 'r+')
    infil.truncate(userIn)
    print ("After deletion")
    print (infil.read())
    infil.close()


def main ():
    keepGoing = True

    while (keepGoing == True):

        userInput = int(raw_input("Enter 1 for read whole file, 2 for appending to the existing file"
                                  " 3 for delete some portion of the file or 4 for exit"))
        if (userInput == 1):
            print ("showing the contents of entire file")
            showEntireFile()
        if (userInput == 2):
            appendingOnTheFile()
        if (userInput == 3):
            deleteContentsFromTheFile()
        if (userInput == 4):
            keepGoing = False

if __name__=="__main__":main()