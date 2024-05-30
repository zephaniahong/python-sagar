import time


class Optional:
    def __init__(self, val) -> None:
        self.val = val

    def map(self, f):
        return Optional(f(self.val))

    def map_or_else(self, f, default):
        if not self.val:
            return Optional(default)
        return Optional(f(self.val))

    def flat_map(self, f):
        return f(self.val)

    def get_or_else(self, default):
        if not self.val:
            return default
        return self.val


class Lazy:
    def __init__(self, lazy_val):
        self.lazy_val = lazy_val
        self.val = None

    def eval(self):
        if not self.val:
            self.val = self.lazy_val()
        return self.val

    def map(self, f):
        return Lazy(lambda: f(self.lazy_val()))


# x = Optional(5).map(lambda x: x * 3)
# y = Optional(20).flat_map(lambda x: Optional(x * 5))
# print(y.get_or_else(1))
# print(x.get_or_else(10))
def expensive():
    time.sleep(3)
    return 5


l = Lazy(expensive)
l2 = l.map(lambda x: x / 2)
print(l2)
