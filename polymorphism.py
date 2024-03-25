class a:
    def met(self):
        print("this is class a")
class b:
    def met(self):
        print("this is class b")
class c:
    def met(self):
        print("this is class c")
def poly(d):
    d.met()
    
obj1=a()
obj2=b()
obj3=c()

poly(obj1)
poly(obj2)
poly(obj3)