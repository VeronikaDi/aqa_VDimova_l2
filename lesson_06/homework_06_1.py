# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()


proposed_string: str = input("Provide your string here please: ")

unique_counter: int = sum([1 for char in proposed_string if proposed_string.count(char) == 1])

if unique_counter > 10:
    print(True)
else:
    print(False)
