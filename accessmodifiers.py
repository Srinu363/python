#they heve three types
#public: it access outside the class also.
#protected:it means attributrs and methods are accessble for derived class
#private:it means can't access any methods and attributesderved class
class student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"hello my name is {self.name}")
s1=student("srinu")
print(s1.name)
s1.display()
##private code
class hello:
    age=10
    _subject="python"
    def __init__(self,name,rollno):
        self.name=name#public
        self._rollno=rollno#private
    print(age)
    print(_subject)
class branch(hello):
    pass
s1=branch("srinu",20)
print(s1.name)
print(s1._rollno)