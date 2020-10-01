#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:44:51 2020
@author: minimal
"""
from  numpy import *
from  matplotlib.pyplot import *

n = 9000   # number of unit spaced x values on x-axis
alpha = 2.5
 # constant for the outer sum
delta = 0.00001

def f(x):
    """Main function used in inner sum"""
    return 1/x**(1/2)

# X values for ploting the x-axis
X = [x for x in range(1, n+1)]

# All of the values of 1/x^{1/2} for any given x value
series = [f(x) for x in X]

# List of all of the partial sum of 1/x^{1/2}, all put to the power of alpha at 
#every index x, S_1**alpha, S_2**alpha, S_3**alpha...
partial_sums = [sum(series[0:x+1]) for x in X]  
# It is [0:x] because the 0'th index of x is 1 since f(0) not allowed.
# then zero up til but not including x is a the first x number of terms.

# list of all of the partial sums of the 
partial_sum_expression = [1/partial_sums[x-1]**alpha for x in X]

# this is the sequence of the final sum.
final_sum = [sum(partial_sum_expression[0:x]) for x in X]
    

#(RED) Values of 1/x^{1/2} plotted over the x-axis
plot(X, series, color='red')

#(Blue) values of every partial sum of , S1, S2, S3, S4, S5
#plot(X, partial_sums, color='blue')

# Orange sum of the partial sums
plot(X, partial_sum_expression, color='orange')

# Orange sum of the partial sums
plot(X, final_sum, color='purple')

    
    

