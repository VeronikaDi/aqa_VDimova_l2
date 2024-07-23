alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n"'
                       'I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')

print(alice_in_wonderland)

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

s_black_sea = 436402
s_azov_sea = 37800
s_total = s_black_sea + s_azov_sea

print(f"{s_total} km2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

total_in_all_3 = 375291
total_in_1_and_2 = 250449
total_in_2_and_3 = 222950
goods_in_1 = total_in_all_3 - total_in_2_and_3
goods_in_3 = total_in_all_3 - total_in_1_and_2
goods_in_2 = total_in_all_3 - goods_in_1 - goods_in_3
# or
# goods_in_2 = total_in_2_and_3 - goods_in_3
# or
# goods_in_2 = total_in_1_and_2 - goods_in_1

print(goods_in_1)
print(goods_in_2)
print(goods_in_3)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

months_to_pay = 12 + 6
price_per_month = 1179
total_price = months_to_pay * price_per_month

print(f"{total_price} UAH")

# or

price_per_month_2 = 1179
years_to_pay_2 = 1.5
months_to_pay_2 = int(years_to_pay_2 * 12)
total_price_2 = months_to_pay * price_per_month

print(f"{total_price_2} UAH")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

a = 8019
b = 9907
c = 2789
d = 7248
e = 7128
f = 19224
a_div = 8
b_div = 9
c_div = 5
d_div = 6
e_div = 5
f_div = 9

a_ost = a % a_div
b_ost = b % b_div
c_ost = c % c_div
d_ost = d % d_div
e_ost = e % e_div
f_ost = f % f_div

print(a_ost, b_ost, c_ost, d_ost, e_ost, f_ost)

# or
print(a_ost)
print(b_ost)
print(c_ost)
print(d_ost)
print(e_ost)
print(f_ost)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

big_pizza = 274
middle_pizza = 218
juice = 35
cake = 350
water = 21

big_pizza_quantity = 4
middle_pizza_quantity = 2
juice_quantity = 4
cake_quantity = 1
water_quantity = 3

big_pizza_cost = big_pizza * big_pizza_quantity
middle_pizza_cost = middle_pizza * middle_pizza_quantity
juice_cost = juice * juice_quantity
cake_cost = cake * cake_quantity
water_cost = water * water_quantity

total_cost = big_pizza_cost + middle_pizza_cost + juice_cost + cake_cost + water_cost

print(f"{total_cost} UAH")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

total_photos = 232
max_photos_per_page = 8

pages_needed = total_photos / max_photos_per_page
print(pages_needed)

# also could be (ONLY if the number has an integer value):

pages_needed_2 = total_photos // max_photos_per_page
print(pages_needed_2)

# or

pages_needed_3 = int(total_photos / max_photos_per_page)
print(pages_needed_3)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

total_way = 1600
way_cut = 100
petrol_per_way_cut = 9
tank_capacity = 48

# 1)
total_petrol = (total_way / way_cut) * petrol_per_way_cut
print(f"{total_petrol} liters")

# 2)
total_stops_for_full_tank = total_petrol / tank_capacity
print(total_stops_for_full_tank)
