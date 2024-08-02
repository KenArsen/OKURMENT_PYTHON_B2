a = []
for i in range(10):
    a.append(i)
print(a)

a = [i for i in range(10)]

list_gen = [int(i) for i in range(10)]
set_gen = {i for i in "OkurmenOkurmen"}
dict_gen = {i: j for i, j in enumerate("Okurmen")}