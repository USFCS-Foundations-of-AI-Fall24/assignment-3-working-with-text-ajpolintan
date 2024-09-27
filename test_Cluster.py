from unittest import TestCase
import unittest
from Cluster import *
from Document import *

class TestCluster(TestCase):
    def test_calculate_centroid(self):
       pass

    def test_kmeans(self):
        d = Document(true_class='pos')
        d.add_tokens(['cat', 'dog', 'fish'])
        d2 = Document(true_class='pos')
        d2.add_tokens(['cat', 'dog', 'fish'])
        d3 = Document(true_class='neg')
        d3.add_tokens(['bunny', 'lizard', 'octopus', 'bunny'])
        d4 = Document(true_class='neg')
        d4.add_tokens(['rare', 'care', 'bear'])
        #if there is an empty document ignore 
        print(k_means(2, ['pos', 'neg'], [d,d2,d3,d4]))
        



if __name__ == '__main__':
    unittest.main()