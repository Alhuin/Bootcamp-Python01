class InitVectorError(Exception):
    def __init__(self):
        self.message = f"Init Vector error: Wrong type sent to init method."


class ForbiddenOperation(Exception):
    def __init__(self, operation):
        self.message = f'Forbidden Operation: Tried to {operation}.'


def isnum(obj):
    return type(obj) == int or type(obj) == float


class Vector:
    def __init__(self, arg):
        if type(arg) == int:
            self.values = [round(float(i), 1) for i in range(0, arg)]
            self.size = arg
        elif type(arg) == tuple and len(arg) == 2:
            if not all(isinstance(a, int) for a in arg):
                raise InitVectorError
            self.values = [round(float(i), 1) for i in range(arg[0], arg[1])]
            self.size = arg[1] - arg[0]
        elif type(arg) == list:
            if not all(isinstance(a, int) or isinstance(a, float)
                       for a in arg):
                raise InitVectorError
            self.values = [round(float(i), 1) for i in arg]
            self.size = len(arg)
        else:
            raise InitVectorError

    def __add__(self, other):
        """ Addition between 2 vectors """
        if isinstance(other, Vector):
            if self.size == other.size:
                return Vector([self.values[i] + other.values[i]
                               for i in range(self.size)])
            raise ForbiddenOperation("add 2 vectors of diffrent sizes")
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Vector):
            return self + other
        return NotImplemented

    def __sub__(self, other):
        """ Substraction between 2 vectors """
        if isinstance(other, Vector):
            if self.size == other.size:
                return Vector([self.values[i] - other.values[i]
                               for i in range(self.size)])
            raise ForbiddenOperation("sub two vectors of different sizes")
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, Vector):
            if self.size == other.size:
                return Vector([other.values[i] - self.values[i]
                               for i in range(self.size)])
            raise ForbiddenOperation("sub two vectors of different sizes")
        return NotImplemented

    def __truediv__(self, other):
        if isnum(other):
            if other == 0:
                raise ForbiddenOperation("divide by 0")
            return Vector([value / other for value in self.values])
        return NotImplemented

    def __rtruediv__(self, other):
        return NotImplemented

    def __mul__(self, other):
        if isnum(other):    # return a vector
            return Vector(
                [self.values[i] * other for i in range(self.size)]
            )
        elif isinstance(other, Vector):     # return a scalar
            if other.size == self.size:
                sum_of_products = 0
                products = [self.values[i] * other.values[i]
                            for i in range(self.size)]
                for product in products:
                    sum_of_products += product
                return sum_of_products
            else:
                raise ForbiddenOperation("mult vectors of diferrent sizes.")
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isnum(other) or isinstance(other, Vector):
            return self * other
        return NotImplemented

    def __str__(self):
        return f"{self.values}"

    def __repr__(self):
        return f"Values: {self.values}\nSize: {self.size}"
