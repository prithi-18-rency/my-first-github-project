def integer(n,m):
    for i in range(n,m+1):
        if i%2!=0 and i%3!=0:
              print(i,end=",")
      
n=int(input("n:" ))
m=int(input("m:" ))
integer(n,m)
