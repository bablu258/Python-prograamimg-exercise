def main():
    mary = '19850103	 -106	 -244	    9999'
    lis = (mary.split())
    print (lis)
    bo = True

    if "-9999" not in lis:
        print " it is not present"
        st = lis[0]
        print st[0:4]

    else:
        print "present"



if __name__== "__main__" :main()