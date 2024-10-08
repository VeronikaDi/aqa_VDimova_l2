import unittest
from homework_09 import sum_of_numbers, sum_numbers, num_average, reverse_str, find_longest_word


class TestHomework09(unittest.TestCase):
    # The test for 01 function from HW 8
    def test_sum_of_numbers_positive(self):
        self.assertEqual(sum_of_numbers("100,-50,50"), 100)

    def test_sum_of_numbers_negative(self):
        self.assertEqual(sum_of_numbers("a,b,c"), "I can not sum this group")

    # The test for 02 function from HW 7
    def test_sum_numbers_positive(self):
        self.assertEqual(sum_numbers(3, 5), 8)

    def test_sum_numbers_negative(self):
        with self.assertRaises(TypeError):
            sum_numbers("five", 5)

    # The test for 03 function from HW 7
    def test_num_average_positive(self):
        self.assertEqual(num_average([1, 2, 3, 4, 5]), 3.0)

    def test_num_average_negative(self):
        with self.assertRaises(TypeError):
            num_average([1, "two", 3])

    # The test for 04 function from HW 7
    def test_reverse_str_positive(self):
        self.assertEqual(reverse_str("Monday"), "yadnoM")

    def test_reverse_str_negative(self):
        self.assertEqual(reverse_str([1, 2, 3]), ["3, 2, 1"])

    # The test for 05 function from HW 7

    def test_find_longest_word_positive(self):
        self.assertEqual(find_longest_word(["apple", "employment", "cherry"]), "employment")

    def test_find_longest_word_negative(self):
        self.assertEqual(find_longest_word(["to", 123, "v"]), "123")


if __name__ == '__main__':
    unittest.main()
