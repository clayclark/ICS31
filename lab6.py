#     Clayton Clark 92141310. ICS 31 Lab sec 11.

#### 1

print('------------------- 1 -----------------------')

def contains(str1: str, str2: str)-> bool:
    ''' Takes two strings and checks if second string is in the first string; If second is in then returns True'''

    if str2 in str1:
        return True
    else:
        return False

assert contains('banana', 'ana') == True
assert not contains('racecar', 'ck') == True


#### 2

print('------------------- 2 -----------------------')

def del_punct(str1: str)-> str:
    ''' Replaces a punctuation with a space '''
    sentence = []

    for i in str1:
        if i.isalnum() or i.isspace():
            sentence.append(i)
        else:
            sentence.append(' ')
    new_sentence = ''.join(sentence)
    return new_sentence

def words(str1: str)-> int:
    ''' Splits string into separate words '''

    sentence = del_punct(str1)
    new_sentence = sentence.split()

    return new_sentence

def avg_len(str1)-> float:
    sentence_list = words(str1)

    results = 0
    for i in range(len(sentence_list)):
        results = results + (len(sentence_list[i]))

    results = results / len(sentence_list)
    return results

def sentence_stats(str1: str)-> str:
    ''' Displays the Sentence Statistics '''
    print('Characters:', len(str1))
    print('Words: ', len(words(str1)))
    print('Average word length: ', avg_len(str1))

sentence_stats('***The ?! quick brown fox:  jumps over the lazy dog.')
sentence_stats('I love UCI')

#### 3

print('------------------- 3 -----------------------')

def initials(s: str):
    ''' Returns the initials of a name'''
    s = s.upper()
    s = words(s)

    initial = []
    for i in range(len(s)):
        initial.append(s[i][0])
    initial = ''.join(initial)
    return initial

assert initials('Bill Cody') == 'BC'
assert initials('Guido van Rossum') == 'GVR'
assert initials('alan turing') == 'AT'


#### d.1

print('------------------- d.1 -----------------------')

from random import randrange

for i in range(50):
    print(randrange(1, 11))

for i in range(50):
    print(randrange(1, 7))

#### d.2

print('------------------- d.2 -----------------------')

def dice():
    ''' Creates a dice '''
    return randrange(1,7)

def roll2dice():
    ''' Rolls two dice '''
    return(dice() + dice())

roll2dice()

for i in range(50):
    print(roll2dice())


#### d.3

print('------------------- d.3 -----------------------')


def distribution_of_rolls(x: int) -> str:
    results = []
    for i in range(0, x):
        results.append(randrange(1, 7) + randrange(1, 7))
    for y in range(2, 13):
        print("{:<2}:  {:<2} ({:<4}%) {}".format(y, results.count(y), round((results.count(y) / x) * 100, 2),
                                                 "*" * results.count(y)))
    print("-----------------------------")
    print(str(x) + ' rolls')


distribution_of_rolls(200)

#### e.1 - e.3

print('------------------- e.1 - e.3 -----------------------')


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def rotate_alpha(n: int)-> str:
    ''' Shifts the alphabet by the inputed integer '''
    new_alpha = []
    n = n%26
    new_alpha.append(ALPHABET[n:])
    new_alpha.append(ALPHABET[0:n])
    new_alpha = ''.join(new_alpha)
    return new_alpha


def Caesar_encrypt(s: str, n: int)-> str:
    '''Encodes string in Caesarian Cipher where ('a' becomes 'b', 'b' becomes 'c', and so on) is one example;
    we could say its key is 1, because each letter moves 1 position later in the alphabet.'''
    rotated_string = rotate_alpha(n)
    code = s.translate(str.maketrans(ALPHABET, rotated_string))
    return code

def Caesar_decrypt(s: str, n: int)-> str:
    '''Decrpyts the Caesarian Cipher'''
    rotated_string = rotate_alpha(n)
    code = s.translate(str.maketrans(rotated_string, ALPHABET))
    return code
print(Caesar_encrypt('hello', 7))

#### f.1

print('------------------- f.1 -----------------------')

prac_list = count = [ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        " ]

def print_line_numbers(l: list)-> str:
    ''' Takes in a list of strings and displays each item on a numbered line'''
    for i in range(len(l)):
        print('{:<5} {}'.format(str(i + 1) + ':', l[i] + '\n'))

#### f.2

print('------------------- f.2 -----------------------')
def empty_line(l: list)-> int:
    '''Returns number of empty lines in a list'''
    count = 0
    for i in range(len(l)):
        if l[i] == '':
            count += 1
    return count

def avg_char(l: list)-> float:
    '''Returns average number of characters per line of list'''
    count = 0
    for i in range(len(l)):
        count += len(l[i])
        count /= len(l)
        count = round(count, 1)
    return count

def avg_char_empty(l: list)-> float:
    '''Returns the average number of characters per non-empty line'''
    count = 0
    for i in range(len(l)):
        if l[i] != '':
            count += len(l[i])
            count /= len(l)
            count = round(count, 1)
    return count

def stats(l: list)-> str:
    ''' Displays stats of list inputed '''
    print('{:<7} {}'.format(len(l), 'lines in the list'))
    print('{:<7} {}'.format(empty_line(l),'empty lines'))
    print('{:<7} {}'.format(avg_char(l), 'average characters per line'))
    print('{:<7} {}'.format(avg_char_empty(l), 'average characters per non-empty line'))

stats(prac_list)

#### f.3

print('------------------- f.3 -----------------------')

def rid_white(s: str)-> str:
    results = []
    for i in s:
        if i == "'":
            results.append("'")
        if i.isspace():
            results.append('')
        elif i.isalnum():
            results.append(i)
        else:
            results.append('')
    results = ''.join(results)
    return results

def list_of_words(l: list)-> list:
    ''' Takes a list of strings and returns a list of individual words with white space and punctuation
        removed(except for apostrophes/single quotes'''
    for i in l:
        print (rid_white(i))

list_of_words(prac_list)
