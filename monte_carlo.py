import Equation as eq
import random
import functools
import argparse

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
    return getVolume() * sum([expr(*getPoint()) for _ in range(N)])/N

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='') # TODO: add description
    parser.add_argument()
    args = parser.parse_args();