from shutil import copyfile


def writeAndRead():
    fd = open("solution.txt", "w")
    st = " i am writing "
    fd.write(st)
    fd.close()
    rd = open("solution.txt", "r+")
    print (rd.read())
    rd.close()

def writeMultipleLinesAndCopypaste():
    fd = open("mal.txt", "w")
    st = ("1.	Generate a random float where the value is between 10 and 100 \n"
          "2.	Generate a random float where the value is between 5 and 95 \n"
          "3.	Write a program to output a random even number between 0 and 10 inclusive using random module and list compression \n"
          "4.	Write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.\n")
    fd.write(st)
    fd.close()
    rd = open("mal.txt", "r+")
    print("mal.txt")
    print (rd.read())
    ne =  open("new.txt", "w")
    copyfile("mal.txt", "new.txt")
    ne.close()
    jk = open("new.txt", "r+")
    print("new.txt")
    print (jk.read())
    jk.close()
    rd.close()


def copyUsingSUdDO():
    fd = open("mal.txt", "w")
    st = ("1.	Generate a random float where the value is between 10 and 100 \n"
          "2.	Generate a random float where the value is between 5 and 95 \n"
          "3.	Write a program to output a random even number between 0 and 10 inclusive using random module and list compression \n"
          "4.	Write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.\n")
    fd.write(st)
    fd.close()
    rd = open("mal.txt", "r+")
    print("mal.txt")
    print (rd.read())
    ne = open("new.txt", "w+")
    for i in rd:
        ne.write(i)
        # code has problems

    ne.close()
    jk = open("new.txt", "r+")
    print("new.txt")
    print (jk.read())
    jk.close()
    rd.close()










def main():

# write and read
#  writeAndRead()
# writing multiple lines
#  writeMultipleLinesAndCopypaste()
 copyUsingSUdDO()





if __name__== "__main__" :main()