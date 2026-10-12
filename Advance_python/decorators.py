#A decorator is a function that adds extra behavior to another function without changing its original code.
#For example, imagine you have several functions. You want to print "Function started" before each function runs. Instead of writing the same print statement repeatedly, you can use a decorator.

def my_decorator(function):
    def wrapper():
        print("Before function execution")

        function()

        print("After function execution")

    return wrapper


@my_decorator
def greet():
    print("Hello Sravani!")


greet()

#Decorator with function arguments
#Sometimes the original function accepts arguments. In that case, use *args and **kwargs in the wrapper.

def my_decorator(function):
    def wrapper(*args, **kwargs):
        print("Calculating result...")

        result = function(*args, **kwargs)

        print("Calculation completed")
        return result

    return wrapper


@my_decorator
def add(a, b):
    return a + b


answer = add(10, 20)
print("Result:", answer)