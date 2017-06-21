from numpy import add, subtract, dot, cross, random, divide, equal
from numpy import linalg as LA


class Point(object):
    """
    Class Point Represents an N-Dimension point as 'N' length Vector/List
    By Default Assumed as 2D
    """

    coordinates = None
    N = None
    radius = None

    def __init__(self, n=2, radius=1):
        if n < 2 or int(n) != n:
            raise ValueError(ArithmeticError, "Dimension of point is invalid")
        else:
            self.coordinates = random.randn(n)
            norm = LA.norm(self.coordinates)
            self.coordinates = divide(self.coordinates, norm / radius)
            self.N = n
            self.radius = radius

    def __str__(self):
        return str(self.coordinates)

    def __add__(self, other):
        self.error_check(other)
        return add(self.coordinates, other.coordinates)

    def __sub__(self, other):
        self.error_check(other)
        return subtract(self.coordinates, other.coordinates)

    def __mul__(self, other):
        self.error_check(other)
        return dot(self.coordinates, other.coordinates)

    def __pow__(self, other, modulo=None):
        """
        :param other:
        :return : Cross product of two points in 'N' Dimensions
        """
        self.error_check(other)
        return cross(self.coordinates, other.coordinates)

    def __eq__(self, other):
        self.error_check(other)
        return equal(self.coordinates, other.coordinates)

    def distance(self, other, order=2):
        """
        :param other
        :param order: what sort distance to find. It can be Euclidean (x*x)^(1/2) or other (abs(x)^n)^(1/n)
        :return Corresponding distance between them
        """
        self.error_check(other)
        return LA.norm(self.coordinates - other.coordinates, order)

    def error_check(self, other):
        if self.N != other.N:
            raise ValueError(ArithmeticError, "Dimensions should match")
        elif type(self) is not type(other):
            raise ValueError(TypeError, "Type Doesn't Matches. other is" + str(type(other)))

            # def origin(self):
            #     """
            #     :return: Position of the origin in n-dimensions
            #     """
            #     new_point = Point(self.N, self.radius)
            #     new_point.coordinates = zeros((self.N, 1))
            #     return new_point
