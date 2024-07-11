people = {}

while True:
    print("0. Exit")
    print("1. Add person")
    print("2. Delete person")
    
    n = int(input("Select one command: "))

    if n == 0:
        break
    elif n == 1:
        name, age = [i for i in input().split()]
        people[name] = age
    elif n == 2:
        name = input()
        del people[name]
    
    for key, value in people.items():
        print(key, value)
    