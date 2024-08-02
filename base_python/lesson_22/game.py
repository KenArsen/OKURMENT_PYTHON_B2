import random


def get_random_number(n=1, m=10):
    return random.randint(n, m)


def check(com_n, per_n):
    return com_n == per_n


def main():
    s = 1
    print("1) Set diapozo")
    n, m = map(int, input("n, m: ").split())

    comp_number = get_random_number()
    while True and s <= 3:
        person_number = int(input("Введите одно число: "))

        if check(comp_number, person_number):
            print("Siz sandy tuura taptynyz!")
            break
        else:
            print(f'{s}) ', end='')
            print("Siz sandy tuura emes taptynyz! Dagy araket kylynyz!")
            s += 1
    else:
        print(f'Computer {comp_number} degen sandy oilogon!')


main()
