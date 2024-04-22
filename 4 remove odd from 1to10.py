# WAP to generate values from 1 to 10 and then remove all the odd numbers from the list by using user-defined functions.

list = []


def generate_numbers(list):
    for i in range(1, 11):
        list.append(i)
    print("Numbers 1 to 10 generated in the list successfully!")
    return list


def remove_odd_numbers(list):
    for i in list:
        if i % 2 != 0:
            list.remove(i)
    print("Removed all odd numbers from the list successfully!")
    return list


# Generate the list of numbers from 1 to 10
print("Original list:", generate_numbers(list))

# Remove odd numbers from the list
print("New List:", remove_odd_numbers(list))
