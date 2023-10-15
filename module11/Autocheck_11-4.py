class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) in (int, float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) in (int, float):
            self.__y = y


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise ValueError

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y


if __name__ == '__main__':
    vector = Vector(Point(1, 10))

    print(vector.coordinates.x)  # 1
    print(vector.coordinates.y)  # 10

    vector[0] = 10  # Встановлюємо координату x вектора 10

    print(vector[0])  # 10
    print(vector[1])  # 10


# class ListedValuesDict:
#     def __init__(self):
#         self.data = {}

#     def __setitem__(self, key, value):
#         if key in self.data:
#             self.data[key].append(value)
#         else:
#             self.data[key] = [value]

#     def __getitem__(self, key):
#         result = str(self.data[key][0])
#         for value in self.data[key][1:]:
#             result += ", " + str(value)
#         return result

# l_dict = ListedValuesDict()
# l_dict[1] = 'a'
# l_dict[1] = 'b'
# print(l_dict[1])  # a, b
