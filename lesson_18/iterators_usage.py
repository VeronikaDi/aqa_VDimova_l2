from iterators import ReverseElementsIterator, ReturnsEvenNumbersIterator


reversed_list = ReverseElementsIterator([10, 20, 30, 40, 50])
for item in reversed_list:
    print(item)


even_iter = ReturnsEvenNumbersIterator(67)
for num in even_iter:
    print(num)
