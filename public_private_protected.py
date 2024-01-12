class hello:
    name="srinu"
    _age=20
    #__subject="python"
class display(hello):
    pass
s1=display()
print(s1.name)
print(s1._age)
#print(s1.__subject)#this __subject attribute cant acceble for other derived class
print(dir(s1))
    