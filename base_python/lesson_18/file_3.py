import datetime

borth = datetime.date(2004, 9, 10)
print(borth.strftime("%A %d. %B %Y"))
current = datetime.date(2024, 7, 25)
print(datetime.datetime.today())
print(datetime.datetime)
print(current - borth)