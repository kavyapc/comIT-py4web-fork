

class Point:
    
    # constructor
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        
    # operator(s) overloading
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(f"{self.name}+{other.name}", self.x + other.x, self.y + other.y)
        return self
    
    def __mul__(self, number):
        if number == 0:
            return Point("Origin", 0 ,0)
        return Point(f"{self.name}-displaced", self.x * number, self.y * number)
    
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
        
        
        
    # CLI representions    
    def __str__(self):
        return f"{self.name}({self.x}, {self.y})"
    
    def __repr__(self):
        return f"{self.name}(x={self.x}, y={self.y})"
    
p1 = Point("P1", 2, 8)
p2  = Point("P2", 44, 28)
p3 = Point("P3", 65, 81)
p4 = Point("P4", 44, 28)
print(p1, p2)    
print(p1 + p2 + p3*3)  
print("p2 is equal to p4:", p2 == p4)
print("p2 is equal to p3:", p2 == p3)


trail = [p1, p2, p3]
print(trail)
