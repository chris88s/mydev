# 1
from getpass import getpass
'''condition = True
x = 1 if condition else 0

# 2
n1 = 10_000_000_000
n2 = 100_000_000
total = n1 + n2
print(f'{total:,}')

# 3
with open('words.txt', 'r') as f:
    file_contents = f.read()
words = file_contents.split(' ')
word_count = len(words)
print(word_count)

# 4
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']
for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}')

for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')

for value in zip(names, heroes, universes):
    print(value)

# unpacking
a, b, *_, d = (1, 2, 3, 4, 5, 6, 7)
print(a)
print(b)
# print(c)
print(d)

# 5


class Person():
    pass


person = Person()
person_info = {'first': 'Corey', 'last': 'Schafer'}

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))
'''

# 6
username = input('Username: ')
password = getpass('Password: ')
print('logging in...')
