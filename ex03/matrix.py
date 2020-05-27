import sys
import os

try:
    from ex02.vector import Vector
except ModuleNotFoundError:
    sys.path.append(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))
    )
    sys.path.append(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    ) + "/ex02")
    from ex02.vector import Vector


class InitMatrixError(Exception):
    def __init__(self, message):
        self.message = message
        # print(message)
    pass


class ForbiddenOperation(Exception):
    def __init__(self, operation):
        self.message = f"Forbidden Operation: {operation}."

    pass


def isnum(obj):
    return type(obj) == int or type(obj) == float


def is_rect_2d_num_list(lst):
    row_len = len(lst[0])
    for el in lst:
        if not isinstance(el, list)\
                or not all(isnum(n) for n in el)\
                or len(el) != row_len:
            return False
    return True


class Matrix:
    def __init__(self, arg, tup=None):
        self.data: list
        self.shape: tuple

        if type(arg) == list and tup is None:
            # Matrix([[], []])
            if not is_rect_2d_num_list(arg):
                raise InitMatrixError("Wrong list type.")
            self.shape = (len(arg), len(arg[0]))
            self.data = [
                [
                    float(arg[i][j])
                    for j in range(self.shape[1])
                ]
                for i in range(self.shape[0])
            ]
        elif type(arg) == tuple:
            # Matrix(2, 1)
            if len(arg) != 2:
                raise InitMatrixError("Wrong tuple size.")
            elif all(isinstance(n, int) for n in arg):
                self.data = [[0.0 for x in range(arg[1])]
                             for y in range(arg[0])]
                self.shape = arg
        elif type(arg) == list and tup is not None \
                and len(tup) == 2 and all(isinstance(n, int) for n in tup):
            # Matrix([[], []], (2, 1))
            if is_rect_2d_num_list(arg):
                if len(arg) == tup[0] and len(arg[1]) == tup[1]:
                    self.shape = (tup[0], tup[1])
                    self.data = [
                        [
                            float(arg[i][j])
                            for j in range(self.shape[1])
                        ]
                        for i in range(self.shape[0])
                    ]
                else:
                    raise InitMatrixError("Matrix shape diff from tuple.")
            else:
                raise InitMatrixError("Wrong list type.")
        else:
            raise InitMatrixError("Wrong data type.")

    def __add__(self, other):
        """ Add a Matrix """
        if isinstance(other, Matrix):
            if self.shape == other.shape:
                new = Matrix(self.shape)
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        new.data[i][j] = self.data[i][j] + other.data[i][j]
                return new
            raise ForbiddenOperation("Can't add Matrices of different shapes")
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Matrix):
            return self + other
        return NotImplemented

    def __sub__(self, other):
        """ Substract a Matrix """
        if isinstance(other, Matrix):
            if self.shape == other.shape:
                return Matrix([
                    [
                        self.data[i][j] - other.data[i][j]
                        for j in range(self.shape[1])
                    ]
                    for i in range(self.shape[0])
                ])
            raise ForbiddenOperation("Can't sub Matrices of different shapes")
        return NotImplemented

    def __rsub__(self, other):
        """ Reverse Substraction """
        if isinstance(other, Matrix):
            if self.shape == other.shape:
                return Matrix([
                    [
                        other.data[i][j] - self.data[i][j]
                        for j in range(self.shape[1])
                    ]
                    for i in range(self.shape[0])
                ])
            raise ForbiddenOperation("Can't sub Matrices of different shapes")
        return NotImplemented

    def __truediv__(self, other):
        if isnum(other):
            if other == 0:
                raise ForbiddenOperation("Division by zero.")
            return Matrix([
                [
                    self.data[i][j] / other
                    for j in range(self.shape[1])
                ]
                for i in range(self.shape[0])
            ])
        return NotImplemented

    def __rtruediv__(self, other):
        return NotImplemented

    def __mul__(self, other):
        if isnum(other):
            return Matrix([
                [
                    self.data[i][j] * other
                    for j in range(self.shape[1])
                ]
                for i in range(self.shape[0])
            ])
        elif isinstance(other, Vector):
            if self.shape[0] == other.size:
                new = Vector(other.size)
                # iterate through rows of self
                for i in range(self.shape[0]):
                    sum_of_products = 0
                    for j in range(self.shape[1]):
                        sum_of_products += self.data[i][j] * other.values[j]
                    new.values[i] = sum_of_products
                return new
            raise ForbiddenOperation("Can't multiply matrix by vector: "
                                     "vector's size is not matrix height")
        elif isinstance(other, Matrix):
            if other.shape == self.shape:
                new = Matrix(self.shape)
                # iterate through rows of self
                for i in range(self.shape[0]):
                    # iterate through columns of other
                    for j in range(self.shape[1]):
                        # iterate through rows of other
                        for k in range(other.shape[1]):
                            new.data[i][j] += self.data[i][k]\
                                              * other.data[k][j]
                return new
            else:
                raise ForbiddenOperation("Can't multiply matrices of "
                                         "different shapes")
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isnum(other)\
                or isinstance(other, Matrix)\
                or isinstance(other, Vector):
            return self * other
        return NotImplemented

    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return f"Data: {self.values}\nShape: {self.tuple}"
