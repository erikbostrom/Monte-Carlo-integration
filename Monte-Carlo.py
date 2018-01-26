"""
=============================================================================
1d Monte-Carlo integration example
=============================================================================

Area of square [0,1]x[0,1] is 1
Area of circle quadrant with radius 1 is equal to the probability a random 
point (x_1,x_2) ~ U([0,1]x[0,1]) is located inside the quadrant.

Erik Bostrom
Jan 16 2018
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import math

def eucl_dist(x1,x2):
    return np.sqrt(x1**2 + x2**2)


plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))


N = 20000
Nc  = 0
error = np.zeros(N)

for i in range(0,N):
    x1 = random.uniform(0,1)
    x2 = random.uniform(0,1)
    d  = eucl_dist(x1,x2)
    area = float(Nc)/float(i+1)
    error[i] = np.abs(area-math.pi/4)
    
    if(d<=1):
        Nc +=1
        ax0.plot(x1, x2,'r.')
    else:
        ax0.plot(x1, x2,'b.')
    ax0.axis('square')
    ax0.set(xlabel="$x_1$",ylabel="$x_2$")
            


    if(i%100==0):
        print "i=",i,d,area

print "Computed area MC:",area
print "Exact area:",math.pi/4
print "Error:",error[N-1]

ax1.semilogy(np.arange(0,N),error,'k')
ax1.set(xlabel="Iter",ylabel="$|N/N_c - \pi/4|$")

plt.show()
