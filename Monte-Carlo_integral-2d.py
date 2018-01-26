"""
=============================================================================
2d Monte-Carlo integration example
=============================================================================

Approximates an integral of a given 2d function in a 3d domain.
Computes volume under graph f(x_1,x_2) = x_3 with the Monte-Carlo method.

Erik Bostrom, Jan 19 2018
=============================================================================
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

#
# Classes
#
class funct():
    xmin = -10
    xmax = 10
    ymin = -10
    ymax = 10
    zmin = -0.25
    zmax = 1
    isol = 6.59312 # Approx. sol. from Mathematica
    volume = (xmax-xmin)*(ymax-ymin)*(zmax-zmin)
    volume_shift = (xmax-xmin)*(ymax-ymin)*(-1)*zmin
    name = "sin(r)/r (sinc), r=(x1^2+x2^2)^1/2"

    def radius(self,x1,x2):
        return np.sqrt(x1**2 + x2**2) 
    
    def surface(self,x1,x2):
        return np.sin(self.radius(x1,x2))/self.radius(x1,x2)
f = funct()

class Omega_p():
    x=list()
    y=list()
    z=list()
Op = Omega_p()

#
# Total number of points
#
N = 10**7

#
# Initialize plots
#
fig0 = plt.figure(num=1, figsize=(9, 7), dpi=60)
fig1 = plt.figure(num=2, figsize=(6, 5), dpi=60)
ax0 = fig0.gca(projection='3d')
ax1 = fig1.gca()

#
# Main loop
#
Nc  = 0
error = list()
iterations = list()
for i in xrange(0,N):
    x = (f.xmax-f.xmin)*random.uniform(0,1)+f.xmin
    y = (f.ymax-f.ymin)*random.uniform(0,1)+f.ymin
    z = (f.zmax-f.zmin)*random.uniform(0,1)+f.zmin
    
    integral = f.volume*float(Nc)/float(i+1)
    integral = integral - f.volume_shift
    
    if(z<=f.surface(x,y)):
        Nc +=1
        if(Nc%10==0):
            Op.x.append(x)
            Op.y.append(y)
            Op.z.append(z)       
    if(i%100000==0):
        err = np.abs(integral-f.isol)/f.isol
        print "i=",i,", relative error=",err
        error.append(err)
        iterations.append(i)

#
# Plotting
#
ax0.scatter(Op.x, Op.y, Op.z, marker='.', s=1, edgecolors='face',c='red')
X = np.arange(f.xmin, f.xmax, 0.1)
Y = np.arange(f.ymin, f.ymax, 0.1)
X, Y = np.meshgrid(X, Y)
Z = f.surface(X,Y)
ax0.plot_wireframe(X, Y, Z,linewidth=0.25)
ax0.set_xlim3d(f.xmin,f.xmax)
ax0.set_ylim3d(f.ymin,f.ymax)
ax0.set_zlim3d(f.zmin,f.zmax)
ax0.set(xlabel="$x_1$",ylabel="$x_2$",zlabel="$x_3=f(x_1,x_2)$")
fig0.savefig('MC_2d_sinc.png')

ax1.loglog(iterations,error,'k')
ax1.set(xlabel="iterations",ylabel="$|I_{approx}-I_{MC}|/|I_{approx}|$")
ax1.set_ylim(0.001,1)
fig1.savefig('MC_2d_sinc_error.png')
plt.show()

#
# Output
#
print ""
print "Monte-Carlo integration. Integral of " + f.name + "."
print "---------------------------------------------------"
print "Computed integral MC:",integral
print "Exact integral:",f.isol
print "Relative error:",error[-1]
print "---------------------------------------------------"
