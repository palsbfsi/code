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

    #More test cases can be added...
    
if __name__ == '__main__':
    unittest.main()