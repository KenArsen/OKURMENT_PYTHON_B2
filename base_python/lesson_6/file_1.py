# String.upper()
# String.lower()
# String.find()
# String.index()
# String.count()
# String.strip()
# String.rstrip()
# String.lstrip()
# String.replace()
# String.isalpha()
# String.isdigit()

text = "How do YOU DO?"
text_upper = text.upper()
print(text_upper)


text = "Bishkek, Naryn, Talas"
text_lower = text.lower()
print(text_lower)


text = "Okurmen is coolO"
text_find = text.find("men")
print(text_find)


text = "I am fine"
text_index = text.index("fine")
print(text_index)


text = "How do you do?"
text_count = text.count("d")
print(text_count)

text = "     Bsihkek Talas         "
text_strip = text.strip()
text_rstrip = text.rstrip()
text_lstrip = text.lstrip()
print(text)
print(text_strip)
print(text_rstrip)
print(text_lstrip)


text = "Kyrgyzstan is very beautiful!"
text_replace_1 = text.replace("Kyrgyzstan", "Kazakstan")
print(text_replace_1)
text_replace = text.replace("beautiful", "nice")
print(text_replace)


text = "IamfromKyrgyzstan"
text_isalpha = text.isalpha()
print(text_isalpha)


text = "1245345"
text_isdigit = text.isdigit()
print(text_isdigit)

