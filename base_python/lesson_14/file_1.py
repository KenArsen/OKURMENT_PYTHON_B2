# set, множество, коптуктор

# set()
# {1,2,3,4,4,4,4,4}
# add() добавление
# pop() удаление
# update() обновление
# discard() уничтожение
# remove() удаление
# & кесилиши, intersection()
# | бириктируу, union()
# - кемитуу 
a = {1, 2, 3, 4, 5, 6}
b = {0, 5, 6, 7, 8, 9}
b = {0, 7, 8, 9}

# apple banana apple banana chary
# apple banana chary
# 3

# words = {i for i in input().split()}
# print(words)
# print(len(words)) # len() узундугун эсептейт

# dict()
# {key: value}
# apple banana apple banana chary
# {'apple': 2, 'banana': 2, 'chary': 1}



# apple banana apple banana chary
# apple banana chary

words = [i for i in input().split()]
set_words = set(words)
res = []
for i in set_words:
    res.append(words.count(i))
print(words)
print(set_words)
print(res)

