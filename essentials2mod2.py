# Essentials2 Module 2

multi = """multiline
string
within
triple
quotes"""
print(multi)
print(len(multi))  # 37


str1 = 'a'
str2 = 'b'
print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)


# ord() function. ord = ASCII/UNICODE code point value (ord = ordinal)
print(ord("C"))     # prints C code point == 67
print(ord("!"))     # prints ! code point == 33

# chr() function. chr = convert code point number to character (chr = character) (opposite to ord)
print(chr(67))  # prints code point 67 == "C"
print(chr(33))  # prints code point 33 == "!"

print(chr(ord("C")))
print(ord(chr(33)))


# strings aren't lists, but you can treat them like lists in many particular cases.
the_string = 'silly walks'          # Indexing strings.
for ix in range(len(the_string)):   # len = 11
    print(the_string[ix], end=' ')  # print each chr with space seperator
print()

the_string = 'silly walks'          # iterating through strings
for character in the_string:
    print(character, end=' ')
print()

# slices
alpha = "abdefg"
print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])       # slice full list from 0 in steps of 2
print(alpha[1::2])      # slice full list from 1 in steps of 2

# in operator
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)

# not in operator
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)

# strings are immutable - cant use del,append, insert
# to modify strings use concatenation to redefine the entire variable as below:
alphabet = "bcdefghijklmnopqrstuvwxy"
alphabet = "a" + alphabet
alphabet = alphabet + "z"
print(alphabet)


# min() finds the minimum element of the sequence passed as an argument. min as per ascii/unicode table
print(min("aAbByYzZ"))

t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))