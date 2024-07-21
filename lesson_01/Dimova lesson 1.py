# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# or

side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4

# or

first_side = 1
second_side = 2
third_side = 3
fourth_side = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача

perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)

# or

perimetery = side_1 + side_2 + side_3 + side_4
print(perimetery)

# or

perimetery = first_side + second_side + third_side + fourth_side
print(perimetery)

# Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі

# task 07
# У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
# Скільки всього дерев посадили в саду?

apples = 4
pears = apples + 5
plums = apples - 2
trees = apples + pears + plums
print(trees)

# task 08
# До обіда температура повітря була на 5 градусів вище нуля.
# Після обіду температура опустилася на 10 градусів.
# Надвечір потепліло на 4 градуси. Яка температура надвечір?

before_lunch = 5
after_lunch = before_lunch - 10
evening = after_lunch + 4
print(evening)

# task 09
# Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
# 1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
# Скількі сьогодні дітей у театральному гуртку?

boys = 24
girls = boys / 2
boys_in = boys - 1
girls_in = girls - 2
kids = boys_in + girls_in
print(kids)

# task 10
# Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
# а третя - як половина вартості першої та другої разом.
# Скільки будуть коштувати усі книги, якщо купити по одному примірнику?

first_book = 8
second_book = first_book + 2
third_book = (first_book + second_book) / 2
books_together = first_book + second_book + third_book
print(books_together)
