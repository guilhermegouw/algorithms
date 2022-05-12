from bubble_sort import bubble_sort
import unittest


class BubbleSortTest(unittest.TestCase):
    def test_bubble_sort_one_element(self):
        self.assertEqual(bubble_sort([1]), [1])

    def test_bubble_sort_two_ordered_elements(self):
        self.assertEqual(bubble_sort([1, 2]), [1, 2])

    def test_bubble_sort_two_unordered_elements(self):
        self.assertEqual(bubble_sort([2, 1]), [1, 2])

    def test_bubble_sort_three_elements_case_1(self):
        self.assertEqual(bubble_sort([1, 3, 2]), [1, 2, 3])

    def test_bubble_sort_three_elements_case_2(self):
        self.assertEqual(bubble_sort([2, 3, 1]), [1, 2, 3])
    
    def test_four_elements_unordered(self):
        self.assertEqual(bubble_sort([4, 2, 3, 1]), [1, 2, 3, 4])
    
    def test_ten_elements_unordered(self):
        self.assertEqual(bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])




if __name__=='__main__':
    unittest.main()