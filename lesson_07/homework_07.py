# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):  # Initialize the appropriate variable
    multiplier = 1
    # Complete the while loop condition.
    while True:
        result = number * multiplier  # десь тут помилка, а може не одна
        if result > 25:  # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))  # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sum_numbers(a, b):
    return a + b


result = sum_numbers(3, 5)
print(result)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def num_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


num_list = [15, 7, 39, 51, 46]
average = num_average(num_list)
print(average)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reverse_str(s):
    return s[::-1]


new_string = [97, 63, 75, 25, 5]
reversed_str = reverse_str(new_string)
print(reversed_str)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def find_longest_word(words):
    if not words:
        return ""
    long_word = max(words, key=len)
    return long_word


words_list = ["Serhii", "Plan", "employment", "eye"]
longest_word = find_longest_word(words_list)
print(longest_word)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# 4 tasks are taken and converted into functions from HW 4:


adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""


# 07 task = function


def count_character_occurrences(text, character):
    """
    Counts the number of occurrences of a character in the text "adwentures_of_tom_sawer"
    :param: text (str): text in which occurrences of the character should be counted
    character (str): character to be counted
    :return:
    int: the number of occurrences of the character in the text
    """
    return text.count(character)


result = count_character_occurrences(adwentures_of_tom_sawer, 'v')
print(f'The number of letters "v": {result}')


# 08 task = function


def count_capital_letters(text):
    """
    Counts the number of capital letters in the text "adwentures_of_tom_sawer"
    :param: text (str): text in which capital letters should be counted
    :return: int: quantity of capital letters
    """
    return sum(1 for char in text if char.isupper())


result = count_capital_letters(adwentures_of_tom_sawer)
print(f'The quantity of capital letters: {result}')

# 09 task = function

import re


def split_into_sentences(text):
    """
    Splits text into sentences. Uses a regular expression to split the text into sentences,
    taking into account possible abbreviations and names
    :param: text: (str): text to split into sentences
    :return: list: list of sentences
    """
    return re.split(r'(?<!\w.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', adwentures_of_tom_sawer)


adwentures_of_tom_sawer_sentences = split_into_sentences(adwentures_of_tom_sawer)
for sentence in adwentures_of_tom_sawer_sentences:
    print(f"\n"
          f"{sentence}")


# 10 task = function


def starts_with_by_the_time(sentences):
    """
    Checks if at least one sentence starts with "By the time"
    :param: sentences (list): list of sentences
    :return: bool: True if at least one sentence starts with "By the time", otherwise False
    """
    return any(sentence.strip().startswith("By the time") for sentence in sentences)


sentences_2 = split_into_sentences(adwentures_of_tom_sawer)
start_with = starts_with_by_the_time(sentences_2)
if start_with:
    print(f"\n"
          "At least one sentence starts with \"By the time\".")
else:
    print(f"\n"
          "There are no sentences with \"By the time\" in the text.")
