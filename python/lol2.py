def m(n):
    if(n==0):
        return p[0]
    else:
        return p[n]+m(n-1)
       
P=input("enter the numberrs to add")
p=list(map(int,P.split(" ")))
n=len(p)
n=n-1
s=m(n)
print(s)
