msg = [1, 2, 3, [9, 6, 4], True, "Okurmen", ["Bishkek", "Naryn"]]
#      0  1  2      3       4       5              6
print(msg[0])
print(msg[6])
print(msg[6][0])
print(msg[6][1])

# 3 -> [9, 6, 4]
print(msg[3][0] + msg[3][1] + msg[3][2])


list_1 = ["One", "Two", ["Three", ["Four", "Five"], "Six"], "Seven"]
#                                   0        1
#                         0              1            2
#          0       1                2                          3
# Five
# Six
# Seven
print(list_1[2][1][1])
print(list_1[2][2])
print(list_1[3])