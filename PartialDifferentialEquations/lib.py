#!/usr/bin/env python3



import time
import copy as cp

import numpy as np
from numba import jit, njit
PI = np.pi

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  
plt.rcParams['image.cmap']='cool'  ## set a global cmap: 'cool' ,   'twilight_shifted', 'hsv', 'jet'
alpha = 0.9



def plot_2D(f,Nx,Nt, x_label = '$x$', y_label = '$t$', title='$u(t,x)$', cmap='cool'):
    
    fig, ax = plt.subplots(figsize = (8, 6))
    
    ax.imshow(f, cmap=cmap, aspect = 'auto')
    
    ax.set_xlabel(x_label, fontsize=15);
    ax.set_ylabel(y_label, fontsize=15);
    ax.set_title(title, fontsize = 20) ;
    
    ax.set_xlim(0, Nx+1)
    ax.set_ylim(0, Nt+1)
    plt.show()


def plot_3D(x,y,z, x_label = '$t$', y_label ='$x$', z_label = '$u$', title='$u(t,x)$', elev=15., azim=0, cmap = 'cool'):  
    
    fig = plt.figure( figsize = (10, 12))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap = cmap, alpha = alpha)
    ax.set_xlabel(x_label, fontsize=15);
    ax.set_ylabel(y_label, fontsize=15);
    ax.set_zlabel(z_label, fontsize=15);
    ax.set_title(title, fontsize = 20);
    ax.view_init(elev=elev, azim=azim)
        
    plt.show()
    
    
   

    
    
def plot_3D_animation(x,y,z, x_label = '$t$', y_label ='$x$', z_label = '$u$', title='$u(t,x)$'):  
       
    fig = plt.figure( figsize = (10, 12))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap = cmap, alpha = alpha)
    ax.set_xlabel(x_label, fontsize=15);
    ax.set_ylabel(y_label, fontsize=15);
    ax.set_zlabel(z_label, fontsize=15);
    ax.set_title(title, fontsize = 20);
    ax.axis('off')
   
    ## For animation: rotation 
    for ii in range(0, 360, 5):
        ax.view_init(elev=15., azim=ii)
        fig.savefig("test_%d.png" % ii)
        
        
        
        
        
        
        
        
        