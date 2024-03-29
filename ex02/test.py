import unittest

from vector import Vector, ForbiddenOperation


class TestVector(unittest.TestCase):

    # initiation

    def setUp(self):
        self.v = Vector(5)
        self.v1 = Vector((10, 15))
        self.v2 = Vector([0.3, 0.5, 0.8])

    def test_vector_init_from_int(self):
        self.assertListEqual(self.v.values, [0.0, 1.0, 2.0, 3.0, 4.0])
        self.assertEqual(self.v.size, 5)

    def test_vector_init_from_range(self):
        self.assertListEqual(self.v1.values, [10, 11, 12, 13, 14])
        self.assertEqual(self.v1.size, 5)

    def test_vector_init_from_list(self):
        self.assertListEqual(self.v2.values, [0.3, 0.5, 0.8])
        self.assertEqual(self.v2.size, 3)

    # Valid operations

    def test_add_vector(self):
        v3 = self.v + self.v1
        self.assertListEqual(v3.values, [10.0, 12.0, 14.0, 16.0, 18.0])
        self.assertEqual(v3.size, 5)

    def test_sub_vector(self):
        v3 = self.v - self.v1
        self.assertListEqual(v3.values, [-10, -10, -10, -10, -10])
        self.assertEqual(v3.size, 5)

    def test_truediv(self):
        with self.assertRaises(ForbiddenOperation):
            v3 = self.v1 / 0
        v3 = self.v1 / 2
        self.assertListEqual(v3.values, [5.0, 5.5, 6.0, 6.5, 7.0])
        self.assertEqual(v3.size, 5)

    def test_mul_vector(self):
        v3 = self.v * self.v1
        self.assertEqual(v3, 130)

    def test_mul_scalar(self):
        v3 = self.v * 2.5
        self.assertListEqual(v3.values, [0.0, 2.5, 5.0, 7.5, 10.0])
        self.assertEqual(v3.size, 5)

    def test_rmul(self):
        v3 = 2.5 * self.v
        self.assertListEqual(v3.values, [0.0, 2.5, 5.0, 7.5, 10.0])
        self.assertEqual(v3.size, 5)

    # Forbidden operations & TypeErrors

    def test_add_different_size_vectors(self):
        with self.assertRaises(ForbiddenOperation):
            v3 = self.v2 + self.v

    def test_add_scalar(self):
        with self.assertRaises(TypeError):
            v3 = self.v2 + 1

    def test_add_wrong_type(self):
        with self.assertRaises(TypeError):
            v3 = self.v2 + (5, 2)

    def test_radd_scalar(self):
        with self.assertRaises(TypeError):
            v3 = 3 + self.v2

    def test_radd_wrong_type(self):
        with self.assertRaises(TypeError):
            v3 = (5, 12) + self.v2

    def test_sub_different_size_vectors(self):
        with self.assertRaises(ForbiddenOperation):
            v3 = self.v2 - self.v

    def test_sub_scalar(self):
        with self.assertRaises(TypeError):
            v3 = self.v2 - 1

    def test_sub_wrong_type(self):
        with self.assertRaises(TypeError):
            v3 = self.v2 - (5, 2)

    def test_rsub_scalar(self):
        with self.assertRaises(TypeError):
            v3 = 3 - self.v2

    def test_rsub_wrong_type(self):
        with self.assertRaises(TypeError):
            v3 = (5, 12) - self.v2


if __name__ == "__main__":
    unittest.main()
