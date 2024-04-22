# WAP to check whether a number is even or odd by using user-defined functions

def OddOrEven(number):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")


while True:
    num = input('enter a number: ')
    if num == 'exit':
        print('tanks')
        break
    else:
        OddOrEven(int(num))
