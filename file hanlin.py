def write():
    name = input("Enter name: ")
    f = open("cricket.txt", "w")
    f.write(name+"\n")
    print(name,"has been added to the file.")

def read():
    f = open("cricket.txt", "r")
    print("Player Names:")
    g = f.readlines()
    for i in g:
        print((g.index(i)+1),':',i)
    f.close()

def append():
    name = input("Enter name: ")
    f = open("cricket.txt", "a")
    f.write(name+"\n")
    print(name,"has been added to the file.")
    
while True:
    print("1. Write player name to file")
    print("2. Read player details from file")
    print("3. Append player details to file")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        write()
    elif choice == "2":
        read()
    elif choice == "3":
        append()
    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")

