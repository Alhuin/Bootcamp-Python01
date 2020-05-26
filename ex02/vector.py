class InitVectorError(Exception):
    pass


class ForbiddenOperation(Exception):
    def __init__(self, operation):
        self.message = f"Forbidden Operation: Tried to {operation}."

    pass


def isnum(obj):
    return type(obj) == int or type(obj) == float


class Vector:
    def __init__(self, arg):
        if type(arg) == int:
            self.values = [round(float(i), 1) for i in range(0, arg)]
            self.size = arg
        elif type(arg) == tuple:
            self.values = [round(float(i), 1) for i in range(arg[0], arg[1])]
            self.size = arg[1] - arg[0]
        elif type(arg) == list:
            self.values = [round(float(i), 1) for i in arg]
            self.size = len(arg)
        else:
            raise InitVectorError

    def __add__(self, other):
        """ Addition between 2 vectors """
        if isnum(other):
            if self.size == 1:    # cannot add scalar to vector
                other = Vector([other])
            else:
                raise ForbiddenOperation("add a vector to a scalar.")
        if self.size == other.size:
            return Vector([self.values[i] + other.values[i]
                           for i in range(self.size)])
        else:
            raise ForbiddenOperation("add 2 vectors of diffrent sizes")

    def __radd__(self, other):
        if isnum(other):    # cannot add vector to scalar
            other = Vector([other])
        return other + self

    def __sub__(self, other):
        """ Substraction between 2 vectors """
        if isnum(other):
            if self.size == 1:    # cannot sub scalar to vector
                other = Vector([other])
            else:
                raise ForbiddenOperation("sub a scalar to a vector")
        if self.size == other.size:
            return Vector([self.values[i] - other.values[i]
                           for i in range(self.size)])
        else:
            raise ForbiddenOperation("sub two vectors of different sizes")

    def __rsub__(self, other):
        if isnum(other):    # cannot sub vector to scalar
            other = Vector([other])
        return other - self

    def __truediv__(self, other):
        try:
            if isnum(other):
                return Vector(
                    [self.values[i] / other for i in range(self.size)]
                )
            elif isnum(self) and isinstance(other, Vector):
                return Vector(
                    [self / other.values[i] for i in range(other.size)]
                )
        except ZeroDivisionError:
            raise ForbiddenOperation("divide by 0.")

    def __rtruediv__(self, other):
        if isinstance(other, Vector):
            return other / self
        else:
            raise ForbiddenOperation("divide a scalar by a vector.")

    def __mul__(self, other):
        if isnum(other):
            return Vector(
                [self.values[i] * other for i in range(self.size)]
            )
        elif isinstance(other, Vector):
            if other.size == self.size:
                sum_of_products = 0
                products = [self.values[i] * other.values[i]
                            for i in range(self.size)]
                for product in products:
                    sum_of_products += product
                return sum_of_products
            else:
                raise ForbiddenOperation("mult vectors of diferrent sizes.")

    def __rmul__(self, other):
        if isnum(other):
            return self * other
        elif isinstance(other, Vector):
            return other * self

    def __str__(self):
        return f"{self.values}"

    def __repr__(self):
        return f"Values: {self.values}\nSize: {self.size}"
