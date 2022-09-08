import random
from faker import Faker

fake = Faker('ru_RU')
for _ in range(3):
    print(random.randint(0, 20))
for _ in range(2):
    print("This is random name: " + fake.name())

for _ in range(2):
    print("This is random adress: " + fake.address())
for _ in range(2):
    print("This is random text: " + fake.text())

print('Hello world')
print("Hello world")
print('Hello "world"')
print('Hello \'world\'')
print(r'Hello \'world\'') #row string. don't work any spechial simbols
print("abc" * 5)
alphabet = "abcdefg"
for i in range(len(alphabet)):
    print(alphabet[i]) # show simbol into string
print(alphabet[0:3])
print(alphabet[0::2]) #step 2
print(alphabet[::]) #also all simbols
print(alphabet[::-1]) #revers string
print(alphabet[0:-1])
print(alphabet[-1]) #show last simbol

first="first word"
second="second word"
third="third word"
print(f"{first} {second} {third} 100 {100}")
