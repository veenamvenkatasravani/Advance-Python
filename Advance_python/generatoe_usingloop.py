def count_numbers(n):
    for number in range(1, n + 1):
        yield number

for value in count_numbers(5):
    print(value)

#Generator for even numbers

def even_numbers(limit):
    for number in range(2, limit + 1, 2):
        yield number

for number in even_numbers(20):
    print(number)

#Generator expression
squares = (number ** 2 for number in range(1, 6))

for square in squares:
    print(square)