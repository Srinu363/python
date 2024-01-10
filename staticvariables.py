class car:
    whells=4 #class variables or static variables
    def __init__(self):
        self.name="volvo"
        self.mil=10
c1=car()
print(c1.name,c1.mil)
c1.name="BMW"
print(c1.name,c1.mil,c1.whells)
car.whells=4
print(c1.name,c1.mil,c1.whells)