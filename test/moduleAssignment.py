import random

def solutionOne ():
   print( random.uniform(10, 100) )

def solutionTwo():
    print(random.uniform(5, 95))

def solutionThree() :
    print(random.randrange(0, 11, 2))

def solutionFour():
    listMaking =[]
    for i in range(11):
        listMaking.append(random.randint(0,11))
    print (listMaking)
    M = [x for x in listMaking if x % 5 == 0 and x % 7 == 0]
    print (M)

def solutionFive():
    listMaking = []
    for i in range(101):
        listMaking.append(random.randint(100, 201))
    print (listMaking)

def solutionSix():
    listMaking = []
    fiveEvenLi = []
    count = int(0)
    for i in range(101):
        listMaking.append(random.randint(100, 201))
    print ("Random generated numbers from 100 to 200: ")
    print (listMaking)
    evenNum = list(filter(lambda y: (y % 2) == 0, listMaking))
    print ("All even numbers of the above list")
    print (evenNum)
    for k in range (len(evenNum)):
        if (count < 5):
         fiveEvenLi.append(evenNum[k])
         count = count + 1
    print ("Five even number of the above list")
    print (fiveEvenLi)


def solutionSeven():
    listMaking = []
    fiveEvenLi = []
    count = int(0)
    for i in range(1001):
        listMaking.append(random.randint(1, 1001))
    print ("Random generated numbers from 1 to 1001: ")
    print (listMaking)
    evenNum = list(filter(lambda y: (y % 5) == 0 and (y % 7) == 0, listMaking))
    print ("All numbers divisible by 5 and 7")
    print (evenNum)
    for k in range(len(evenNum)):
        if (count < 5):
            fiveEvenLi.append(evenNum[k])
            count = count + 1
    print ("Five even numbers divisible by 5 and 7")
    print (fiveEvenLi)




def solutionEight():
    print(random.randint(7, 15))

def solutionNine():
    mklist = [3,6,7,8]
    random.shuffle(mklist)
    print (mklist)

def solutionTen():
    mklist = [3,6,7,8,10,4,5]
    random.shuffle(mklist)
    print (mklist)

def solutionEleven():
    givenList = [5,6,77,45,22,12,24]
    listWithOutEvenNum = list(filter(lambda y: (y % 2) != 0 , givenList))
    print (listWithOutEvenNum)

def solutionTwelve():
    givenList = [1,2,24,12,35,88,70,97,155]
    newLis = [x for x in givenList if x % 5 == 0 and x % 7 == 0]
    print (newLis)

def solutionTherteen():
    givenList = [12,24,35,70,88,120,153]
    print givenList
    newList = [x for (i,x) in enumerate(givenList) if i%2!=0]
    # newList = [x for x in range(len(givenList)) for j in givenList if  x%2!=0 ]
    # print (newList)
    # learn how to deal with double loop in list comprehenshion

def solutionFourteen():
    arr = [[[0 for col in range(8)] for col in range(5)] for row in range(3)]
    print (arr)

def solutionFifteen():
    givenList = [12,24,35,24,88,120,155]
    print givenList
    newList = [x for (i, x) in enumerate(givenList) if i not in (0,4,5)]
    print (newList)

def solutionSixteen():
    givenList = [12,24,35,24,88,120,155]
    print givenList
    newList = [x for x in givenList if x != 24]
    print (newList)

def solutionSeventeen():
    givenList = [12,24,35,88,120,155,89,155,55]
    newLi= []
    print (givenList)
    for i in givenList:
        if (i not in newLi):
            newLi.append(i)

    print (newLi)






def main():
 # solutionOne()
 # solutionTwo()
 # solutionThree()
 # solutionFour()
 # solutionFive()
 # solutionSix()
 # solutionSeven()
 # solutionEight()
 # solutionNine()
 # solutionTen()
 # solutionEleven()
 # solutionTwelve()
 # solutionTherteen()
 # solutionFourteen()
 #  solutionFifteen()
 #  solutionSixteen()
 solutionSeventeen()







if __name__== "__main__" :main()