from monte_carlo import Equation, prod, sub
import numpy as np
import matplotlib.pyplot as pyplot
import matplotlib.animation as animation
import random

pyplot.style.use('grayscale')

def plot(expr, domain, seed = random.uniform, N=5000):

    fig, (ax1, ax2) = pyplot.subplots(1,2)
    ax1.set_title(repr(expr))
    ax2.set_title(f"integral of {repr(expr)} between {','.join(str(d) for d in domain)}")
    fun = ax1.scatter([],[],s=0.1,animated = True)
    monte, = ax2.plot([],animated = True)

    data = {'x':[],'y':[],'i':[],'itg':[]}
    doms = {'x':domain[0],'y':(-1,1),'i':(0,10),'itg':(-1,1)}
    def update_dom(dom,dat,dom_update=np.exp(0.5)):
        if(dat<doms[dom][0]): doms[dom] = (dom_update*dat,doms[dom][1])
        elif(doms[dom][1]<dat): doms[dom] = (doms[dom][0],dom_update*dat)
        else: return
        update_dom_fig(dom)
    def update_dom_fig(dom):
        {
            'x':   lambda: ax1.set_xlim(*doms[dom]),
            'y':   lambda: ax1.set_ylim(*doms[dom]),
            'i':   lambda: ax2.set_xlim(*doms[dom]),
            'itg': lambda: ax2.set_ylim(*doms[dom])
        }[dom]()
        {
            'y':lambda: ax1.figure.canvas.draw(),
            'x': lambda: ax1.figure.canvas.draw(),
            'i':lambda: ax2.figure.canvas.draw(),
            'itg': lambda: ax2.figure.canvas.draw()
        }[dom]()
        
    def init():
        for k in doms: update_dom_fig(k)
        return fun, monte

    def update(frame):
        for key in frame: data[key].append(frame[key]) 
        for key in frame: update_dom(key,frame[key])
        fun.set_offsets(np.c_[data['x'],data['y']])
        monte.set_data(data['i'],data['itg'])
        return fun, monte

    def frames_gen():
        getPoint = lambda : tuple(seed(*d) for d in domain)
        getVolume = lambda : prod(*[abs(sub(*d)) for d in domain])
        guess_sum = 0
        vol = getVolume()
        for i in range(N):
            x = getPoint()
            y = expr(*x)
            g = guess_sum = guess_sum + y
            itg = vol * g / (i+1)
            yield {'x':x[0],'y':y,'i':i,'itg':itg}
        
        print(f"integal of {repr(expr)} between {','.join(str(d) for d in domain)} = {itg}")
    
    ani = animation.FuncAnimation(fig, update, frames_gen, blit=True, init_func=init,interval=1,repeat=False)
    pyplot.show()

if __name__=="__main__":
    plot(Equation("x^2 -2"),[(-3,3)])
