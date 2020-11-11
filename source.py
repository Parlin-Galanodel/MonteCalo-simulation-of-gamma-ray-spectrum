#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 09:27:58 2020

@author: Galanodel

Spyder Editor 4.1.5 included in Anaconda, conda 4.9.1, python 3.8.5

Implement the source as a class. The source include the original gamma
ray source and the aluminium block used to scatter the gamma ray.

"""

import func_const as fc

class Source(object):
    def __init__(self, name='Cs-137', E_origin=662, angle=30):
        self._name = name   # name of the source
        self._energy = E_origin     # gamma ray energy from the source in keV
        self._set_up = angle        # scattering angle
        self._scattered = fc.compton(self._set_up, self._energy)
                                    # scattered energy by the aluminium
                                    # block, in keV
        # the therehold is determined by both source(different energy) and the
        # detector(different material). But photoelectric effect predominate
        # the low energy interactions and 1-0.72 is known for 0.662MeV(Cs-137)
        # and the probability is inverse to the cubic of the photon energy
        # see: https://ocw.mit.edu/courses/nuclear-engineering/22-55j-principles-of-radiation-interactions-fall-2004/lecture-notes/ener_depo_photon.pdf
        # see: http://www.phys.utk.edu/labs/modphys/Compton%20Scattering%20Experiment.pdf
        # so the therehold could be determined by relation
        self._therehold = 0.28 * 662**3 / self._scattered**3

    # the source description
    def info(self):
        print('Source: {}'.format(self._name))
        print('Radiation Energy: {}'.format(self._energy))
        print('Set-up angle: {} degree'.format(self._set_up))
        print('Expected Scattered Energy: {}'.format(self._scattered))

    def name(self):
        return self._name

    def origin_energy(self):
        return self._energy

    def set_up(self):
        return self._set_up

    def scattered(self):
        return self._scattered

    def therehold(self):
        # the percentage of energy transfered to electron, different for
        # different source and gamma ray photon energy
        # for Cs-137 at 0.662MeV and NaI scintillator, this is 1-72%
        return self._therehold


