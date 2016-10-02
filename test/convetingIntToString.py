
def convetor(num, word):
    # number 1 solution
    print("*********converting interger to a string**********")
    print("Data type before conversion")
    print (type(num))
    print("Data type after conversion")
    mo = str(num)
    print (type(mo))

    # number 2 solution
    print("*********converting string to integer**********")
    print("Data type before conversion")
    print (type(word))
    print("Data type after conversion")
    modified = int(word)
    print (type(modified))

def numberThree(strOne, strTwo):

    one = int(strOne)
    two = int(strTwo)
    add = one + two
    print ('Total of two numbers :'),
    print(add)

def numberFour(firstName, lastName):
    concate = firstName + ' ' +lastName
    print (concate)

def numberFive(oneWord, secondWord2):
    firstlen = len(oneWord)
    secondlen = len(secondWord2)
    if (firstlen > secondlen):
        print ("Maximum lenth belongs to "),
        print (oneWord),
        print (" and it lenght is "),
        print (firstlen)
    elif (firstlen < secondlen):
        print ("Maximum lenth belongs to "),
        print (secondWord2),
        print (" and it lenght is "),
        print (secondlen)
    else:
        print ("Length for both String "),
        print (oneWord + " and " + secondWord2),
        print (" is same.")

def numberSix (munber2):
    if (munber2%2)== 0:
        print (munber2 ),
        print (" is even number")
    else:
        print (munber2),
        print (" is odd number")








def main():


    num =int( raw_input("Enter a integer number and the converter will make it a string"))
    word = raw_input("Enter a integral numbers in string and the converter will make it an integer")
    convetor(num, word, )

    # number 3 solution
    strOne= raw_input("Enter first integral numbers in string: ")
    strTwo = raw_input("Enter second integral numbers in string: ")
    numberThree(strOne,strTwo)

    # number 4 solution
    firstName = raw_input("Enter your first name: ")
    lastName = raw_input("Enter your second name: ")
    numberFour(firstName,lastName)

    #solution for number 5
    oneWord= raw_input("Enter first word")
    secondWord2= raw_input("Enter second word")
    numberFive(oneWord,secondWord2)

    #solution for number 6
    munber2 = int (raw_input(" Enter a number to verify if it is a even or odd number"))
    numberSix(munber2)





if __name__== "__main__" :main()
