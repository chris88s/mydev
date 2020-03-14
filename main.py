import sys

print(sys.version)
print(sys.executable)


def greet(who_to_greet):

    greeting = "hello, {}".format(who_to_greet)
    return greeting


print(greet("adam"))
name = input('name: ')
print('hi,', name)
