"""
Оберіть від 3 до 5 різних домашніх завдань та:
- перетворюєте їх у функції (якщо це потрібно)
- створіть в папці файл homeworks.py куди вставте ваші функції з дз
- покрийте їх не менш ніж 10 тестами, 5 позитивних та 5 негативних (це загальна к-сть на все ДЗ).
- імпорт та самі тести помістіть в окремому файлі - test_homeworks09.py
"""

# 01 function from HW 8


def sum_of_numbers(s):
    try:
        numbers = [int(num) for num in s.split(',')]
        return sum(numbers)
    except ValueError:
        return "I can not sum this group"


# list_from_task = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
#
# results = [sum_of_numbers(s) for s in list_from_task]
# print(results)


# 02 function from HW 7


def sum_numbers(a, b):
    return a + b


# result = sum_numbers(3, 5)
# print(result)


# 03 function from HW 7


def num_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# num_list = [15, 7, 39, 51, 46]
# average = num_average(num_list)
# print(average)


# 04 function from HW 7


def reverse_str(s):
    return s[::-1]


# new_string = [97, 63, 75, 25, 5]
# reversed_str = reverse_str(new_string)
# print(reversed_str)


# 05 function from HW 7


def find_longest_word(words):
    if not words:
        return ""
    long_word = max(words, key=len)
    return long_word


# words_list = ["Serhii", "Plan", "employment", "eye"]
# longest_word = find_longest_word(words_list)
# print(longest_word)
