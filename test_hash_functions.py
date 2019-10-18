import unitest
import os
import hash_functions as hf

Class TestHashFunctions(unitest.TestCase)

    def test_no_input_N(self):
        self.assertRaises(TypeError, hf.h_ascii, 'text', None)

    def test_ascii_no_key(self):
        self.assertEqual(hf.h_ascii([], 10), 'Specify key')

    def test_rolling_costant(self):
        k = 107
        e = 101
        y = 121
        total = k + e + y
        N = 20
        self.assertEqual(hash_functions.h_ascii('key', 20), total % N)

    def test_H_first_position(self):
        r = hash_functions.h_rolling('key', 1)
        self.assertEqual(r, 0)
