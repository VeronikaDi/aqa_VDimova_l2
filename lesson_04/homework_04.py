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

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3

# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

print(adwentures_of_tom_sawer.replace("\n", " "))

# task 02 ==
""" Замініть .... на пробіл"""

print(adwentures_of_tom_sawer.replace(" ....", ""))

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами."""

print(adwentures_of_tom_sawer.replace("  ", " "))

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h" """

letter_h = adwentures_of_tom_sawer.count("h")
print(f"\n"
      f"The number of letters h in adwentures_of_tom_sawer is {letter_h}.")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?"""

capital_letter = 0
for char in adwentures_of_tom_sawer:
    if char.isupper():
        capital_letter += 1
print(f"\n"
      f"The number of capital letters in adwentures_of_tom_sawer is {capital_letter}.")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге"""

word = "Tom"
adwentures_of_tom_sawer_lower = adwentures_of_tom_sawer.lower()
tom_lower = word.lower()
first_place = adwentures_of_tom_sawer_lower.find(tom_lower)

if first_place == -1:
    print("\n"
          "There is no name Tom in the text.")
else:
    second_place = adwentures_of_tom_sawer_lower.find(tom_lower, first_place + len(tom_lower))

    if second_place == -1:
        print("\n"
              "The name Tom appeared in the  text only once")
    else:
        print(f"\n"
              f"Second time name {word} appeared in the text at {second_place} position.")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences"""
adwentures_of_tom_sawer_sentences = None

import re

adwentures_of_tom_sawer_sentences = re.split(r'(?<!\w.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', adwentures_of_tom_sawer)

for sentence in adwentures_of_tom_sawer_sentences:
    print(f"\n"
          f"{sentence}")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр."""

sentences_split = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', adwentures_of_tom_sawer)
if len(sentences_split) >= 4:
    fourth_sentence = sentences_split[3]
    fourth_sentence_lower = fourth_sentence.lower()
    print(f'\n'
          f'Sentence number 4 with low register is: \n'
          f'{fourth_sentence_lower}')
else:
    print("\n"
          "There is no 4th sentence in the text")

# task 09
""" Перевірте чи починається якесь речення з "By the time"."""

sentences_2 = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', adwentures_of_tom_sawer)
start_with = any(sentence.strip().startswith("By the time") for sentence in sentences_2)

print(start_with)

if start_with:
    print('\n'
          'At least one sentence starts with "By the time".')
else:
    print('\n'
          'There are no sentences with "By the time" in the text.')


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences."""

sentence_3 = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', adwentures_of_tom_sawer)
last_sentence = sentence_3[-1].strip()
number_of_words = len(last_sentence.split())

print(f'\n'
      f'The last sentence in "adwentures_of_tom_sawer" consists of {number_of_words} words.')
