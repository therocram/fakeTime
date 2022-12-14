# rectangularBox
# Implements the methods and functions of fakeTime.py to 
# solve for the ground state and first two excited states
# of a particle in a rectangular infinite square well.
#
# Created by Masen Pitts on 4/17/2022
# Last updated on 4/21/2022

#**************************************************#
# The parameters that the user will most commonly modify are:
#
# - a: Width of the infinite well in the x direction.
#
# - b: Width of the infinite well in the y direction.
#
# - meshRes: this gives the total number of grid points in both dimensions
#   since the configuration space region is square. The total number of
#   grid point is the SQUARE of this value (e.g. a meshRes of 100 corresponds)
#   to 10,000 total grid points. Be aware that significantly increasing
#   meshRes will likely make the algorithm unstable if dtau is not lowered
#   by an appropriate amount.
#
# - boundaryValue: this sets the boundary condition for the system.
#
# - dtau: this determines the fake time step for the algorithm.
#
# - N: this determines the total number of algorithm steps. The larger this
#   value is the more accurate the energy eignvalues will be and the longer
#   the program will run.
#
# Feel free to experiment with whatever potential energy function you
# want using the V function! Just make sure that whatever you write
# returns a calculation in terms of X and Y.
# - Some fun ones:
#       - X**2 + Y**2 - 2D quantum harmonic ossilator
#       - np.sqrt(X**2 + Y**2) - Cone shaped potential
#       - np.exp(X*Y) - Don't try this at home
#
# Note that the accuracy of data will be heavily reliant on
#   - the guess functions you define in grdGuess, excGuess1, excGuess2.
#   - the width of the infinite well and the way in which the
#     rectangular region is defined (xmin and ymin are set to zero but
#     you can work on any arbitrary range of positive and negative values).
#
# The Matplotlib 3D surface plots done at the bottom of the file are
# completely optional. Feel free to visualize and analyze the data
# however you want to. 
# The following variables returned by the algorithm contain relevant data:
#
# - grdState, excited1, excited2: numpy arrays that contain the
#   solution values for the ground state and first excited state
#   wavefunctions.
#
# - X, Y: these are the grids that should be used for plotting the 
#   wavefunctions (see the surface plots below as an example).
#
# - energyList: this contains all of the energy eigenvalues sorted from
#   lowest to highest.
#
# See Section 3 of the report for a detailed analysis of the results of
# this program's use.
#**************************************************#

import fakeTime as ft
#import numpy as np
import matplotlib.pyplot as plt

def V(X, Y):
    return 0

def grdGuess(X, Y):
    return X*(a-X)*Y*(b-Y)

def excGuess1(X, Y):
    x = X*(a-X)
    y = Y*(b-Y)*((0.5*b) - Y)
    return x*y

def excGuess2(X, Y):
    x = X*(a-X)
    y = Y*(b-Y)*((b/3.0) - Y)*((2*b/3.0) - Y)
    return x*y

xmin = 0
ymin = 0

a = 3
b = 5

meshRes = 100
boundaryValue = 0
dtau = 0.0003
N = 500

grdState, excited1, excited2, X, Y, energyList = ft.quantumSolver2D(xmin, 
                                                 a, ymin, b, meshRes, 
                                                 V, grdGuess, excGuess1, 
                                                 excGuess2, boundaryValue, 
                                                 dtau, N)

# 3D surface plots of three lowest energy eigenfunctions.
grdPlot = plt.figure()
axG = grdPlot.add_subplot(projection="3d")
axG.plot_surface(X, Y, grdState, cmap=plt.cm.plasma)
axG.set_xlim3d(0, a)
axG.set_ylim3d(0, b)
plt.title("Ground State Wavefunction")
plt.xlabel("X")
plt.ylabel("Y")

exc1Plot = plt.figure()
ax1 = exc1Plot.add_subplot(projection="3d")
ax1.plot_surface(X, Y, excited1, cmap=plt.cm.plasma)
ax1.set_xlim3d(0, a)
ax1.set_ylim3d(0, b)
plt.title("First Excited State Wavefunction")
plt.xlabel("X")
plt.ylabel("Y")

exc2Plot = plt.figure()
ax2 = exc2Plot.add_subplot(projection="3d")
ax2.plot_surface(X, Y, excited2, cmap=plt.cm.plasma)
ax2.set_xlim3d(0, a)
ax2.set_ylim3d(0, b)
plt.title("Second Excited State Wavefunction")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()