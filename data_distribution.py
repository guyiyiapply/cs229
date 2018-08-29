# -*- coding: utf-8 -*-
"""
Created on Wed Jul 04 11:12:35 2018

@author: guyia
"""

from scipy.stats import binom#binomial distribution
import matplotlib.pyplot as plt
import numpy as np

n, p = 20, 0.5
x = np.arange(0, 20, 0.001)
plt.plot(x, binom.pmf(x, n, p))




from scipy.stats import norm#normal distribution
import matplotlib.pyplot as plt

value= np.arange(-3,3,0.001)
plt.plot(value,norm.pdf(value))

