"""
getattr(obj, name [, default]) — возвращает значение атрибута объекта;
hasattr(obj, name) — проверяет на наличие атрибута name в obj;
setattr(obj, name, value) — задает значение атрибута (если атрибут не существует, то он создается);
delattr(obj, name) — удаляет атрибут с именем name.
"""

"""
isinstance(object, type) -> например: isinstance(5, int)
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


obj1 = Person('John', 25)
print(getattr(obj1, "age"))
print(getattr(obj1, "name"))

print(hasattr(obj1, "gender"))

setattr(obj1, "name", "Arsen")
setattr(obj1, "gender", "male")
print(getattr(obj1, "name"))
print(getattr(obj1, "gender"))
