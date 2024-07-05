class fruit:
    def __init__(a,color,name,no):
        a.col=color
        a.nam=name
        a.no=no
        
    def fun(a):
        print("the funtions parameter is -",a.col)
     
        

f=fruit("red","orange",2)
f.fun()
print("fruit-",f.nam)
print("color-",f.col)
print("number-",f.no)
print(f)
