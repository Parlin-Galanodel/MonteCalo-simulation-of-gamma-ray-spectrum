#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:52:21 2020

@author: Galanodel

Spyder Editor 4.1.5 included in Anaconda, conda 4.9.1, python 3.8.5

This file contains the essential constants and functons will be used

"""

# the esstential libraries and constants:
import numpy as np
from scipy import integrate as it
from scipy import constants as cons

# the default random number generator
rng = np.random.default_rng

# rename the pi as captial to indicate it is constant
PI = cons.pi

# trig function would be used
cos = np.cos
sin = np.sin

# fine structure constant
a = cons.fine_structure

# hbar
hbar = cons.hbar

# speed of light
c = cons.c

# electron mass
m = cons.m_e

# the rest mass energy of electron is 511 keV
M_e = 511

#floor function in numpy
floor = np.floor

# The compton scattering function
def compton(theta, E=662):
    theta = theta / 180 * PI # convert degree to radian
    scattered = E / (1 + E/M_e * (1 - cos(theta)))
    return scattered

# The energy transfered to the electron after scattering
def compton_e(theta, E=662):
    e_K = E - compton(theta, E)
    return e_K

# Klein-Nishina formula
# this formula is related to the probability of each scattered angle
# but it is not normalized
def kn(theta, E=662):
    theta = theta / 180 * PI
    ratio = 1 / (1 + E/M_e * (1 - cos(theta)))
    return 0.5 * a**2 * (hbar/c/m)**2 * ratio**2 * (ratio + 1/ratio -
                                                    (sin(theta))**2)

# normalization constant
# with this constant the pdf correspond to kn func is (1 / rou[0] * kn)
def rou(E=662):
    def kn2(theta):
        return kn(theta, E)
    rou = it.quad(kn2, 0, PI)
    return rou

r = rou()[0]

# the pdf
def pdf(theta, E=662):
    return 1/r * kn(theta,E)

