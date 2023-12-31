class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_value):
        self.__x = new_value
    
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_value):
        self.__y = new_value  

point = Point(5, 10)

print(point.x)  # 5
point.x = 4
print(point.x)  # 4
print(point.y)  # 10