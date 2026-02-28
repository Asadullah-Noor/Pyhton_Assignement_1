def outer():
    def inner():
        print("This is the inner function.")
    inner()
outer()