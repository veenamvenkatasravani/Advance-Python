fruits = ["Apple", "Banana", "Mango"]

my_iterator  = iter(fruits)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))


#Iterator with a string

word = "CODE"

iterator = iter(word)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


#Iterator with a tuple

numbers = (100, 200, 300)

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))