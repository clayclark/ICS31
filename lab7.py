#Sarah Memon 48619347 and Clayton Clark 92141310 Lab Asst 7 Sec 11

#Part c.2:
print('---------------------Part c.2 ---------------------')

infile1 = open("C:/Users/Clay Clark/Desktop/surnames.txt", 'r')
infile2 = open("C:/Users/Clay Clark/Desktop/femalenames.txt", 'r')
infile3 = open("C:/Users/Clay Clark/Desktop/malenames.txt", 'r')

content = infile1.read()
surnames_lists = content.split()
s = []
for line in open("C:/Users/Clay Clark/Desktop/surnames.txt"):
    s.append(line.split()[0].capitalize())

content2 = infile2.read()
femalenames_lists = content2.split()
d = []
for line in open("C:/Users/Clay Clark/Desktop/femalenames.txt"):
    d.append(line.split()[0].capitalize())

content3 = infile3.read()
malenames_lists = content3.split()
f = []
for line in open("C:/Users/Clay Clark/Desktop/malenames.txt"):
    f.append(line.split()[0].capitalize())

f.extend(d)


# Part c.3
print("------------------PART c.3--------------------")
from random import randrange

def single_name():
    ''' Combines the surname and female and male names '''
    return(one_name(s) + ', ' + one_name(f))

def one_name(l: list)-> str:
    ''' Takes in one of three name lists and returns name chosen at random '''
    rand = randrange(0, len(l))
    return(l[rand])

def random_names(num: int) -> list:
    """ Produces a number of random name inputed in the syntax lastname, firstname; Can be male or female """
    new_list= []
    for i in range(num):
        new_list.append(single_name())
    return new_list

print(random_names(10))

#Part d.1
print("------------------PART d.1 --------------------")

infile4 = open("C:/Users/Clay Clark/Desktop/wordlist.txt")
dictionary = infile4.readlines()
infile4.close()

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def rotate_alpha(n: int) -> str:
    ''' Shifts the alphabet by the inputed integer '''
    new_alpha = []
    n = n % 26
    new_alpha.append(ALPHABET[n:])
    new_alpha.append(ALPHABET[0:n])
    new_alpha = ''.join(new_alpha)
    return new_alpha

def Caesar_encrypt(s: str, n: int)-> str:
    '''Encodes string in Caesarian Cipher where ('a' becomes 'b', 'b' becomes 'c', and so on) is one example;
    we could say its key is 1, because each letter moves 1 position later in the alphabet.'''
    rotated_string = rotate_alpha(n)
    s = s.lower()
    code = s.translate(str.maketrans(ALPHABET, rotated_string))
    return code.capitalize()

def Caesar_decrypt(s: str, n: int) -> str:
    '''Decrpyts the Caesarian Cipher'''
    rotated_string = rotate_alpha(n)
    s = s.lower()
    code = s.translate(str.maketrans(rotated_string, ALPHABET))
    return code

def Caesar_break(cipher: str)-> str:
    '''takes a ciphertext string
    (encrypted using a Caesar cipher as we did last week)
    and returns the plaintext for that string, without having the key'''

    for i in range(26):
        word = Caesar_decrypt(cipher, i)
        word = word.capitalize()
        for x in dictionary:
            if word in x:
                return word

assert Caesar_break('Rncxeh') == 'Cynips'



#PART E:
print('-------------------- Part E -----------------------')

def copy_file(s: str):
    infile2 = open("C:/Users/Clay Clark/Desktop/book.txt")
    result = []

    for line in infile2:
        result.append(line)
    if s == 'line numbers':
        for i in range(len(result)):
            num = i+ 1
            print('{0:5}: {1:}'.format(num, result[i]))
    elif s == 'Gutenberg trim':
        start = result.index('*** START OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***\n')
        end = result.index('*** END OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***\n')
        result = (result[start:end])
        result = ' '.join(result)
        return result


    elif s == "statistics":
        num_lines = len(result)
        num_empty = 0
        char_count = 0
        for item in result:
            if item is None:
                num_empty += 1
            for characters in item:
                char_count += 1
        print('{:5.1f} '.format(num_lines) + 'lines in the list')
        print('{:5.1f} '.format(num_empty) + 'empty lines')
        print('{:5.1f} '.format(char_count/num_lines) + 'average characters per line')
        print('{:5.1f} '.format(char_count/(num_lines - num_empty)) + 'average characters per non-empty line')

    else:
        infile_name = input("Please enter the name of the file to copy: ")
        infile = open(infile_name, 'r')
        outfile_name = input("Please enter the name of the new copy:  ")
        outfile = open(outfile_name, 'w')
        for line in infile:
            outfile.write(line)
        infile.close()
        outfile.close()
# print(copy_file('statistics'))
# print(copy_file('line numbers'))
# print(copy_file('Gutenberg trim'))
# print(copy_file('fdsafda'))






