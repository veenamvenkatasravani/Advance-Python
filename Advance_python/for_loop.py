numbers = [1,2,3,4,5]
for number in numbers:
    print(number)


#iterator tho approximately ila work avuthundi:

numbers = [1, 2, 3]

iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break

