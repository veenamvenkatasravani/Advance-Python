def get_numbers():
    return [1,2,3,4,5]

numbers = get_numbers()
print(numbers)


#generator_function

def get_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

numbers = get_numbers()

print(next(numbers))
print(next(numbers))
print(next(numbers))