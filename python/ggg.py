def lol(l):
    if(l==0):
        return r[0]
    else:
        return r[l]+lol(l-1)
    
 

r=input("enter the string")
r=list(r)
l=len(r)
l=l-1
h=lol(l)
print(h)

