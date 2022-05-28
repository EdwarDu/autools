#!/usr/bin/python3

import numpy as np
import scipy
from scipy.optimize import fsolve
import sys
import pickle
import os
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def solve_b(b, c1, c2, c3):
    return (np.square(np.cos(b-np.deg2rad(30))) - np.square(np.cos(b-np.deg2rad(120)))) / \
           (np.square(np.cos(b+np.deg2rad(30))) - np.square(np.cos(b-np.deg2rad(30)))) - \
           (c2-c3)/(c1-c2)


c1_v = np.loadtxt(sys.argv[1])
c2_v = np.loadtxt(sys.argv[2])
c3_v = np.loadtxt(sys.argv[3])

orig_shape = c1_v.shape

c1_v = c1_v.ravel()
c2_v = c2_v.ravel()
c3_v = c3_v.ravel()

assert(c1_v.shape == c2_v.shape == c3_v.shape)

if os.path.exists("./b_v.pickle"):
    with open("./b_v.pickle", "rb") as f_b_v:
        b_v = pickle.load(f_b_v)
else:
    print("solving")
    b_v = fsolve(solve_b, np.zeros(c1_v.shape) + 0.00000001, (c1_v, c2_v, c3_v))
    print("solved")
    with open("./b_v.pickle", "wb") as f_b_v:
        pickle.dump(b_v, file=f_b_v)

b_v = np.reshape(b_v, orig_shape)
c1_v = np.reshape(c1_v, orig_shape)
c2_v = np.reshape(c2_v, orig_shape)
c3_v = np.reshape(c3_v, orig_shape)

#print(b_array)
#print(solve_b(b_array, c1_array, c2_array, c3_array))

m_v = (c1_v - c2_v) / (np.square(np.cos(b_v + np.deg2rad(30))) - np.square(np.cos(b_v - np.deg2rad(30))))
c_v = c1_v - m_v * np.square(np.cos(b_v + np.deg2rad(30)))

# Verify
c1_diff = c1_v - c_v - m_v * np.square(np.cos(b_v + np.deg2rad(30)))
c2_diff = c2_v - c_v - m_v * np.square(np.cos(b_v - np.deg2rad(30)))
c3_diff = c3_v - c_v - m_v * np.square(np.cos(b_v - np.deg2rad(120)))

np.savetxt("m.dat", m_v)
np.savetxt("b.dat", b_v)
np.savetxt("c.dat", c_v)

#np.savetxt("c1_diff.dat", c1_diff)
#np.savetxt("c2_diff.dat", c2_diff)
#np.savetxt("c3_diff.dat", c3_diff)

o_v = m_v / (m_v + 2*c_v)


def show_fig(data: np.ndarray):
    fig = plt.figure()
    axes = fig.add_subplot(111, aspect='equal')
    hm_v = axes.imshow(data, cmap=plt.cm.rainbow)
    fig.colorbar(hm_v, ax=axes)

    height, width = data.shape
    x, y = np.meshgrid(np.arange(0, width, 1), np.arange(0, height, 1))
    unit = np.ones(data.shape) * 2
    data_deg = (data - np.min(data)) / (np.max(data) - np.min(data))*np.pi*2
    # TODO: angle function needs to be fixed
    u = unit * np.sin(data_deg)
    v = unit * np.cos(data_deg)
    axes.quiver(x, y, u, v, units='dots', scale=2, scale_units='xy', width=1, headwidth=4, headlength=6)
    fig.show()

beta = np.loadtxt('beta_data')

show_fig(b_v)
show_fig(o_v)

show_fig(beta)

plt.pause(1)
input('Enter to close')
plt.close()
