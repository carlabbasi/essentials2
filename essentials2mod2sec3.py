# Essentials2 Module 2 Section 3

# STRING METHODS

# capitalize() method: Only capitalizes index 0 (if it's a letter)
print("capitalize this string".capitalize())
print("928375 numbers don't work".capitalize())

a = "word one"
a.capitalize()      # this capitalise doesn't change anything as it hasn't been stored in a variable
print(a)

b = "word two"
c = b.capitalize()
print(b)
print(c)


# centre() method: used to pad a string. by default adds spaces to 'centre' string
print('[' + 'alpha'.center(10) + ']')
print('[' + 'alpha'.center(20) + ']')
print('[' + 'alpha'.center(30) + ']')
print(' alpha '.center(40,))

# can be used with 2 arguments: second arg determines what is used to space the string out
print('[' + 'gamma'.center(20, '*') + ']')
print('[' + 'gamma'.center(30, '!') + ']')
print('[' + ' gamma '.center(40, '#') + ']')
print(' gamma '.center(50, '='))


# startswith() method: checks if a given string starts with the specified arg (returns True or False)
print("omega".startswith("meg"))
print("omega".startswith("om"))

# endswith() method: checks if the given string ends with the specified arg and returns True or False
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

# changed to use comprehension:
print("yes") if "epsilon".endswith("on") else print("no")


# find() method: it looks for a substring and returns the INDEX of the first occurrence of this substring,
# similar to index() method but safer - returns -1 if substring not found, only works with type(str)
print("Eta".find("ta"))
print("Eta".find("mma"))

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

# 2 parameter variant allows to search from a specific index
print('kappa'.find('a', 2))

# loops can be used to find multiple occurrences:
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(str(fnd) + ", ", end="")
    fnd = the_text.find('the', fnd + 1)
print()

# 3 parameter variant allow to specify the first index to disregard
print('kappa'.find('a', 1, 4))      # find 'a', starting at index 1 but disregard index 4
print('kappa'.find('a', 2, 4))      # find 'a', starting at index 2 but disregard index 4


# rfind() method: offer the same functionality as find but searches from the end of the string to the beginning
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))


# isalnum() method: checks if the string contains only digits or alphabetical characters (letters)
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

t = 'Six lambdas'                   # spaces are not alphanumeric
print(t.isalnum())
t = '&Alpha;&beta;&Gamma;&delta;'   # symbols not alphanumeric
print(t.isalnum())
t = '20E1'
print(t.isalnum())


# isalpha() method: checks if a string is letters only
print("Moooo".isalpha())
print('Mu40'.isalpha())


# isdigit(): checks if a string is all digits
print('2018'.isdigit())
print("Year2019".isdigit())


# islower() method: checks if string is all lower case
print("Moooo".islower())
print('moooo'.islower())


# isupper() method: checks if string is all upper case
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())


# isspace() method: identifies whitespace. If any other characters, returns False
print(' \n '.isspace())     # \n is classed as white space
print(" ".isspace())
print("mooo mooo mooo".isspace())


# join() method: performs a join. expects 1 arg as a list (all elems in list must be strings). all lists elems
# will be joined into a single string. the method requires a string to invoke to be used as a seperator:
print(".".join(["This", "string", "is", "joined", "by", "full", "stops"]))
print("@@".join(["This", "string", "is", "joined", "by", "two", "@", "symbols"]))
print(" ".join(["This", "string", "is", "joined", "by", "spaces"]))


# split() method: splits a string and build a list of the substrings. it assumes the substrings are delimited
# by whitespace (reverse operation is join)
print("phi       chi\npsi".split())


# lower() method: copies a string to replace all uppercase letters as lower case
print("SiGmA=60".lower())
str1 = "THIS IS ALL LOWER"
str2 = str1.lower()
print(str2)


# upper() method: copies a string to replace all lowercase letters as upper case
print("I know that I know nothing. Part 2.".upper())
str1 = "this is all upper"
str2 = str1.upper()
print(str2)


# strip() method: combines the effects of lstrip/rstrip - makes a new str removing all leading and
# trailing whitespace
print("[" + "   aleph   ".strip() + "]")


# lstrip() method: with no parameters, creates a new string and removes all the leading white space
print("[" + "      tau ".lstrip() + "]")

# with a parameter, strips all leading chars in the argument
print("www.cisco.com".lstrip("w."))
print("cccccccccccccc.cisco.com".lstrip("c."))

# only applies to the start of a string, the below arg has no effect
print("pythoninstitute.org".lstrip(".org"))


# rstrip() method: works the same as lstrip but works in reverse
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))


# replace() method: copies a string, a replaces all occurrences of first arg with second arg
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
print("replace an occurrence an of an occurrence".replace("", "!"))

# three params can be used to limit the total number of replacements
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))


# swapcase() method: swaps the case of all letter in the str
print("I know that I know nothing.".swapcase())


# title() method: capitalises the first letter of all words in string and makes all others lowercase
print("I know that I know nothing. Part 1.".title())
print("I KNOW that I kNOw noTHing. PARt 1.".title())


def mysplit(string):
    if type(string) != str:
        print("Function requires a string!")
        return None

    else:
        split_string = string.split()
        return split_string

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
print(mysplit(1243))
