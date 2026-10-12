numbers = [10, 20]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print("No more elements")