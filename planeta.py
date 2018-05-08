import numpy as np
import matplotlib.pyplot as plt

m_sol = 1.989 * (10**30)
G = 6.672 * (10**-11)
UA = 1.496e+11
m_s = 24*60*60

pos_merc = [-3.894047987585573e-01, -1.332519941030263e-01, 2.437568298707685e-02]
vel_merc = [3.612905245490849e-03, -2.528088736917957e-02, -2.398028352182838e-03]
pos_earth = [-2.586676831066763e-01, 9.543469645410976e-01, -1.595083095917812e-04]
vel_earth = [-1.687252071741174e-02, -4.609551576881071e-03, -2.312777737362271e-07]
pos_jup = [-4.236440177153345e+00, -3.388942705723363e+00,  1.088146165237461e-01]
vel_jup = [4.625986351687299e-03, -5.533913700980636e-03, -8.046778631012602e-05]

for i in range(len(pos_merc)):
    pos_merc[i] = pos_merc[i]*UA
    vel_merc[i] = vel_merc[i]*(UA/m_s)
    pos_earth[i] = pos_earth[i]*UA
    vel_earth[i] = vel_earth[i]*(UA/m_s)
    pos_jup[i] = pos_jup[i]*UA
    vel_jup[i] = vel_jup[i]*(UA/m_s)

#para Mercurio
v_m = np.sqrt(vel_merc[0]**2 + vel_merc[1]**2 + vel_merc[2]**2)
r_m = np.sqrt(pos_merc[0]**2 + pos_merc[1]**2 + pos_merc[2]**2)

alpha = np.linspace(0.5, 5, 1000)
b_teo = G * m_sol
b = (v_m**2)/(r_m**(1-alpha))

prob = np.exp(-(b_teo - b)**2/(2*np.var(b)))
max_alpha = np.argmax(prob)
plt.plot(b, prob, label = 'alpha = ' + str(max_alpha))
plt.legend()
plt.savefig('planeta.pdf')
