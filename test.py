def mydecorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@mydecorator
def say_whee():
    print("Welcome!")

say_whee()