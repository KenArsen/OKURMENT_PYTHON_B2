def get_list(numbers=[]):
    print(f"Numbers: {numbers}")

a = [1, 2, True, "Okurmen"]

get_list()
get_list(numbers=a)


def get_dict(people):
    for name, surname in people.items():
        print(name, surname)

b = {
    "Arsen": "Kenzhegulov",
    "Asan": "Emilbekov",
    "Uson": "Emilbekov",
}

get_dict(b)

def get_set(uniquie):
    print("Unuque:", uniquie)

c = {0,2,3,2,3,3,"Arsen", "Arsen", True, True}
get_set(uniquie=c)


def get_sum(nums):
    total_sum = 0
    for num in nums:
        total_sum += num
    print(f'Total sum = {total_sum}')

def get_multiple(nums):
    total_multiple = 1
    for num in nums:
        total_multiple *= num
    print(f'Total multiple = {total_multiple}')


d = [4,3,2,1,5,6,7,8]
get_sum(nums=d)
get_multiple(nums=d)

