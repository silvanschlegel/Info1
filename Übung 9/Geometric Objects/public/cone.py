from geometric_object import GeometricObject


class Cone(GeometricObject):

    def __init__(self, radius, vertical_height, slant_height, color, filled):
        GeometricObject.__init__(self, color, filled)
        self.__radius = radius
        self.__vertical_height = vertical_height
        self.__slant_height = slant_height
        self.__PI = 3.14


    def get_radius(self):
        return self.__radius

    def get_vertical_height(self):
        return self.__vertical_height

    def get_slant_height(self):
        return self.__slant_height

    def get_area(self):
        return round(3.14*self.__radius**2 + 3.14*self.__radius*self.__slant_height, 2)

    def get_volume(self):
        return round((1/3)*3.14*self.__radius**2*self.__vertical_height,2)
