print('Hello')

print(123 + 24)
print(3 ** 5)
print(3 * 4 * 5 * 6 * 7)

number_of_cookies = 25
number_of_students = 100
print(number_of_students / number_of_cookies)

#lab1d

def factorial (n: int) -> int:
    ''' Compute n! (n factorial) '''
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)
assert factorial(0) == 1
assert factorial(5) == 120

print("10! is", factorial(10))
print("100! is", factorial(100))
print("120! is", factorial(120))
print("(50 * 10)! is", factorial((50*10)))
print("5! is", factorial(5))

#lab1e

print(20*2)
print(56%2)

print(2 + 4 + 6 + 8 + 10)
print((75 + 83.5 + 61 + 43) / 4)
print(2 ** 10)
print(.5 * 50 * 15 ** 2)


wall = 'w'
cannon = 'c'

print(wall + cannon)
print(wall + cannon + wall)
print(3 * wall + cannon + 3 * wall)
print((wall + 2 * cannon) * 4)
print((3 * wall + cannon) * 4 + wall)
print((4 * wall + cannon) * 4 + 4 * wall)


test_scores = "4325220523455023"

print(test_scores[0])
print(test_scores[4])
print(test_scores[9])
print(test_scores[15])


s = "anteater"

print(s[0] == 'a')
print(s[-1] == 'r')
print(s[3] == 'x')
print(s[0:3] == 'zot')

pi = 3.14159
make = 'Toyota'
model = 'Camry'
year = 2014
ICS_majors = ['Computer Science', 'Informatics', 'Computer Game Science']
a = (3 + 5 + 7 + 9) / 4

print(20 + 35 > 2 ** 4)
print('hello' != 'goodbye')
print(10%3 <= 1)
print(len(["apple", "orange", "banana", "mango"]) == 5)
print(63%2)


s = "abcdefghijklmnopqrstuvwxyz"

print(s[3] + s[14] + s[6])
print(s[-7] + s[-5])
print(s[8] + s[2] + s[-8])
print(s[-6] + s[2] + s[8])