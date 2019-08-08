'''Simple objects'''

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,other):
        x_sq_dif = (self.x-other.x) **2
        y_sq_dif = (self.y-other.y) **2
        return(x_sq_dif + y_sq_dif) **.5
    def magnitude(self):
        origin = Coordinate(0,0)
        return self.distance(origin)
    def __str__(self):
        return '{},{}'.format(self.x,self.y)

class Fraction(object):
    '''Number represented as a fraction'''
    def __init__(self,numer,denom):
        'inputs must be integers'
        assert type(numer) == int and type(denom) == int
        self.numer = numer
        self.denom = denom
    def __str__(self):
        'Returns string of fraction'
        return '{}/{}'.format(self.numer,self.denom)
    def __add__(self,other):
        top = self.numer * other.denom + self.denom * other.numer
        bottom = self.denom*other.denom
        return Fraction(top,bottom)
    def __sub__(self,other):
        top = self.numer * other.denom - self.denom * other.numer
        bottom = self.denom*other.denom
        return Fraction(top,bottom)
    def __float__(self):
        return self.numer / self.denom
