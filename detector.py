#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 09:45:15 2020

@author: Galanodel

Spyder Editor 4.1.5 included in Anaconda, conda 4.9.1, python 3.8.5

This file implement the detector (include NaI scintillator, photomultiplier
and multi-channel analyser(MCA))

"""

import func_const as fc

class Detector(object):
    def __init__(self, name='NaI scintillator', gain=5e-3, MCA_bit_depth=9,
                 MCA_max_signal=5.0, detector_resoludtion=0.075,
                 rndseed1=1, rndseed2=2, rndseed3=3):
        self._name = name
        self._gain = gain # detector gain of volt per keV
        self._MCA_bit_depth = MCA_bit_depth
        self._MCA_max_signal = MCA_max_signal
        self._detector_resolution = detector_resoludtion
            # the detector resolution at 0.662MeV is 0.075 for default
        self._source = None
        self._rnd1 = fc.rng(rndseed1) # these 3 rnds are independent random
        self._rnd2 = fc.rng(rndseed2) # number generator, for 3 diff purpose
        self._rnd3 = fc.rng(rndseed3) # of randomness rnd1 used to decide
                                      # process type rnd2, rnd3 used to
                                      # generate signal, the random seed are
                                      # assigned explicitly to make the result
                                      # reproducible, with the same
                                      # seed we get the same result

    # source description
    def info(self):
        print(self._name)
        print('thecanical details:')
        print('    Gain: {}'.format(self._gain))
        print('    MCA bit depth: {}'.format(self._MCA_bit_depth))
        print('    MCA max signal: {}'.format(self._MCA_max_signal))
        print('    Detector resolution: {}'.format(self._detector_resolution))

    # set up the source for detecting, can also be used to change source
    def setup_source(self, source):
        self._source = source

    # the random process type could be photoeletric effect or compton
    # scattering, use the therehold to decide which would happen
    def random_proces_type(self):
        rnd1 = self._rnd1.random()
        if rnd1 < self._source.therehold():
            return 'Photoelecric'
        else:
            return 'Compton'
# TODO: add other effect, background noise, backscattering, x-ray generation
# and so on
    def background_noise(self, signal):
        # this could be done by using a smooth function like b-spline,
        # but the noise recorded in the experiment gave a graph looks
        # like gamma distribution pdf, so I will probabily try gamma
        # distribution first.
        pass


    # the noise would affect the signal detection
    # to mimic the real experiment, add gaussian noise to each signal calculated
    # by theory, this would help avoid gaussian convolution and mimic the
    # real experiment easily
    # the noise is relative to the signal, so take it as a
    # parameter
    def random_noise(self, signal):
        # Note: this is going to be the noise when the detector received the
        # signal, not the background noise
        stddev = self._detector_resolution * signal / 2
        noise = self._rnd2.normal(0, stddev)
        return noise

    # generate the compton scattering signal
    def compton(self):
        # TODO: add probability for each scattering angle
        # this could be done using Klein-Nishana formula
        # see: https://demonstrations.wolfram.com/KleinNishinaFormulaForComptonEffect/
        rnd3 = self._rnd3.random()
        theta = rnd3 * 180 # the random scattering angle in degree
        E = self._source.scattered() # the photon energy from the source
                                    # scattered by aluminium block and received
                                    # by the detector
        p = fc.pdf(theta, E) # the probability of this event
        energy = fc.compton_e(theta, E) # the energy deposited in detector
        signal = energy * self._gain
        noise = self.random_noise(signal)
        signal += noise
        return signal, p

    # generate signal with noise for each signal to mimic the real signal
    def photoelectric(self):
        signal = self._source.scattered() * self._gain
        noise = self.random_noise(signal)
        signal += noise
        return signal

    # convert the signal to outcome bins
    def outcomebin(self, signal):
        number_of_bins = 2**(self._MCA_bit_depth)
        bin_number = fc.floor(number_of_bins * signal / self._MCA_max_signal)
        return bin_number

