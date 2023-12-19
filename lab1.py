from abc import ABC, abstractmethod


class BaseAbstractSuperClass(ABC):
    def __init__(self):
        super(BaseAbstractSuperClass, self).__init__()

    @abstractmethod
    def volume(self):
        pass


class BaseInterface:
    @abstractmethod
    def create_object(self):
        pass


class Cube(BaseAbstractSuperClass, BaseInterface):

    def create_object(self):
        print("The object is created")


    def __init__(self, height, width, length):
        super().__init__()
        self.__height = height
        self.__width = width
        self.__length = length
        self.create_object()

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def length(self):
        return self.__length

    @height.setter
    def height(self, hg):
        if hg > 0:
            self.__height = hg
        else:
            raise ValueError

    @width.setter
    def width(self, wd):
        if wd > 0:
            self.__width = wd
        else:
            raise ValueError

    @length.setter
    def length(self, ln):
        if ln > 0:
            self.__length = ln
        else:
            raise ValueError

    def volume(self):
        return f"The volume of Cube is: {self.height * self.width * self.length}"






class Parallelogram(BaseAbstractSuperClass, BaseInterface):

    def create_object(self):
        print("The object is created")

    def __init__(self, width, length, height):
        super().__init__()
        self.__width = width
        self.__length = length
        self.height = height
        self.create_object()



    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def length(self):
        return self.__length

    @height.setter
    def height(self, hg):
        if hg > 0:
            self.__height = hg
        else:
            raise ValueError

    @width.setter
    def width(self, wd):
        if wd > 0:
            self.__width = wd
        else:
            raise ValueError

    @length.setter
    def length(self, ln):
        if ln > 0:
            self.__length = ln
        else:
            raise ValueError

    def volume(self):
        return f"The volume of Parallelogram: {self.width * self.length * self.height}"






class Pyramid(BaseAbstractSuperClass, BaseInterface):

    def create_object(self):
        print("The object is created")

    def __init__(self, width, height, length):
        super().__init__()
        self.__width = width
        self.__length = length
        self.height = height
        self.create_object()

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def length(self):
        return self.__length

    @height.setter
    def height(self, hg):
        if hg > 0:
            self.__height = hg
        else:
            raise ValueError

    @width.setter
    def width(self, wd):
        if wd > 0:
            self.__width = wd
        else:
            raise ValueError

    @length.setter
    def length(self, ln):
        if ln > 0:
            self.__length = ln
        else:
            raise ValueError

    def volume(self):
        return f"The volume of Pyramid: {(self.width * self.height) * self.height / 3}"



cube = Cube(1, 2, 3)
print(cube.volume())

parallelogram = Parallelogram(4, 5, 6)
print(parallelogram.volume())

pyramid = Pyramid(7, 8, 9)
print(pyramid.volume())
