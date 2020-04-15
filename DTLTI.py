#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:08:41 2020

@author: krish
"""
import numpy
import matplotlib.pyplot

r_n = lambda n: n * (n>0)
u_n = lambda n: numpy.heaviside(n,1)
h_eq = lambda n: ((u_n(n) * numpy.e ** (-0.1 * n)) + r_n(n) + r_n(n - 6) - 2 * r_n(n - 3) + u_n(n - 2) - u_n(n - 5))
t = numpy.arange(0, 11, 1)
f = numpy.convolve(u_n(t), h_eq(t))
print(numpy.round(f[: max(t) + 1],2))
matplotlib.pyplot.stem(t, f[:11], linefmt="k", markerfmt="k.", basefmt="k")
matplotlib.pyplot.xlabel("n")
matplotlib.pyplot.ylabel("x[n] * h_eq[n]")
matplotlib.pyplot.show()








