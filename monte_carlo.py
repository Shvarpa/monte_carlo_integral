import Equation as eq
import random
import functools

class Equation(eq.Expression):
    def integral(self,*args,**kwargs): return integral(self,*args,**kwargs)

def prod(*args):
    return functools.reduce(lambda x,y:x*y,args,1)

def sub(*args):
    args=list(args)
    return sum(args[:1]) - sum(args[1:])

def integral(expr, domain, seed = random.uniform, N=5000):
    getPoint = lambda : tuple(seed(*d) for d in domain)
    getVolume = lambda : prod(*[abs(sub(*d)) for d in domain])
    guess_sum = 0
    for _ in range(N):
        guess_sum+=expr(*getPoint())
    return getVolume() * guess_sum / N

if __name__ == "__main__":
    print(Equation("x^2 + y^2 + z^2 -10").integral([(-1,1),(-1,1),(-1,1)]))
