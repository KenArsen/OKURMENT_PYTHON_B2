def get_info(func):
    def wrapper():
        print("Starting")
        func()
        print("Finished")
    return wrapper

@get_info
def fun():
    print("Okurmen")

# fun = get_info(fun)
fun()


