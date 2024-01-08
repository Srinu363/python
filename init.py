class hello:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def details(self):
        print("this is my name",self.name,self.roll)
a=hello("srinu",8)
a.details()