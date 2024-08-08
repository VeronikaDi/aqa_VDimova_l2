# Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
# [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
# Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
# Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі),
# вам потрібно зловити вийняток і вивести “Не можу це зробити!”
# Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
# Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”


test_list_1: list[str] = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
test_list_2: list[str] = ["1,2,3,4", "1,2,3,4,50", "1,2,3"]


def sum_all_chars_in_string_if_int(test_list: list[str]) -> None:
    result: list[int] = list()
    try:
        for item in test_list:
            chars_list: list = item.split(",")
            result.append(sum(int(integer) for integer in chars_list))
    except ValueError as exception:
        print(f"I can not sum your items from list due to: {exception}")
    else:
        print(result)


sum_all_chars_in_string_if_int(test_list_1)
sum_all_chars_in_string_if_int(test_list_2)


# Or it can be also solved as:


def sum_of_numbers(s):
    try:
        numbers = [int(num) for num in s.split(',')]
        return sum(numbers)
    except ValueError:
        return "I can not sum this group"


list_from_task = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

results = [sum_of_numbers(s) for s in list_from_task]
print(results)
