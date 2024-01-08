class hello:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        print(name,roll)
    def details(self):
        print("this is my name",self.name,self.roll)
a=hello("srinu",8)
a1=hello("srinu",9)
a.details()