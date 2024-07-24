def get_info(age):
    def student(name):
        print(f"{name} are student")
    
    def school(name):
        print(f"{name} are school boy")
    
    if age > 18:
        return student
    return school

person_1 = get_info(age=22)
person_1("Arsen")
person_2 = get_info(age=17)
person_2("Ali")

def get_total(numbers, is_sum=True):
    def get_sum():
        pass

    def get_multiple():
        pass

