# 01 function from HW 8


def sum_of_numbers(s):
    try:
        numbers = [int(num) for num in s.split(',')]
        return sum(numbers)
    except ValueError:
        return "I can not sum this group"


# 02 function from HW 7


def sum_numbers(a, b):
    return a + b


# 03 function from HW 7


def num_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# 04 function from HW 7


def reverse_str(s):
    return s[::-1]


# 05 function from HW 7


def find_longest_word(words):
    if not words:
        return ""
    long_word = max(words, key=len)
    return long_word
