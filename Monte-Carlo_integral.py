"""
1d Monte-Carlo integration example.
Integral under a 1d graph.

Erik Bostrom
Jan 16 2018

"""

import numpy as np
import matplotlib.pyplot as plt
import random
import math

class funct():
    L  = np.pi
    iexact = 2
    name = "sin(x)"
    
    def curve(self,x):
        return np.sin(x)
f = funct()    

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))

N = 1000
Nc  = 0
error = np.zeros(N)

for i in range(0,N):
    x1 = f.L*random.uniform(0,1)
    x2 = random.uniform(0,1)
    integral = f.L*float(Nc)/float(i+1)
    error[i] = np.abs(integral-f.iexact)
    
    if(x2<=f.curve(x1)):
        Nc +=1
        ax0.plot(x1, x2,'r.')
    else:
        ax0.plot(x1, x2,'b.')
    ax0.set_xlim(0,f.L)
    ax0.set_ylim(0,1)
    ax0.set(xlabel="$x_1$",ylabel="$x_2=f(x_1)$")

    if(i%100==0):
        print "i=",i

print ""
print "Monte-Carlo simulation. Integral of " + f.name + "."
print "---------------------------------------------------"
print "Computed integral MC:",integral
print "Exact integral:",f.iexact
print "Error:",error[N-1]
print "---------------------------------------------------"

ax1.semilogy(np.arange(0,N),error,'k')
ax1.set(xlabel="Iter",ylabel="$|N/N_c - \pi/4|$")

plt.show()
