import unittest
from programA import convert


class TestConvertOption(unittest.TestCase):

    def test_hex_conversion(self):
        hex_val, _, _ = convert(255)
        self.assertEqual(hex_val, "FF")

    def test_binary_length_is_16(self):
        _, bin_val, _ = convert(5)
        self.assertEqual(len(bin_val), 16)

    def test_binary_correctness(self):
        _, bin_val, _ = convert(5)
        self.assertEqual(bin_val, "0000000000000101")

    def test_signed_small_number(self):
        _, _, signed = convert(123)
        self.assertEqual(signed, 123)

    def test_signed_max_unsigned(self):
        _, _, signed = convert(65535)
        self.assertEqual(signed, -1)

    def test_signed_boundary(self):
        _, _, signed = convert(32768)
        self.assertEqual(signed, -32768)

    def test_zero(self):
        hex_val, bin_val, signed = convert(0)
        self.assertEqual(hex_val, "0")
        self.assertEqual(bin_val, "0000000000000000")
        self.assertEqual(signed, 0)


if __name__ == "__main__":
    unittest.main()

    #this is sample code. it should be removed once started.