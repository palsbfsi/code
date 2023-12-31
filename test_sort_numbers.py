import unittest
from sort_numbers import remove_duplicates_and_sort

class TestRemoveDuplicatesAndSort(unittest.TestCase):
    def test_basic_case(self):
        input_numbers = [10, 20, 30, 20, 40, 50, 10, 60, 70, 80]
        expected_output = [80, 70, 60, 50, 40, 30, 20, 10]
        
        sorted_numbers = remove_duplicates_and_sort(input_numbers)
        
        self.assertEqual(sorted_numbers, expected_output)
    
    def test_empty_input(self):
        input_numbers = []
        expected_output = []
        
        sorted_numbers = remove_duplicates_and_sort(input_numbers)
        
        self.assertEqual(sorted_numbers, expected_output)
    
    def test_duplicate_numbers(self):
        input_numbers = [5, 10, 5, 15, 10, 20]
        expected_output = [20, 15, 10, 5]
        
        sorted_numbers = remove_duplicates_and_sort(input_numbers)
        
        self.assertEqual(sorted_numbers, expected_output)
        
    #Test coundary condition
    def test_boundary_condition(self):
        input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
        expected_output = [100, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        
        sorted_numbers = remove_duplicates_and_sort(input_numbers)
        
        self.assertEqual(sorted_numbers, expected_output)

    
if __name__ == '__main__':
    unittest.main()