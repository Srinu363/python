from abc import abstractmethod

class shape:
    @abstractmethod
    def area(self):
        self.width=int(input("enter the width:"))
        self.height=int(input("enter the height:"))
        self.total=self.width*self.height
class Rectangle(shape):
    def area(self):
        super().area()
        return self.total
rectangle=Rectangle()
rectangle.area()
print("total area is:",rectangle.total)
