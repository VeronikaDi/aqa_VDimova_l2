name = "Veronika"
age = 31

print(name,
      age)

a = 0.0028
b = 0.0026
result = a / b
result_2 = result - 1
result_3 = result_2 * 100

print(result_3)

is_true = True
is_false = False

result = is_true or is_false
result_2 = is_true and is_false
print(result)
print(result_2)

if age and result_3 == 10:
      print(True)

# my_tuple = (1, 2, 3)
#
# print("My name: \n"
#      "Veronika")
#
# status = "completed"
#
# print(status[-1])
# size_of_sequence = len(status)
# last_symbol_index = len(status) - 1
#
# print(status[last_symbol_index])
#
# for symbol in status:
#      print(symbol)

my_tuple = (1, 2, 3)
my_tuple2 = tuple([1, 4, 6])
print(my_tuple[-1])

my_list = ["Nika", "Vera", "Naida"]
# my_list_2 - list(["Nika", "Vera", "Naida", "Max"])

print(my_list)
my_list.append("Max")
print(my_list)
my_list.remove("Naida")
print(my_list)
for name in my_list:
      print(name)

my_set = {1, 2, 3, 3}
print(my_set)
print(my_set)
print(my_set)

my_dict = {"name": "Vero",
           "age": "31"}
print(my_dict['name'])

a = 3
b = 4

if a == b:
    print("Yes")
if a != b:
    print("Yes")

x = min (1, 2, 3)
y = max(1, 2, 3)
print(x)
print(y)

user_names = ["Alla", "Mila", "Viktor", "Zina", "Alex"]
user_ages = [23, 45, 76, 82, 19]

for name in user_names:
    print(f"Current User name is: {name}")
for age in user_ages:
    print(f"Current User age is: {age}")

user_dict = {"Serhii": 56,
             "Max": 43}
for age, name, in enumerate(user_dict):
    print(f"User Name: {name} \n",
          f"User Age: {age}")

user_name = input("Fill your name here: ")

print(f"User name is: {user_name}")

user_age = int(input("Fill your age here: "))

if user_age == 36:
    print(f"User age is: {user_age}")
