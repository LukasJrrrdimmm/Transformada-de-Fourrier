import math as math
import numpy as np
import matplotlib.pyplot as plt

lim = int(200)
print(math.pi)
print(math.e)
phi = math.pi
e = math.e
#k = int(input("digite um valor para k: "))
#d = int(input("didite um denominador: "))
l2 = int(input("digite um limite: "))
x = int(-50)
pT = phi
j = complex(0, 1)
print(j)
w0 = (2*phi)/pT
#t = x/d
t0 = 2*(-lim)
v1 = [-lim]*lim
v2 = [-lim]*lim
v3 = [-lim]*lim
ve = [-lim]*lim
vf = [-lim]*lim
si = [-lim]*lim
ff = [-lim]*lim
f2 = [-lim]*lim
while x<lim:
    ff[x] = [2/(phi**2) + sum((4*phi*(n**2))*math.cos(n*x) for n in range(1, l2))]


    v3[x] = [1/5 +(sum((2/(n*phi**2))*(math.sin(n*phi/5)*math.cos(n*phi*x/5)
        - (2/(n*phi**2))*math.cos(n*phi/5)*math.sin(n*phi*x/5)) for n in range(1, l2)))]


    if x == 0:
        #ve[x] = [1/5]
        ve[x] = [2*phi**2]
        v2[x] = [0]
        vf[x] = [0]
        f2[x] = [0]
    else:
        #ve[x] = [x/(50*phi)*math.sin(x*phi**2/5)]
        ve[x] = [(1/(x**2))*math.cos(x*phi)]
        #v2[x] = [(1/(x**2))*math.cos(x*phi)]
        vf[x] = [-x/(50*phi)*math.cos(x/5*phi**2)]
        vf[x] = [0]
        f2[x] = [0]

    x = x + 1
plt.plot(v1, 'g')
plt.plot(ve,'*')
plt.plot(si, 'brown')
plt.plot(f2, 'brown')
plt.plot(vf, '*')
plt.plot(v2, 'b')
plt.plot(v3, 'brown')
plt.plot(ff, 'k')
plt.plot(f2, 'brown')
plt.show()
