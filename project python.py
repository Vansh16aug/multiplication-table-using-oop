class tables:
    def tables (self,nvalue):
        for x in range(2, nvalue + 1):
            print("\n","TABLE OF ",x,"\n")
            for y in range(1, 11):
                 print(x,"x",y,"=",x*y)
nvalue=int(input("enter:"))
f=tables()
f.tables(nvalue)