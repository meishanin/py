# WAP to accept a string and print the number of uppercase, lowercase, and vowels by using user-defined functions

def count(string):
    uc, lc, vc = 0, 0, 0
    for i in string:
        if i.lower() in 'aeiou':
            vc += 1
        if i.isupper():
            uc += 1
        elif i.islower():
            lc += 1
    print('Uppercase:', uc)
    print('Lowercase:', lc)
    print('Vowels:', vc)


count(input('Enter a string: '))
