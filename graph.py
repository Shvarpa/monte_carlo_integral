from monte_carlo import Equation, prod, sub
import matplotlib.pyplot as pyplot
import random
pyplot.ion()

class DynamicPlot:
    def __init__(self, updateInterval):
        self.data = {
            'x':[],
            'y':[],
            'itg':[]
        }
        self.size = 0.5
        self.counter=0
        self.updateInterval = updateInterval
        self.fig = pyplot.figure()
        self.ax1 = self.fig.add_subplot(121)
        self.ax1.scatter([],[])
        self.ax1.set_autoscaley_on(True)
        # if bounds: self.ax1.set_xlim(*bounds[0])
        pyplot.xlabel("x")
        pyplot.ylabel("y")

        self.ax2 = pyplot.subplot(122)
        self.ax2.plot([])
        pyplot.xlabel("הצרטיא רפסמ")
        pyplot.ylabel("שחונמ לרגטניא")
        pyplot.tight_layout()

    def update_plot(self,data):
        for key in data: self.data[key].append(data[key])
        self.counter+=1
        if(self.counter == self.updateInterval):
            self.replot()
            self.counter=0
        

    def replot(self):
        self.ax1.clear()
        self.ax2.clear()
        self.ax1.scatter(self.data['x'],self.data['y'],self.size)
        self.ax2.plot(self.data['itg'])
        pyplot.pause(1e-17)

        


def plot(expr, domain, seed = random.uniform, N=5000, update_intervals =100):
    getPoint = lambda : tuple(seed(*d) for d in domain)
    getVolume = lambda : prod(*[abs(sub(*d)) for d in domain])
    guess_sum = 0
    vol = getVolume()

    plot = DynamicPlot(update_intervals)
    for i in range(N):
        x = getPoint()
        y = expr(*x)
        g = guess_sum = guess_sum + y
        itg = vol * g / (i+1)
        plot.update_plot({'x':x,'y':y,'itg':itg})

    print(f"integal of {repr(expr)} between {','.join(str(d) for d in domain)} = {itg}")
    pyplot.pause(10)
plot(Equation("x^2 -2"),[(-3,3)])
