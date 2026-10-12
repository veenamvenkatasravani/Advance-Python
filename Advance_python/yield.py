def demo():
    print("Start")
    yield 10

    print("Middle")
    yield 20

    print("End")

result = demo()

print(next(result))
print(next(result))

#return vs yield

def normal_function():
    return 10

def generator_function():
    yield 10
    yield 20

print(normal_function())
print(list(generator_function()))