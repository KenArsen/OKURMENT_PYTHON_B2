try:
    a = 5 
    b = 1
    c = a / b
    print(c)

except ZeroDivisionError:
    print("Sandy 0 bolgongo bolboit!")
except FileNotFoundError:
    print("File Not Found Error")
finally:
    print("Finished")