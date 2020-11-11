#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:06:24 2020

@author: Galanodel

Spyder Editor 4.1.5 included in Anaconda, conda 4.9.1, python 3.8.5

This file implement the monte carlo simulation with the help of func_const.py
source.py and detector.py and plot the simulation date with matplotlib. So far
only Cs-137 at 20, 30, 45 degree is investigated.

"""

import source as S
import detector as D
from matplotlib import pyplot as plt

def simulation(angle, length):

    # initialise the source and detector
    source = S.Source(angle=angle)
    detector = D.Detector()

    # set up detector
    detector.setup_source(source)

    # initialise a dictionary for simulation data:
    data = dict((i,0) for i in range(2**detector._MCA_bit_depth))

    # generate and collect data
    for i in range(length):
        if detector.random_proces_type() == 'Compton':
            signal, p1 = detector.compton()
            binnumber = detector.outcomebin(signal)
            data[binnumber] += p1
        else:
             signal = detector.photoelectric()
             binnumber = detector.outcomebin(signal)
             data[binnumber] += 1/10

    # get the x, y coordinate from data and plot
    x, y = zip(*[item for item in data.items()])
    plt.figure(dpi=400)
    plt.scatter(x, y, c='r', marker='.')
    plt.ylabel('count')
    plt.xlabel('bin')
    plt.title('Cs-137 scattered at {} degrees'.format(source.set_up()))

for i in (20,30,45):
    simulation(i, 5000)
plt.show()

