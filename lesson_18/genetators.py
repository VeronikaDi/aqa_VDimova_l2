
def sequence_even_numbers_generator(N):
    for num in range(0, N + 1, 2):
        yield num


def fibonacci_generator(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b
