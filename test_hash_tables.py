import hash_tables
import hash_functions
import unittest

class TestHashTables(unitest.TestCase)

    def Test_LinearProbe_search_ascii(self):
        test = hash_tables.LinearProbe(10, hash_functions.h_ascii)
        test.T = [(str(i), 2*i) for i in range(test.N)]
        self.assertEqual(test.search('3'), 6)

     def Test_LinearProbe_search_rolling(self):
        test = hash_tables.LinearProbe(10, hash_functions.h_rolling)
        test.T = [(str(i), 2*i) for i in range(test.N)]
        self.assertEqual(test.search('3'), 6)

     def Test_LinearProbe_search_in_table_random(self):
        test = hash_tables.LinearProbe(10, hash_functions.h_python)
        test.T = [(str(i), 2*i) for i in range(test.N)]
        self.assertEqual(test.search('3'), 6)
