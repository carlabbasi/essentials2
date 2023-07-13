# mod2sect4.py

# comparing strings
print('alpha' == 'alpha')   # true
print('alpha' != 'Alpha')   # true
print()

# comparing the first different character in both strings
print('alpha' < 'alphabet')     # true
print()

# String comparison is always case-sensitive (upper-case letters are taken as lesser than lower-case ones).
print('beta' > 'Beta')
print()

# string digits still not a number.
print('10' == '010')
print('10' > '010')
print('10' > '8')
print('20' < '8')
print('20' < '80')
print()

# Comparing strings against numbers is generally a bad idea.
# Can only use != which always returns True and == which always returns False.
print('10' == 10)           # always False
print('10' != 10)           # always True
print('10' != 1)            # always True
# print('10' > 10           # always gives TypeError


# sorting using sorted() function or sort() method
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)                 # sorted creates a new list and sorts them
print(first_greek)
print(first_greek_2)
print()

second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)
second_greek.sort()                                 # sort arranges the list in-situ
print(second_greek)


# number to string using str()
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)
print(si + ' ' + sf)

# string to number using int() and float(). string must represent a valid number  or ValueError is thrown
si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)
print(itg + flt)

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3)
print(s3[1])


