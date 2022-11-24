class Q:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __or__(self, q, w):
        return 1 if q + w > 0 else 0

    def __and__(self, q, w):
        return q * w

    def __not__(self, another):
        return 0 if another == 1 else 1

    def f113(self):
        return self.__or__(self.__and__(self.b, self.__not__(self.c)), (self.__not__(self.a)))
    
    def f114(self):
        return self.f113()

    def f115(self):
        return self.__or__(self.__and__(self.a, self.b), self.__and__(self.a, self.__not__(self.c)))

    def f116(self):
        return self.f115()

    def f117(self):
        return self.__or__(self.__and__(self.a, self.__not__(self.c)), self.__and__(self.__not__(self.b), self.__not__(self.c)))
    
    def f118(self):
        return self.f117()

    def f119(self):
        return self.__or__(self.__and__(self.a, self.__not__(self.c)), self.__and__(self.__and__(self.__not__(self.a), self.b), self.c))

    def f120(self):
        return self.f119()

    def f121(self):
        return self.__or__(self.__or__(self.__and__(self.__and__(self.__not__(self.a), self.b), self.c),
                                       self.__and__(self.__and__(self.__not__(self.a), self.b), self.__not__(self.c))),
                           self.__and__(self.__and__(self.__not__(self.a), self.__not__(self.b)), self.__not__(self.c)))

    def f122(self):
        return self.__or__(self.__or__(self.__and__(self.__and__(self.__not__(self.a), self.b), self.c),
                                       self.__and__(self.__and__(self.__not__(self.a), self.__not__(self.b)), self.c)),
                           self.__and__(self.__and__(self.__not__(self.a), self.__not__(self.b)), self.__not__(self.c)))

    def f123(self):
        return self.__or__(self.__or__(self.__and__(self.__and__(self.__not__(self.a), self.b), self.c),
                                       self.__and__(self.__and__(self.__not__(self.a), self.__not__(self.b)), self.c)),
                           self.__and__(self.__and__(self.a, self.__not__(self.b)), self.__not__(self.c)))


while True:
    q = Q(*[int(i) for i in input()])

    z = {113: q.f113(),
    114: q.f114(), 
    115: q.f115(), 
    116: q.f116(), 
    117: q.f117(),
    118: q.f118(),
    119: q.f119(),
    120: q.f120(),
    121: q.f121(),
    122: q.f122(),
    123: q.f123()}

    print('', z[int(input())], "\n", sep='\n', end='\n')
