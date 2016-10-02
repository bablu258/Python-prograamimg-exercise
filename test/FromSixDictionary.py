def dicFunct(one, two, three):

    dict = {one:(one**one),two:(two**two),three:(three**three)}
    print dict [one] , dict [two], dict [three]

def eightSolution ():
    d = {}
    print("Only value of the dictionary is printing...")
    for num in range(1, 21):
        d[num] = int(num) ** int(num)
        #print d[num],  #sudo code
    print (d.values()) #build_in method

def nineSolution ():
    d = {}
    print("Only key of the dictionary is printing...")
    for num in range(1, 21):
        d[num] = int(num) ** int(num)

    print(d.keys())


def tenSolution():
    li = []
    print(" Printing square value of the lists 1 to 20...")
    for num in range(1, 21):
        li.append(int(num)** int (num))

    print li,


def elevenSolution():
    li = []
    print(" Printing square value of the lists 1 to 5...")
    for num in range(1, 21):
        li.append(int(num)** int (num))

    print(li[0:5])

def tupal12Solution():
    li = []
    print(" Printing tuple square value...")
    for num in range(1, 21):
        li.append(int(num) ** int(num))
    myTuple = tuple(li)
    print myTuple


def solution13():
    myTu = (1,2,3,4,5,6,7,8,9,10)
    print(myTu[0:5])
    print(myTu[5:10])

def solution14():
    myTu = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print("Printing all even numbers from tuple")
    for ele in range(len(myTu)):
        if (myTu[ele]%2)==0 :
            print(myTu[ele]),

def solution15(ele):
       evenNum = lambda ele : ((ele % 2) == 0)
       if (evenNum (ele)== True):
           print ele

def solution16():
    myli = [1,2,3,4,5,6,7,8,9,10]
    print map(lambda x: x ** x, myli)

def solution17():
    myli = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    maLi =  list (map(lambda x: x ** x, myli))
    print maLi
    evenNum = list(filter(lambda y : (y%2)==0 , maLi))
    print evenNum

def solution18():
    a = []
    print ("Priting the list having 1 to 20")
    for x in range(1,21):
        a.append(x)
    print a
    evenNum = filter(lambda x: (x%2) == 0 , a)
    print ("Priting the list having even numbers from 1 to 20")
    print evenNum

def solution19 ():
    a = []
    print ("Priting the list having 1 to 20")
    for x in range(1, 21):
        a.append(x)
    print a
    squareNum = map(lambda x: x ** x , a)
    print ("Priting the list having square numbers from 1 to 20")
    print squareNum

















def main():
    #seven solution
    # one = int (raw_input("Enter one "))
    # two = int(raw_input("Enter two"))
    # three = int(raw_input("Enter three"))
    # dicFunct(one, two, three)

    #eight solution
    #eightSolution()

    #nine solution
    #nineSolution()

    # ten solution
    #tenSolution()

    #eleven solution
    #elevenSolution()


    #12 solution
    # tupal12Solution()

    # 13 solution
    # solution13()

    #14 solution
    # solution14()

    #15 solution
    # myList = [1,2,3,4,5,6,7,8,9,10]
    # filter(solution15, myList)

    # 16 solution
    # solution16()

    #solution 17
    # solution17()

    #solution 18
    #solution18()

    #solution 19
    solution19()
















if __name__== "__main__" :main()


