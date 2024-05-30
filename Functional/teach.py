import time
# class Jar():
#     def __init__(self, cookies):
#         self.cookies = cookies
    
#     def deposit(self, amount):
#         # self.cookies += amount
#         return Jar(self.cookies + amount)

# j = Jar(5)
# amount = input("How many cookies would you like to deposit? ")
# if amount is not None:
#     j2 = j.deposit(val)
# else:

class Optional():
    def __init__(self, val):
        self.val = val
    def map(self, f):
        if self.val is not None:
            return Optional(f(self.val))
        else:
            return Optional(None)
    def get_or_else(self, default_val):
        if self.val is None:
            return default_val
        return self.val
        



def query_db():
    return 5 

def area(v):
    return v * 10

val = Optional(query_db())
val2 = val.map(lambda x: x * 2).map(area).get_or_else(50)
# print(val2)


def expensive(val):
    time.sleep(2)
    return val * 2

def exp2(val):
    time.sleep(3)
    return val * 5

# def run(f):
#     return lambda: f(5)

# expensive(5)
x = lambda: expensive(5)
# x()
# f = 5
# f = lambda x: print(x)
# f(5)
# s = exp2(expensive(5))
# o = Optional(None).map_or_else(lambda x: x, 10)
# o2 = Optional(None)

l = Lazy(lambda: 5).map(expensive).map(exp2)
l.get()

class Lazy():
    def __init__(self, lazy_val):
        self.lazy_val = lazy_val
    
    def map(self, f):
        return Lazy()



