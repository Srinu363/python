a = 2

if a <= 1:
    print("Enter a number greater than one")
else:
    for i in range(2, a):
        if a % i == 0:
            print("not prime")
            break
            
    else:
        print("prime")
