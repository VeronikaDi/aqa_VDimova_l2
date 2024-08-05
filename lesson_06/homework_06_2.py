# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".


is_correct_str: bool = False

while not is_correct_str:
    provided_word: str = input("Provide your word please: ").lower()

    if provided_word.find("h") != -1:
        is_correct_str = True
