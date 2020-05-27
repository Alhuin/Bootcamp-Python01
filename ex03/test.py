import unittest
import sys
import os

try:
    from ex02.vector import Vector
    from matrix import Matrix, InitMatrixError, ForbiddenOperation
except ModuleNotFoundError:
    sys.path.append(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__)))
    )
    sys.path.append(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))) + "/ex02")
    from ex02.vector import Vector
    from matrix import Matrix, InitMatrixError, ForbiddenOperation


class TestMatrixInit(unittest.TestCase):

    # Good Init
    def setUp(self):
        self.m = Matrix([
            [1.0, 2.0, 3.5, 4.0, 5.0],
            [0.1, 0.2, 0.3, 0.4, 0.5]
        ])
        self.m1 = Matrix((2, 5))
        self.m2 = Matrix(
            [
                [0.3, 0.5, 0.8],
                [2.5, 3.8, 4.5]],
            (2, 3)
        )

    def test_init_from_list(self):
        self.assertListEqual(
            [[1.0, 2.0, 3.5, 4.0, 5.0], [0.1, 0.2, 0.3, 0.4, 0.5]],
            self.m.data,
        )
        self.assertTupleEqual(self.m.shape, (2, 5))

    def test_init_from_range_tuple(self):
        self.assertListEqual(
            [[0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0]],
            self.m1.data,
        )
        self.assertTupleEqual(self.m1.shape, (2, 5))

    def test_init_from_mixed_tuple(self):
        self.assertListEqual(
            [[0.3, 0.5, 0.8], [2.5, 3.8, 4.5]],
            self.m2.data,
        )
        self.assertTupleEqual(self.m2.shape, (2, 3))

    # Wrong Init

    def test_init_from_wrong_data(self):                # Wrong data type.
        with self.assertRaises(InitMatrixError):
            m3 = Matrix("test")

    def test_init_from_bad_typed_list(self):            # Wrong list type.
        with self.assertRaises(InitMatrixError):
            m3 = Matrix([[0.0, 1.0], [2.0, "test"]])

    def test_init_from_bad_sized_tuple(self):           # Wrong tuple size.
        with self.assertRaises(InitMatrixError):
            m3 = Matrix((1, 2, 3))

    def test_init_matrix_shape_diff_tuple(self):    # Matrix shape diff from
        with self.assertRaises(InitMatrixError):    # tuple.
            m3 = Matrix([[0.3, 0.5, 0.8], [2.5, 3.8, 4.5]], (3, 2))

    def test_init_mixed_bad_typed_list(self):           # Wrong list type.
        with self.assertRaises(InitMatrixError):
            m3 = Matrix([[0.3, 0.5, 0.8], [2.5, "test", 4.5]], (2, 3))

    def test_init_bad_mixed_tuple(self):                # Wrong tuple type.
        with self.assertRaises(InitMatrixError):
            m3 = Matrix([[0.3, 0.5, 0.8], [2.5, 3.2, 4.5]], "test")


class TestMatrixOperations(unittest.TestCase):
    def setUp(self):
        self.m = Matrix([
            [1.0, 2.0],
            [3.0, 4.0]
        ])
        self.m1 = Matrix((2, 5))
        self.m2 = Matrix(
            [
                [5.0, 6.0],
                [7.0, 8.0]
            ],
            (2, 2)
        )
        self.v = Vector([5, 6])

    def test_add_matrix(self):
        m3 = self.m + self.m2
        self.assertListEqual(
            m3.data,
            [[6.0, 8.0], [10.0, 12.0]]
        )
        self.assertTupleEqual(m3.shape, (2, 2))

    def test_radd_matrix(self):
        m3 = self.m.__radd__(self.m2)
        self.assertListEqual(
            m3.data,
            [[6.0, 8.0], [10.0, 12.0]]
        )
        self.assertTupleEqual(m3.shape, (2, 2))

    def test_sub_matrix(self):
        m3 = self.m2 - self.m
        self.assertListEqual(
            m3.data,
            [[4.0, 4.0], [4.0, 4.0]]
        )
        self.assertTupleEqual(m3.shape, (2, 2))

    def test_rsub_matrix(self):
        m3 = self.m.__rsub__(self.m2)
        self.assertListEqual(
            m3.data,
            [[4.0, 4.0], [4.0, 4.0]]
        )
        self.assertTupleEqual(m3.shape, (2, 2))

    def test_mul_scalar(self):
        m3 = self.m * 2
        self.assertListEqual(
            m3.data,
            [[2.0, 4.0], [6.0, 8.0]]
        )
        self.assertTupleEqual(m3.shape, (2, 2))

    def test_mul_matrix(self):
        m3 = self.m * self.m2
        self.assertListEqual(
            m3.data,
            [[19.0, 22.0], [43.0, 50.0]]
        )
        self.assertTupleEqual(m3.shape, (2, 2))

    def test_mul_vector(self):
        m3 = self.m * self.v
        self.assertListEqual(
            m3.values,
            [17.0, 39.0]
        )
        self.assertEqual(m3.size, 2)

    def test_rmul(self):
        m3 = self.m * self.v
        self.assertListEqual(
            m3.values,
            [17.0, 39.0]
        )
        self.assertEqual(m3.size, 2)
        m3 = self.m * self.m2
        self.assertListEqual(
            m3.data,
            [[19.0, 22.0], [43.0, 50.0]]
        )
        self.assertTupleEqual(m3.shape, (2, 2))
        m3 = self.m * 2
        self.assertListEqual(
            m3.data,
            [[2.0, 4.0], [6.0, 8.0]]
        )
        self.assertTupleEqual(m3.shape, (2, 2))

    def test_rtruediv(self):
        m3 = self.m / self.m2
        print(m3)

    # Errors

    def test_add_errors(self):
        with self.assertRaises(ForbiddenOperation):
            self.m + self.m1

    def test_radd_errors(self):
        with self.assertRaises(TypeError):
            self.m + "string"

    def test_sub_errors(self):
        with self.assertRaises(TypeError):
            self.m - "string"
        with self.assertRaises(ForbiddenOperation):
            self.m - self.m1

    def test_rsub_errors(self):
        with self.assertRaises(TypeError):
            self.m + "string"
        with self.assertRaises(ForbiddenOperation):
            self.m - self.m1

    def test_mul_errors(self):
        with self.assertRaises(ForbiddenOperation):
            pass

    def test_rmul_errors(self):
        with self.assertRaises(ForbiddenOperation):
            pass

    def test_truediv_errors(self):
        with self.assertRaises(ForbiddenOperation):
            pass

    def test_rtruediv_errors(self):
        with self.assertRaises(ForbiddenOperation):
            pass


if __name__ == "__main__":
    unittest.main()
