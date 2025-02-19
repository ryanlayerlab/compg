import unittest
import string_search

class TestStringSearch(unittest.TestCase):
    def test_string_search(self):
        self.assertEqual(string_search.naive_search('abc', 'abc'), [0])
        self.assertEqual(string_search.naive_search('abcabc', 'abc'), [0,3])
        self.assertEqual(string_search.naive_search('abc', 'bc'), [1])
        self.assertEqual(string_search.naive_search('abc', 'c'), [2])
        self.assertEqual(string_search.naive_search('abc', 'x'), [])

    def test_bad_char_table(self):
        bct = string_search.get_bad_char_table('CTTACTTAC')

        self.assertEqual(bct[(8,'A')], 1)
        self.assertEqual(bct[(8,'C')], 4)
        self.assertEqual(bct[(8,'T')], 2)

        self.assertEqual(bct[(5,'A')], 2)
        self.assertEqual(bct[(5,'C')], 1)
        self.assertEqual(bct[(5,'T')], 3)

        self.assertTrue((1,'A') not in bct)
        self.assertTrue((3,'A') not in bct)

    def test_bc_string_search(self):
        self.assertEqual(string_search.nn_with_bc('abc', 'abc'), [0])
        self.assertEqual(string_search.nn_with_bc('abcabc', 'abc'), [0,3])
        self.assertEqual(string_search.nn_with_bc('abc', 'bc'), [1])
        self.assertEqual(string_search.nn_with_bc('abc', 'c'), [2])
        self.assertEqual(string_search.nn_with_bc('abc', 'x'), [])


