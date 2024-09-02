#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:53:17 2024

@author: evdokia
"""
 
import numpy as np
 
def wilsonScore(nS,n,z):
    return (nS+0.5*(z**2.0)+z*np.sqrt(nS*(n-nS)/n+0.25*(z**2.0)))/(n+(z**2.0))
 
if __name__ == "__main__":
    import sys
    if(len(sys.argv)<3):
        print("Error: Not enough arguments.", file=sys.stderr)
        print("Usage: ./getConfidenceBounds numTrials numSuccesses", file=sys.stderr)
        sys.exit(1)
    n = float(sys.argv[1])
    nS = float(sys.argv[2])
    roundDecimalPlaces = 14
    # mu(Bayes) below is the mean-estimate using Bayes' update rule
    # when the initial distribution (the prior) for the mean is taken
    # to be the uniform distribution. It should avoid NaNs arising from
    # 100% and 0% samples, and is known to approach the maximum likelihood
    # estimator (the more common estimate for the mean) for large sample
    # sizes.
    # For 100% samples, it roughly corresponds to the lower bound for the
    # 1*sigma confidence interval.
    print(" 2 sigma : "+str(round(wilsonScore(nS,n,+2.00),roundDecimalPlaces)))
    print("     95% : "+str(round(wilsonScore(nS,n,+1.96),roundDecimalPlaces)))
    print("   sigma : "+str(round(wilsonScore(nS,n,+1.00),roundDecimalPlaces)))
    print("      mu : "+str(round(wilsonScore(nS,n, 0.00),roundDecimalPlaces)))
    print("mu(Bayes): "+str(round((nS+1.0)/(n+2.0),roundDecimalPlaces)))
    print("-  sigma : "+str(round(wilsonScore(nS,n,-1.00),roundDecimalPlaces)))
    print("-    95% : "+str(round(wilsonScore(nS,n,-1.96),roundDecimalPlaces)))
    print("-2 sigma : "+str(round(wilsonScore(nS,n,-2.00),roundDecimalPlaces)))
 
# nS in the success number, n is the total number
# wilsonScore(10, 100, 1.96) upper bound
# wilsonScore(10, 100, -1.96) lower bound