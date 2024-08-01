# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті


provided_list_1: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   #  30
provided_list_2: list[int] = [10, 11, 20, 27, 30, 33]  #  60

sum_result: int = 0
for integer in provided_list_1:
    if integer % 2 == 0:
        sum_result += integer

print(sum_result)

sum_result: int = 0
for integer in provided_list_2:
    if integer % 2 == 0:
        sum_result += integer

print(sum_result)

# or could be solved as:

result: int = sum([integer for integer in provided_list_1 if integer % 2 == 0])

print(result)

result_2: int = sum([integer for integer in provided_list_2 if integer % 2 == 0])

print(result_2)