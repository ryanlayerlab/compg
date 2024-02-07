#make unit tests for naive_search.py
import unittest
import naive_search

class TestNaiveSearch(unittest.TestCase):
    def test_naive_search(self):
        self.assertEqual(naive_search.naive_search('AA', 'A'),
                         [0,1])
        self.assertEqual(naive_search.naive_search('A', 'C'),
                         [])
        self.assertEqual(naive_search.naive_search('A', 'A'),
                         [0])
        self.assertEqual(naive_search.naive_search('ACTG', 'CT'),
                         [1])
        self.assertEqual(naive_search.naive_search('ACTGCT', 'CT'),
                         [1,4])
        self.assertEqual(naive_search.naive_search('ACTGCTCT', 'CT'),
                         [1,4,6])
        self.assertEqual(naive_search.naive_search('CTACTGCTCT', 'CT'),
                         [0,3,6,8])



    def test_naive_search_backward(self):
        self.assertEqual(naive_search.naive_search_backward('AA', 'A'),
                         [0,1])
        self.assertEqual(naive_search.naive_search_backward('A', 'C'),
                         [])
        self.assertEqual(naive_search.naive_search_backward('A', 'A'),
                         [0])
        self.assertEqual(naive_search.naive_search_backward('ACTG', 'CT'),
                         [1])
        self.assertEqual(naive_search.naive_search_backward('ACTGCT', 'CT'),
                         [1,4])
        self.assertEqual(naive_search.naive_search_backward('ACTGCTCT', 'CT'),
                         [1,4,6])
        self.assertEqual(naive_search.naive_search_backward('CTACTGCTCT', 'CT'),
                         [0,3,6,8])

    def test_get_bct(self):
        bct = naive_search.get_bct('ACTGGTA')
        exps = {(1, 'A'): 1,
                (2, 'A'): 2, (2, 'C'): 1,
                (3, 'A'): 3, (3, 'C'): 2, (3, 'T'): 1,
                (4, 'A'): 4, (4, 'C'): 3, (4, 'T'): 2, 
                (5, 'A'): 5, (5, 'C'): 4,              (5, 'G'): 1,
                             (6, 'C'): 5, (6, 'T'): 1, (6, 'G'): 2}

        for exp in exps:
            self.assertEqual(bct[exp], exps[exp])

    def test_naive_search_bct(self):
        self.assertEqual(naive_search.naive_search_bct('AA', 'A'),
                         [0,1])
        self.assertEqual(naive_search.naive_search_bct('A', 'C'),
                         [])
        self.assertEqual(naive_search.naive_search_bct('A', 'A'),
                         [0])
        self.assertEqual(naive_search.naive_search_bct('ACTG', 'CT'),
                         [1])
        self.assertEqual(naive_search.naive_search_bct('ACTGCT', 'CT'),
                         [1,4])
        self.assertEqual(naive_search.naive_search_bct('ACTGCTCT', 'CT'),
                         [1,4,6])
        self.assertEqual(naive_search.naive_search_bct('CTACTGCTCT', 'CT'),
                         [0,3,6,8])
        self.assertEqual(naive_search.naive_search_bct('CTATCCATCT', 'ATC'),
                         [2,6])
        self.assertEqual(naive_search.naive_search_bct('CGAAGCTTTT', 'AAGCTTT'),
                         [2])

    def test_naive_search_bct_gst(self):
        self.assertEqual(naive_search.naive_search_bct_gst('AA', 'A'),
                         [0,1])
        self.assertEqual(naive_search.naive_search_bct_gst('A', 'C'),
                         [])
        self.assertEqual(naive_search.naive_search_bct_gst('A', 'A'),
                         [0])
        self.assertEqual(naive_search.naive_search_bct_gst('ACTG', 'CT'),
                         [1])
        self.assertEqual(naive_search.naive_search_bct_gst('ACTGCT', 'CT'),
                         [1,4])
        self.assertEqual(naive_search.naive_search_bct_gst('ACTGCTCT', 'CT'),
                         [1,4,6])
        self.assertEqual(naive_search.naive_search_bct_gst('CTACTGCTCT', 'CT'),
                         [0,3,6,8])
        self.assertEqual(naive_search.naive_search_bct_gst('CTATCCATCT', 'ATC'),
                         [2,6])
        self.assertEqual(naive_search.naive_search_bct_gst('CGAAGCTTTT', 'AAGCTTT'),
                         [2])


    def test_naive_search_gst(self):
        self.assertEqual(naive_search.naive_search_gst('AA', 'A'),
                         [0,1])
        self.assertEqual(naive_search.naive_search_gst('A', 'C'),
                         [])
        self.assertEqual(naive_search.naive_search_gst('A', 'A'),
                         [0])
        self.assertEqual(naive_search.naive_search_gst('ACTG', 'CT'),
                         [1])
        self.assertEqual(naive_search.naive_search_gst('ACTGCT', 'CT'),
                         [1,4])
        self.assertEqual(naive_search.naive_search_gst('ACTGCTCT', 'CT'),
                         [1,4,6])
        self.assertEqual(naive_search.naive_search_gst('CTACTGCTCT', 'CT'),
                         [0,3,6,8])
        self.assertEqual(naive_search.naive_search_gst('CTATCCATCT', 'ATC'),
                         [2,6])
        self.assertEqual(naive_search.naive_search_gst('CGAAGCTTTT', 'AAGCTTT'),
                         [2])




if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
