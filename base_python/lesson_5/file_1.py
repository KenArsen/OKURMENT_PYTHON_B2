text = "Okurmen"
# O   k  u  r  m  e  n
# 0   1  2  3  4  5  6 
# -7 -6 -5 -4 -3 -2 -1

print(text[-7])
print(text[0] + text[-1])
print(text[0] > text[-1])

# [start:end:step]
# [башы:аягы:кадамы]

print(text[2:5])
print(text[0:7:2])
print(text[2:])
print(text[:5])
print(text[:5:2])
print(text[::])
print(text[-6:-2])
print(text[-2:-6:-1])
print(text[-5:0:-1])