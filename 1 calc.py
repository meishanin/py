# WAP to make a simple calculator by using user-defined functions.

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y != 0:
        return x / y if y != 0 else "cannot divide by zero"

print('''
~~~Kakulater~~~

Select operation:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exit
''')

while True:
    choice = input("Enter choice: ")

    if choice == "5":
        print("tanks fr usin the kakulater! See u Soon!")
        break

    num1 = float(input("enter numero uno: "))
    num2 = float(input("enter numero dos: "))

    if choice == "1":
            res = add(num1, num2)
    elif choice == "2":
            res = add(num1, num2)
    elif choice == "3":
            res = mul(num1, num2)
    elif choice == "4":
            res = div(num1, num2)
    else:
        print("Invalid input!")

    print(f"Result: {res}\n")
