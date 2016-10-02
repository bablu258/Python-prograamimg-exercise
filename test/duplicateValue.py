def main():
 myli= [2,25,4,2,9,2,3,2,4,25]
 newli = []
 result = []

 for i in range(len(myli)):
     for j in range(len(myli)):
         if (myli[i] == myli[j]):
             if(i != j):
                 newli.append(myli[i])

 for x in newli:
     if x  not in result:
         result.append(x)

 print (result)

if __name__== "__main__" :main()