from monte_carlo import Equation, prod, sub
import matplotlib.pyplot as pyplot
import random

def integral(expr, domain, seed = random.uniform, N=1000):
    getPoint = lambda : tuple(seed(*d) for d in domain)
    getVolume = lambda : prod(*[abs(sub(*d)) for d in domain])
    guess_sum = 0
    vol = getVolume()
    xs=[]
    ys=[]
    gs=[]
    for i in range(N):
        x = getPoint()
        y = expr(*x)
        g = guess_sum = guess_sum + y
        xs.append(x)
        ys.append(y)
        gs.append(g)
    integral_guess = [vol * gs[i] / (i+1) for i in range(len(gs))]
    pyplot.subplot(1,2,1)
    pyplot.xlabel("x")
    pyplot.ylabel("y")
    pyplot.scatter(xs,ys)

    pyplot.subplot(1,2,2)
    pyplot.plot(range(N),integral_guess)
    pyplot.xlabel("הצרטיא רפסמ")
    pyplot.ylabel("שחונמ לרגטניא")
    pyplot.tight_layout()

    last_integral = vol * guess_sum / N
    print(last_integral)
    pyplot.show()
    return last_integral

integral(Equation("x^2 -2"),[(-3,3)])
