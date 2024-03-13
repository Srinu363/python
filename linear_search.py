a=list(map(int,input("enter the list elements").split()))
b=7
for i in range(len(a)):
    if a[i]==b:
        print("element present at index",i)
        break
else:
    print("not found")
        