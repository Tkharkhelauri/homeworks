
def decor1(func):
    def inner():
        x = func()
        return x * 4
    return inner

def decor2(func):
    def inner():
        x = func()
        return x - 10
    return inner

@decor2
@decor1
def return_num():
    return 5

print(return_num())


# result = decor(return_num)
# print(result())
