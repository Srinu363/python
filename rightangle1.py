def rightangle1(rows):
    for i in range(rows):
        print(" " * (rows-i) + "*" * i)
rows=int(input("enter the number"))
rightangle1(rows)