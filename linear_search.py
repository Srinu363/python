a=[1,5,63,7,8,9,2,5,6,1,]
b=547
for i in range(len(a)):
    if a[i]==b:
        print("element present at index",a[i])
        break
else:
    print("not found ")
        