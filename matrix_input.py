a=int(input("entert the number of rows"))
b=int(input("enter teh number of columns"))
c=[]
for i in range(a):
    d=[]
    for j in range(b):
        ele=int(input("enter the numbers "))
        d.append(ele)
    c.append(d)
print(c)