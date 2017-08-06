class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def set_point(self, x, y):
        self.x = x
        self.y = y

    def get_point(self):
        return self.x, self.y

    def __add__(self, n):
        self.x += n
        self.y += n
        return self
    
    def __radd__(self, n):
        self.x += n
        self.y += n
        return self
    
    def __sub__(self, other):
        pass
    def __rsub__(self, other):
        pass
    def __mul__(self, other):
        pass
    def __rmul__(self, other):
        pass
    '/'
    def __truediv__(self, other):
        pass
    def __rtruediv__(self, other):
        pass
    '//'
    def __floordiv__(self, other):
        pass
    def __rfloordiv__(self, other):
        pass
    '%'
    def __mod__(self, other):
        pass
    def __rmod__(self, other):
        pass
    def __and__(self, other):
        pass
    def __or__(self, other):
        pass
    def __xor__(self, other):
        pass
    
    
if __name__=="__main__":
    p1 = Point(2, 2)
    p2 = p1 + 3
    #p2 = 3 + p1
    res = p2.get_point()
    print(res[0], res[1])
