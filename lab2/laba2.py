def greet(name):
    print("Привет,", name)

def square(number):
    return number ** 2

def max_of_two(x, y):
    return max(x, y)

def describe_person(name, age=30):
    print("Имя:", name)
    print("Возраст:", age)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
