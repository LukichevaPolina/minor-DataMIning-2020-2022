class Fraction:
    def NOK(self, num, dev):
        return num * dev // self.Reduction(num, dev)

    def Reduction(self, num, dev):
        a, b = abs(num), abs(dev)
        while a * b != 0:
            if a > b:
                a -= b
            else:
                b -= a
        return max(a, b)

    def __init__(self, num, dev):
        # if dev == 0:
        #     yield 'Unexpected dev!'
        a = self.Reduction(num, dev)
        self.num, self.dev = num // a, dev // a

    def __add__(self, other):
        dev = self.NOK(self.dev, other.dev)
        return Fraction(dev // self.dev * self.num + dev // other.dev * other.num, dev)

    def __sub__(self, other):
        dev = self.NOK(self.dev, other.dev)
        return Fraction(dev // self.dev * self.num - dev // other.dev * other.num, dev)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.dev * other.dev)

    def __truediv__(self, other):
        return Fraction(self.num * other.dev, self.dev * other.num)

    def __eq__(self, other):
        return self.num == other.num and self.dev == other.dev

    def __ne__(self, other):
        return not (self.__eq__(other))

    def __lt__(self, other):
        dev = self.NOK(self.dev, other.dev)
        return dev // self.dev * self.num < dev // other.dev * other.num

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not (self.__le__(other))

    def __ge__(self, other):
        return not (self.__lt__(other))

    def __str__(self):
        return str(self.num) + '/' + str(self.dev)

    def __repr__(self):
        return str(self.num) + '/' + str(self.dev)


f = Fraction(456, 10)
b = Fraction(2, 5)
s = (f + b)
print(s)
s = (f - b)
print(s)
s = (f * b)
print(s)
s = (f / b)
print(s)
print(f == b)
print(f != b)
print(f < b)
print(f <= b)
print(f > b)
print(f >= b)
