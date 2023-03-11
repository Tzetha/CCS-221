import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from scipy.spatial import Delaunay

import tensorflow as tf


center_x = 0
center_y = 0
radius = 10
height_z = 20

def _plt_basic_object_(points):
    tri=Delaunay(points).convex_hull
    fig=plt.figure(figsize=(8,8))
    ax=fig.add_subplot(111, projection='3d')
    S=ax.plot_trisurf(points[:,0], points[:,1], points[:, 2], triangles=tri, shade=True, cmap=cm.binary,lw=0.5)

    ax.set_xlim3d(-5,5)
    ax.set_ylim3d(-5,5)
    ax.set_zlim3d(-5,5)
    plt.show()

def _cube_(bottom_lower=(0, 0, 0), side_length=5):
    bottom_lower = np.array(bottom_lower)
    points = np.vstack([
        bottom_lower,
        bottom_lower + [-1, -1, -1],
        bottom_lower + [1, -1, -1],
        bottom_lower + [1, 1, -1],
        bottom_lower + [-1, 1, -1], 
        bottom_lower + [0, 0, 1],
       
    ])
    return points

def sphere():
 ax = plt.axes(projection = "3d")

 u = np.linspace(0, 2*np.pi,100)
 v = np.linspace(0, np.pi, 100)
 r = 10

 x = r * np.outer(np.cos(u), np.sin(v))
 y = r * np.outer(np.sin(u), np.sin(v))
 z = r * np.outer(np.ones(np.size(u)), np.cos(v))

 ax.plot_surface(x,y,z, rstride = 5, cstride = 5)
 plt.show()

def _heart_(bottom_center = (0, 0, 0)):
    bottom_center = np.array(bottom_center)
    points = np.vstack([
        bottom_center + [+1.5, -1, +3.5],
        bottom_center + [+1.5, +1, +3.5],
        bottom_center + [-1.5, -1, +3.5],
        bottom_center + [-1.5, +1, +3.5],        
        bottom_center + [0, +1, +2],
        bottom_center + [0, -1, +2],
        bottom_center + [+3, 0, +2],
        bottom_center + [-3, 0, +2],
        bottom_center + [0, 1, -2],
        bottom_center + [0, -1, -2]
    ])
    return points

init_heart = _heart_(bottom_center=(0,0,0))
points_heart = tf.constant(init_heart, dtype=tf.float32)
counter = 2
_plt_basic_object_(init_heart, counter)
 
    
def main():
    init_cube_ = _cube_(side_length=3)
    points = tf.constant(init_cube_, dtype=tf.float32)

    _plt_basic_object_(init_cube_)
    sphere()  


if __name__ == '__main__':
    main()
