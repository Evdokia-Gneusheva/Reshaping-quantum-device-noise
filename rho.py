#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 16:17:21 2024

@author: evdokia
"""

import boto3
from braket.circuits import Circuit, Noise, Gate, Instruction, ResultType
from braket.aws import AwsDevice
from braket.devices import LocalSimulator

from matplotlib import pyplot as plt
import numpy as np
import scipy
import string
import networkx as nx
 
from getConfidenceBounds import wilsonScore

import json

import pandas as pd

from scipy.interpolate import make_interp_spline

pi = np.pi

def remapping(listt):
    for sublist in listt:
        zero = sublist[0]
        one = sublist[1]
        two = sublist[2]
        three = sublist[3]
        four = sublist[4]
        five = sublist[5]
        sublist[4] = zero
        sublist[2] = one
        sublist[1] = two
        sublist[0] = three
        sublist[5] = four
        sublist[3] = five
        
    return listt

# 0 - 9
# 1 - 8
# 2 - 4
# 3 - 13
# 4 - 3
# 5 - 14 
# [3, 4, 8, 9, 14, 13]

# a=[[4, 2, 1, 0, 5, 3]]
# [0, 1, 2 ,3, 4, 5]
# print(remapping(a))

def list_to_bitstring_dict(counts):
    bitstring_dict = {}

    for bitlist in counts:
        # Convert the list to a bitstring
        bitstring = ''.join(map(str, bitlist))
        
        # Count the occurrences of the bitstring
        if bitstring in bitstring_dict:
            bitstring_dict[bitstring] += 1
        else:
            bitstring_dict[bitstring] = 1
    
    return bitstring_dict



############################## 15 reps 1000 shots #############################


with open('0.01 15 reps 1000 shots.json') as file:
    counts_001_15 = json.load(file)['measurements']

counts_001_15 = remapping(counts_001_15)
counts_001_15 = list_to_bitstring_dict(counts_001_15)

count0_001_15 = counts_001_15.get('000000', 0) + counts_001_15.get('000001',0)\
      + counts_001_15.get('100100',0) + counts_001_15.get('100101',0)\
      + counts_001_15.get('010110',0) + counts_001_15.get('010111',0)\
      + counts_001_15.get('001010',0) + counts_001_15.get('001011',0)
count1_001_15 = counts_001_15.get('111000',0) + counts_001_15.get('111001',0)\
      + counts_001_15.get('011100',0) + counts_001_15.get('011101',0)\
      + counts_001_15.get('101110',0) + counts_001_15.get('101111',0)\
      + counts_001_15.get('110010',0) + counts_001_15.get('110011',0)
 
rho00sim_001_15 = count0_001_15 / (count0_001_15 + count1_001_15) # out of the code space are not included
rho11sim_001_15 = count1_001_15 / (count0_001_15 + count1_001_15)
 



with open('0.328 15 reps 1000 shots.json') as file:
    counts_0328_15 = json.load(file)['measurements']

counts_0328_15 = remapping(counts_0328_15)
counts_0328_15 = list_to_bitstring_dict(counts_0328_15)

count0_0328_15 = counts_0328_15.get('000000', 0) + counts_0328_15.get('000001',0)\
      + counts_0328_15.get('100100',0) + counts_0328_15.get('100101',0)\
      + counts_0328_15.get('010110',0) + counts_0328_15.get('010111',0)\
      + counts_0328_15.get('001010',0) + counts_0328_15.get('001011',0)
count1_0328_15 = counts_0328_15.get('111000',0) + counts_0328_15.get('111001',0)\
      + counts_0328_15.get('011100',0) + counts_0328_15.get('011101',0)\
      + counts_0328_15.get('101110',0) + counts_0328_15.get('101111',0)\
      + counts_0328_15.get('110010',0) + counts_0328_15.get('110011',0)
 
rho00sim_0328_15 = count0_0328_15 / (count0_0328_15 + count1_0328_15) # out of the code space are not included
rho11sim_0328_15 = count1_0328_15 / (count0_0328_15 + count1_0328_15)
 


with open('0.647 15 reps 1000 shots.json') as file:
    counts_0647_15 = json.load(file)['measurements']

counts_0647_15 = remapping(counts_0647_15)
counts_0647_15 = list_to_bitstring_dict(counts_0647_15)

count0_0647_15 = counts_0647_15.get('000000', 0) + counts_0647_15.get('000001',0)\
      + counts_0647_15.get('100100',0) + counts_0647_15.get('100101',0)\
      + counts_0647_15.get('010110',0) + counts_0647_15.get('010111',0)\
      + counts_0647_15.get('001010',0) + counts_0647_15.get('001011',0)
count1_0647_15 = counts_0647_15.get('111000',0) + counts_0647_15.get('111001',0)\
      + counts_0647_15.get('011100',0) + counts_0647_15.get('011101',0)\
      + counts_0647_15.get('101110',0) + counts_0647_15.get('101111',0)\
      + counts_0647_15.get('110010',0) + counts_0647_15.get('110011',0)
 
rho00sim_0647_15 = count0_0647_15 / (count0_0647_15 + count1_0647_15) # out of the code space are not included
rho11sim_0647_15 = count1_0647_15 / (count0_0647_15 + count1_0647_15)



with open('0.965 15 reps 1000 shots.json') as file:
    counts_0965_15 = json.load(file)['measurements']

counts_0965_15 = remapping(counts_0965_15)
counts_0965_15 = list_to_bitstring_dict(counts_0965_15)

count0_0965_15 = counts_0965_15.get('000000', 0) + counts_0965_15.get('000001',0)\
      + counts_0965_15.get('100100',0) + counts_0965_15.get('100101',0)\
      + counts_0965_15.get('010110',0) + counts_0965_15.get('010111',0)\
      + counts_0965_15.get('001010',0) + counts_0965_15.get('001011',0)
count1_0965_15 = counts_0965_15.get('111000',0) + counts_0965_15.get('111001',0)\
      + counts_0965_15.get('011100',0) + counts_0965_15.get('011101',0)\
      + counts_0965_15.get('101110',0) + counts_0965_15.get('101111',0)\
      + counts_0965_15.get('110010',0) + counts_0965_15.get('110011',0)
 
rho00sim_0965_15 = count0_0965_15 / (count0_0965_15 + count1_0965_15) # out of the code space are not included
rho11sim_0965_15 = count1_0965_15 / (count0_0965_15 + count1_0965_15)


############################## 25 reps 1000 shots #############################

with open('0.01 25 reps 1000 shots.json') as file:
    counts_001_25 = json.load(file)['measurements']

counts_001_25 = remapping(counts_001_25)
counts_001_25 = list_to_bitstring_dict(counts_001_25)

count0_001_25 = counts_001_25.get('000000', 0) + counts_001_25.get('000001',0)\
      + counts_001_25.get('100100',0) + counts_001_25.get('100101',0)\
      + counts_001_25.get('010110',0) + counts_001_25.get('010111',0)\
      + counts_001_25.get('001010',0) + counts_001_25.get('001011',0)
count1_001_25 = counts_001_25.get('111000',0) + counts_001_25.get('111001',0)\
      + counts_001_25.get('011100',0) + counts_001_25.get('011101',0)\
      + counts_001_25.get('101110',0) + counts_001_25.get('101111',0)\
      + counts_001_25.get('110010',0) + counts_001_25.get('110011',0)
 
rho00sim_001_25 = count0_001_25 / (count0_001_25 + count1_001_25) # out of the code space are not included
rho11sim_001_25 = count1_001_25 / (count0_001_25 + count1_001_25)
 

with open('0.328 25 reps 1000 shots.json') as file:
    counts_0328_25 = json.load(file)['measurements']

counts_0328_25 = remapping(counts_0328_25)
counts_0328_25 = list_to_bitstring_dict(counts_0328_25)

count0_0328_25 = counts_0328_25.get('000000', 0) + counts_0328_25.get('000001',0)\
      + counts_0328_25.get('100100',0) + counts_0328_25.get('100101',0)\
      + counts_0328_25.get('010110',0) + counts_0328_25.get('010111',0)\
      + counts_0328_25.get('001010',0) + counts_0328_25.get('001011',0)
count1_0328_25 = counts_0328_25.get('111000',0) + counts_0328_25.get('111001',0)\
      + counts_0328_25.get('011100',0) + counts_0328_25.get('011101',0)\
      + counts_0328_25.get('101110',0) + counts_0328_25.get('101111',0)\
      + counts_0328_25.get('110010',0) + counts_0328_25.get('110011',0)
 
rho00sim_0328_25 = count0_0328_25 / (count0_0328_25 + count1_0328_25) # out of the code space are not included
rho11sim_0328_25 = count1_0328_25 / (count0_0328_25 + count1_0328_25)


with open('0.647 25 reps 1000 shots.json') as file:
    counts_0647_25 = json.load(file)['measurements']

counts_0647_25 = remapping(counts_0647_25)
counts_0647_25 = list_to_bitstring_dict(counts_0647_25)

count0_0647_25 = counts_0647_25.get('000000', 0) + counts_0647_25.get('000001',0)\
      + counts_0647_25.get('100100',0) + counts_0647_25.get('100101',0)\
      + counts_0647_25.get('010110',0) + counts_0647_25.get('010111',0)\
      + counts_0647_25.get('001010',0) + counts_0647_25.get('001011',0)
count1_0647_25 = counts_0647_25.get('111000',0) + counts_0647_25.get('111001',0)\
      + counts_0647_25.get('011100',0) + counts_0647_25.get('011101',0)\
      + counts_0647_25.get('101110',0) + counts_0647_25.get('101111',0)\
      + counts_0647_25.get('110010',0) + counts_0647_25.get('110011',0)
 
rho00sim_0647_25 = count0_0647_25 / (count0_0647_25 + count1_0647_25) # out of the code space are not included
rho11sim_0647_25 = count1_0647_25 / (count0_0647_25 + count1_0647_25)


with open('0.965 25 reps 1000 shots.json') as file:
    counts_0965_25 = json.load(file)['measurements']

counts_0965_25 = remapping(counts_0965_25)
counts_0965_25 = list_to_bitstring_dict(counts_0965_25)

count0_0965_25 = counts_0965_25.get('000000', 0) + counts_0965_25.get('000001',0)\
      + counts_0965_25.get('100100',0) + counts_0965_25.get('100101',0)\
      + counts_0965_25.get('010110',0) + counts_0965_25.get('010111',0)\
      + counts_0965_25.get('001010',0) + counts_0965_25.get('001011',0)
count1_0965_25 = counts_0965_25.get('111000',0) + counts_0965_25.get('111001',0)\
      + counts_0965_25.get('011100',0) + counts_0965_25.get('011101',0)\
      + counts_0965_25.get('101110',0) + counts_0965_25.get('101111',0)\
      + counts_0965_25.get('110010',0) + counts_0965_25.get('110011',0)
 
rho00sim_0965_25 = count0_0965_25 / (count0_0965_25 + count1_0965_25) # out of the code space are not included
rho11sim_0965_25 = count1_0965_25 / (count0_0965_25 + count1_0965_25)

############################## 35 reps 1000 shots #############################


with open('0.01 35 reps 1000 shots.json') as file:
    counts_001_35 = json.load(file)['measurements']

counts_001_35 = remapping(counts_001_35)
counts_001_35 = list_to_bitstring_dict(counts_001_35)

count0_001_35 = counts_001_35.get('000000', 0) + counts_001_35.get('000001',0)\
      + counts_001_35.get('100100',0) + counts_001_35.get('100101',0)\
      + counts_001_35.get('010110',0) + counts_001_35.get('010111',0)\
      + counts_001_35.get('001010',0) + counts_001_35.get('001011',0)
count1_001_35 = counts_001_35.get('111000',0) + counts_001_35.get('111001',0)\
      + counts_001_35.get('011100',0) + counts_001_35.get('011101',0)\
      + counts_001_35.get('101110',0) + counts_001_35.get('101111',0)\
      + counts_001_35.get('110010',0) + counts_001_35.get('110011',0)
 
rho00sim_001_35 = count0_001_35 / (count0_001_35 + count1_001_35) # out of the code space are not included
rho11sim_001_35 = count1_001_35 / (count0_001_35 + count1_001_35)
 

with open('0.328 35 reps 1000 shots.json') as file:
    counts_0328_35 = json.load(file)['measurements']

counts_0328_35 = remapping(counts_0328_35)
counts_0328_35 = list_to_bitstring_dict(counts_0328_35)

count0_0328_35 = counts_0328_35.get('000000', 0) + counts_0328_35.get('000001',0)\
      + counts_0328_35.get('100100',0) + counts_0328_35.get('100101',0)\
      + counts_0328_35.get('010110',0) + counts_0328_35.get('010111',0)\
      + counts_0328_35.get('001010',0) + counts_0328_35.get('001011',0)
count1_0328_35 = counts_0328_35.get('111000',0) + counts_0328_35.get('111001',0)\
      + counts_0328_35.get('011100',0) + counts_0328_35.get('011101',0)\
      + counts_0328_35.get('101110',0) + counts_0328_35.get('101111',0)\
      + counts_0328_35.get('110010',0) + counts_0328_35.get('110011',0)
 
rho00sim_0328_35 = count0_0328_35 / (count0_0328_35 + count1_0328_35) # out of the code space are not included
rho11sim_0328_35 = count1_0328_35 / (count0_0328_35 + count1_0328_35)


with open('0.647 35 reps 1000 shots.json') as file:
    counts_0647_35 = json.load(file)['measurements']

counts_0647_35 = remapping(counts_0647_35)
counts_0647_35 = list_to_bitstring_dict(counts_0647_35)

count0_0647_35 = counts_0647_35.get('000000', 0) + counts_0647_35.get('000001',0)\
      + counts_0647_35.get('100100',0) + counts_0647_35.get('100101',0)\
      + counts_0647_35.get('010110',0) + counts_0647_35.get('010111',0)\
      + counts_0647_35.get('001010',0) + counts_0647_35.get('001011',0)
count1_0647_35 = counts_0647_35.get('111000',0) + counts_0647_35.get('111001',0)\
      + counts_0647_35.get('011100',0) + counts_0647_35.get('011101',0)\
      + counts_0647_35.get('101110',0) + counts_0647_35.get('101111',0)\
      + counts_0647_35.get('110010',0) + counts_0647_35.get('110011',0)
 
rho00sim_0647_35 = count0_0647_35 / (count0_0647_35 + count1_0647_35) # out of the code space are not included
rho11sim_0647_35 = count1_0647_35 / (count0_0647_35 + count1_0647_35)


with open('0.965 35 reps 1000 shots.json') as file:
    counts_0965_35 = json.load(file)['measurements']

counts_0965_35 = remapping(counts_0965_35)
counts_0965_35 = list_to_bitstring_dict(counts_0965_35)

count0_0965_35 = counts_0965_35.get('000000', 0) + counts_0965_35.get('000001',0)\
      + counts_0965_35.get('100100',0) + counts_0965_35.get('100101',0)\
      + counts_0965_35.get('010110',0) + counts_0965_35.get('010111',0)\
      + counts_0965_35.get('001010',0) + counts_0965_35.get('001011',0)
count1_0965_35 = counts_0965_35.get('111000',0) + counts_0965_35.get('111001',0)\
      + counts_0965_35.get('011100',0) + counts_0965_35.get('011101',0)\
      + counts_0965_35.get('101110',0) + counts_0965_35.get('101111',0)\
      + counts_0965_35.get('110010',0) + counts_0965_35.get('110011',0)
 
rho00sim_0965_35 = count0_0965_35 / (count0_0965_35 + count1_0965_35) # out of the code space are not included
rho11sim_0965_35 = count1_0965_35 / (count0_0965_35 + count1_0965_35)



############################## 45 reps 1000 shots #############################



with open('0.01 45 reps 1000 shots.json') as file:
    counts_001_45 = json.load(file)['measurements']

counts_001_45 = remapping(counts_001_45)
counts_001_45 = list_to_bitstring_dict(counts_001_45)

count0_001_45 = counts_001_45.get('000000', 0) + counts_001_45.get('000001',0)\
      + counts_001_45.get('100100',0) + counts_001_45.get('100101',0)\
      + counts_001_45.get('010110',0) + counts_001_45.get('010111',0)\
      + counts_001_45.get('001010',0) + counts_001_45.get('001011',0)
count1_001_45 = counts_001_45.get('111000',0) + counts_001_45.get('111001',0)\
      + counts_001_45.get('011100',0) + counts_001_45.get('011101',0)\
      + counts_001_45.get('101110',0) + counts_001_45.get('101111',0)\
      + counts_001_45.get('110010',0) + counts_001_45.get('110011',0)
 
rho00sim_001_45 = count0_001_45 / (count0_001_45 + count1_001_45) # out of the code space are not included
rho11sim_001_45 = count1_001_45 / (count0_001_45 + count1_001_45)
 

with open('0.328 45 reps 1000 shots.json') as file:
    counts_0328_45 = json.load(file)['measurements']

counts_0328_45 = remapping(counts_0328_45)
counts_0328_45 = list_to_bitstring_dict(counts_0328_45)

count0_0328_45 = counts_0328_45.get('000000', 0) + counts_0328_45.get('000001',0)\
      + counts_0328_45.get('100100',0) + counts_0328_45.get('100101',0)\
      + counts_0328_45.get('010110',0) + counts_0328_45.get('010111',0)\
      + counts_0328_45.get('001010',0) + counts_0328_45.get('001011',0)
count1_0328_45 = counts_0328_45.get('111000',0) + counts_0328_45.get('111001',0)\
      + counts_0328_45.get('011100',0) + counts_0328_45.get('011101',0)\
      + counts_0328_45.get('101110',0) + counts_0328_45.get('101111',0)\
      + counts_0328_45.get('110010',0) + counts_0328_45.get('110011',0)
 
rho00sim_0328_45 = count0_0328_45 / (count0_0328_45 + count1_0328_45) # out of the code space are not included
rho11sim_0328_45 = count1_0328_45 / (count0_0328_45 + count1_0328_45)


with open('0.647 45 reps 1000 shots.json') as file:
    counts_0647_45 = json.load(file)['measurements']

counts_0647_45 = remapping(counts_0647_45)
counts_0647_45 = list_to_bitstring_dict(counts_0647_45)

count0_0647_45 = counts_0647_45.get('000000', 0) + counts_0647_45.get('000001',0)\
      + counts_0647_45.get('100100',0) + counts_0647_45.get('100101',0)\
      + counts_0647_45.get('010110',0) + counts_0647_45.get('010111',0)\
      + counts_0647_45.get('001010',0) + counts_0647_45.get('001011',0)
count1_0647_45 = counts_0647_45.get('111000',0) + counts_0647_45.get('111001',0)\
      + counts_0647_45.get('011100',0) + counts_0647_45.get('011101',0)\
      + counts_0647_45.get('101110',0) + counts_0647_45.get('101111',0)\
      + counts_0647_45.get('110010',0) + counts_0647_45.get('110011',0)
 
rho00sim_0647_45 = count0_0647_45 / (count0_0647_45 + count1_0647_45) # out of the code space are not included
rho11sim_0647_45 = count1_0647_45 / (count0_0647_45 + count1_0647_45)


with open('0.965 45 reps 1000 shots.json') as file:
    counts_0965_45 = json.load(file)['measurements']

counts_0965_45 = remapping(counts_0965_45)
counts_0965_45 = list_to_bitstring_dict(counts_0965_45)

count0_0965_45 = counts_0965_45.get('000000', 0) + counts_0965_45.get('000001',0)\
      + counts_0965_45.get('100100',0) + counts_0965_45.get('100101',0)\
      + counts_0965_45.get('010110',0) + counts_0965_45.get('010111',0)\
      + counts_0965_45.get('001010',0) + counts_0965_45.get('001011',0)
count1_0965_45 = counts_0965_45.get('111000',0) + counts_0965_45.get('111001',0)\
      + counts_0965_45.get('011100',0) + counts_0965_45.get('011101',0)\
      + counts_0965_45.get('101110',0) + counts_0965_45.get('101111',0)\
      + counts_0965_45.get('110010',0) + counts_0965_45.get('110011',0)
 
rho00sim_0965_45 = count0_0965_45 / (count0_0965_45 + count1_0965_45) # out of the code space are not included
rho11sim_0965_45 = count1_0965_45 / (count0_0965_45 + count1_0965_45)


############################## 55 reps 1000 shots #############################


with open('0.01 55 reps 1000 shots.json') as file:
    counts_001_55 = json.load(file)['measurements']

counts_001_55 = remapping(counts_001_55)
counts_001_55 = list_to_bitstring_dict(counts_001_55)

count0_001_55 = counts_001_55.get('000000', 0) + counts_001_55.get('000001',0)\
      + counts_001_55.get('100100',0) + counts_001_55.get('100101',0)\
      + counts_001_55.get('010110',0) + counts_001_55.get('010111',0)\
      + counts_001_55.get('001010',0) + counts_001_55.get('001011',0)
count1_001_55 = counts_001_55.get('111000',0) + counts_001_55.get('111001',0)\
      + counts_001_55.get('011100',0) + counts_001_55.get('011101',0)\
      + counts_001_55.get('101110',0) + counts_001_55.get('101111',0)\
      + counts_001_55.get('110010',0) + counts_001_55.get('110011',0)
 
rho00sim_001_55 = count0_001_55 / (count0_001_55 + count1_001_55) # out of the code space are not included
rho11sim_001_55 = count1_001_55 / (count0_001_55 + count1_001_55)
 

with open('0.328 55 reps 1000 shots.json') as file:
    counts_0328_55 = json.load(file)['measurements']

counts_0328_55 = remapping(counts_0328_55)
counts_0328_55 = list_to_bitstring_dict(counts_0328_55)

count0_0328_55 = counts_0328_55.get('000000', 0) + counts_0328_55.get('000001',0)\
      + counts_0328_55.get('100100',0) + counts_0328_55.get('100101',0)\
      + counts_0328_55.get('010110',0) + counts_0328_55.get('010111',0)\
      + counts_0328_55.get('001010',0) + counts_0328_55.get('001011',0)
count1_0328_55 = counts_0328_55.get('111000',0) + counts_0328_55.get('111001',0)\
      + counts_0328_55.get('011100',0) + counts_0328_55.get('011101',0)\
      + counts_0328_55.get('101110',0) + counts_0328_55.get('101111',0)\
      + counts_0328_55.get('110010',0) + counts_0328_55.get('110011',0)
 
rho00sim_0328_55 = count0_0328_55 / (count0_0328_55 + count1_0328_55) # out of the code space are not included
rho11sim_0328_55 = count1_0328_55 / (count0_0328_55 + count1_0328_55)


with open('0.647 55 reps 1000 shots.json') as file:
    counts_0647_55 = json.load(file)['measurements']

counts_0647_55 = remapping(counts_0647_55)
counts_0647_55 = list_to_bitstring_dict(counts_0647_55)

count0_0647_55 = counts_0647_55.get('000000', 0) + counts_0647_55.get('000001',0)\
      + counts_0647_55.get('100100',0) + counts_0647_55.get('100101',0)\
      + counts_0647_55.get('010110',0) + counts_0647_55.get('010111',0)\
      + counts_0647_55.get('001010',0) + counts_0647_55.get('001011',0)
count1_0647_55 = counts_0647_55.get('111000',0) + counts_0647_55.get('111001',0)\
      + counts_0647_55.get('011100',0) + counts_0647_55.get('011101',0)\
      + counts_0647_55.get('101110',0) + counts_0647_55.get('101111',0)\
      + counts_0647_55.get('110010',0) + counts_0647_55.get('110011',0)
 
rho00sim_0647_55 = count0_0647_55 / (count0_0647_55 + count1_0647_55) # out of the code space are not included
rho11sim_0647_55 = count1_0647_55 / (count0_0647_55 + count1_0647_55)


with open('0.965 55 reps 1000 shots.json') as file:
    counts_0965_55 = json.load(file)['measurements']

counts_0965_55 = remapping(counts_0965_55)
counts_0965_55 = list_to_bitstring_dict(counts_0965_55)

count0_0965_55 = counts_0965_55.get('000000', 0) + counts_0965_55.get('000001',0)\
      + counts_0965_55.get('100100',0) + counts_0965_55.get('100101',0)\
      + counts_0965_55.get('010110',0) + counts_0965_55.get('010111',0)\
      + counts_0965_55.get('001010',0) + counts_0965_55.get('001011',0)
count1_0965_55 = counts_0965_55.get('111000',0) + counts_0965_55.get('111001',0)\
      + counts_0965_55.get('011100',0) + counts_0965_55.get('011101',0)\
      + counts_0965_55.get('101110',0) + counts_0965_55.get('101111',0)\
      + counts_0965_55.get('110010',0) + counts_0965_55.get('110011',0)
 
rho00sim_0965_55 = count0_0965_55 / (count0_0965_55 + count1_0965_55) # out of the code space are not included
rho11sim_0965_55 = count1_0965_55 / (count0_0965_55 + count1_0965_55)

############################## 30 reps 1000 shots #############################


with open('0.01 30 reps 1000 shots.json') as file:
    counts_001_30 = json.load(file)['measurements']

counts_001_30 = remapping(counts_001_30)
counts_001_30 = list_to_bitstring_dict(counts_001_30)

count0_001_30 = counts_001_30.get('000000', 0) + counts_001_30.get('000001',0)\
      + counts_001_30.get('100100',0) + counts_001_30.get('100101',0)\
      + counts_001_30.get('010110',0) + counts_001_30.get('010111',0)\
      + counts_001_30.get('001010',0) + counts_001_30.get('001011',0)
count1_001_30 = counts_001_30.get('111000',0) + counts_001_30.get('111001',0)\
      + counts_001_30.get('011100',0) + counts_001_30.get('011101',0)\
      + counts_001_30.get('101110',0) + counts_001_30.get('101111',0)\
      + counts_001_30.get('110010',0) + counts_001_30.get('110011',0)
 
rho00sim_001_30 = count0_001_30 / (count0_001_30 + count1_001_30) # out of the code space are not included
rho11sim_001_30 = count1_001_30 / (count0_001_30 + count1_001_30)
 

with open('0.328 30 reps 1000 shots.json') as file:
    counts_0328_30 = json.load(file)['measurements']

counts_0328_30 = remapping(counts_0328_30)
counts_0328_30 = list_to_bitstring_dict(counts_0328_30)

count0_0328_30 = counts_0328_30.get('000000', 0) + counts_0328_30.get('000001',0)\
      + counts_0328_30.get('100100',0) + counts_0328_30.get('100101',0)\
      + counts_0328_30.get('010110',0) + counts_0328_30.get('010111',0)\
      + counts_0328_30.get('001010',0) + counts_0328_30.get('001011',0)
count1_0328_30 = counts_0328_30.get('111000',0) + counts_0328_30.get('111001',0)\
      + counts_0328_30.get('011100',0) + counts_0328_30.get('011101',0)\
      + counts_0328_30.get('101110',0) + counts_0328_30.get('101111',0)\
      + counts_0328_30.get('110010',0) + counts_0328_30.get('110011',0)
 
rho00sim_0328_30 = count0_0328_30 / (count0_0328_30 + count1_0328_30) # out of the code space are not included
rho11sim_0328_30 = count1_0328_30 / (count0_0328_30 + count1_0328_30)


with open('0.647 30 reps 1000 shots.json') as file:
    counts_0647_30 = json.load(file)['measurements']

counts_0647_30 = remapping(counts_0647_30)
counts_0647_30 = list_to_bitstring_dict(counts_0647_30)

count0_0647_30 = counts_0647_30.get('000000', 0) + counts_0647_30.get('000001',0)\
      + counts_0647_30.get('100100',0) + counts_0647_30.get('100101',0)\
      + counts_0647_30.get('010110',0) + counts_0647_30.get('010111',0)\
      + counts_0647_30.get('001010',0) + counts_0647_30.get('001011',0)
count1_0647_30 = counts_0647_30.get('111000',0) + counts_0647_30.get('111001',0)\
      + counts_0647_30.get('011100',0) + counts_0647_30.get('011101',0)\
      + counts_0647_30.get('101110',0) + counts_0647_30.get('101111',0)\
      + counts_0647_30.get('110010',0) + counts_0647_30.get('110011',0)
 
rho00sim_0647_30 = count0_0647_30 / (count0_0647_30 + count1_0647_30) # out of the code space are not included
rho11sim_0647_30 = count1_0647_30 / (count0_0647_30 + count1_0647_30)


with open('0.965 30 reps 1000 shots.json') as file:
    counts_0965_30 = json.load(file)['measurements']

counts_0965_30 = remapping(counts_0965_30)
counts_0965_30 = list_to_bitstring_dict(counts_0965_30)

count0_0965_30 = counts_0965_30.get('000000', 0) + counts_0965_30.get('000001',0)\
      + counts_0965_30.get('100100',0) + counts_0965_30.get('100101',0)\
      + counts_0965_30.get('010110',0) + counts_0965_30.get('010111',0)\
      + counts_0965_30.get('001010',0) + counts_0965_30.get('001011',0)
count1_0965_30 = counts_0965_30.get('111000',0) + counts_0965_30.get('111001',0)\
      + counts_0965_30.get('011100',0) + counts_0965_30.get('011101',0)\
      + counts_0965_30.get('101110',0) + counts_0965_30.get('101111',0)\
      + counts_0965_30.get('110010',0) + counts_0965_30.get('110011',0)
 
rho00sim_0965_30 = count0_0965_30 / (count0_0965_30 + count1_0965_30) # out of the code space are not included
rho11sim_0965_30 = count1_0965_30 / (count0_0965_30 + count1_0965_30)

############################## 20 reps 1000 shots #############################


with open('0.01 20 reps 1000 shots.json') as file:
    counts_001_20 = json.load(file)['measurements']

counts_001_20 = remapping(counts_001_20)
counts_001_20 = list_to_bitstring_dict(counts_001_20)

count0_001_20 = counts_001_20.get('000000', 0) + counts_001_20.get('000001',0)\
      + counts_001_20.get('100100',0) + counts_001_20.get('100101',0)\
      + counts_001_20.get('010110',0) + counts_001_20.get('010111',0)\
      + counts_001_20.get('001010',0) + counts_001_20.get('001011',0)
count1_001_20 = counts_001_20.get('111000',0) + counts_001_20.get('111001',0)\
      + counts_001_20.get('011100',0) + counts_001_20.get('011101',0)\
      + counts_001_20.get('101110',0) + counts_001_20.get('101111',0)\
      + counts_001_20.get('110010',0) + counts_001_20.get('110011',0)
 
rho00sim_001_20 = count0_001_20 / (count0_001_20 + count1_001_20) # out of the code space are not included
rho11sim_001_20 = count1_001_20 / (count0_001_20 + count1_001_20)
 

with open('0.328 20 reps 1000 shots.json') as file:
    counts_0328_20 = json.load(file)['measurements']

counts_0328_20 = remapping(counts_0328_20)
counts_0328_20 = list_to_bitstring_dict(counts_0328_20)

count0_0328_20 = counts_0328_20.get('000000', 0) + counts_0328_20.get('000001',0)\
      + counts_0328_20.get('100100',0) + counts_0328_20.get('100101',0)\
      + counts_0328_20.get('010110',0) + counts_0328_20.get('010111',0)\
      + counts_0328_20.get('001010',0) + counts_0328_20.get('001011',0)
count1_0328_20 = counts_0328_20.get('111000',0) + counts_0328_20.get('111001',0)\
      + counts_0328_20.get('011100',0) + counts_0328_20.get('011101',0)\
      + counts_0328_20.get('101110',0) + counts_0328_20.get('101111',0)\
      + counts_0328_20.get('110010',0) + counts_0328_20.get('110011',0)
 
rho00sim_0328_20 = count0_0328_20 / (count0_0328_20 + count1_0328_20) # out of the code space are not included
rho11sim_0328_20 = count1_0328_20 / (count0_0328_20 + count1_0328_20)


with open('0.647 20 reps 1000 shots.json') as file:
    counts_0647_20 = json.load(file)['measurements']

counts_0647_20 = remapping(counts_0647_20)
counts_0647_20 = list_to_bitstring_dict(counts_0647_20)

count0_0647_20 = counts_0647_20.get('000000', 0) + counts_0647_20.get('000001',0)\
      + counts_0647_20.get('100100',0) + counts_0647_20.get('100101',0)\
      + counts_0647_20.get('010110',0) + counts_0647_20.get('010111',0)\
      + counts_0647_20.get('001010',0) + counts_0647_20.get('001011',0)
count1_0647_20 = counts_0647_20.get('111000',0) + counts_0647_20.get('111001',0)\
      + counts_0647_20.get('011100',0) + counts_0647_20.get('011101',0)\
      + counts_0647_20.get('101110',0) + counts_0647_20.get('101111',0)\
      + counts_0647_20.get('110010',0) + counts_0647_20.get('110011',0)
 
rho00sim_0647_20 = count0_0647_20 / (count0_0647_20 + count1_0647_20) # out of the code space are not included
rho11sim_0647_20 = count1_0647_20 / (count0_0647_20 + count1_0647_20)


with open('0.965 20 reps 1000 shots.json') as file:
    counts_0965_20 = json.load(file)['measurements']

counts_0965_20 = remapping(counts_0965_20)
counts_0965_20 = list_to_bitstring_dict(counts_0965_20)

count0_0965_20 = counts_0965_20.get('000000', 0) + counts_0965_20.get('000001',0)\
      + counts_0965_20.get('100100',0) + counts_0965_20.get('100101',0)\
      + counts_0965_20.get('010110',0) + counts_0965_20.get('010111',0)\
      + counts_0965_20.get('001010',0) + counts_0965_20.get('001011',0)
count1_0965_20 = counts_0965_20.get('111000',0) + counts_0965_20.get('111001',0)\
      + counts_0965_20.get('011100',0) + counts_0965_20.get('011101',0)\
      + counts_0965_20.get('101110',0) + counts_0965_20.get('101111',0)\
      + counts_0965_20.get('110010',0) + counts_0965_20.get('110011',0)
 
rho00sim_0965_20 = count0_0965_20 / (count0_0965_20 + count1_0965_20) # out of the code space are not included
rho11sim_0965_20 = count1_0965_20 / (count0_0965_20 + count1_0965_20)

 
########################### LOWER AND UPPER BOUNDS ############################


up001_15 = wilsonScore(count0_001_15, count0_001_15 + count1_001_15, 1.96) # upper bound
low001_15 = wilsonScore(count0_001_15, count0_001_15 + count1_001_15, -1.96) # upper bound
up001_20 = wilsonScore(count0_001_20, count0_001_20 + count1_001_20, 1.96) # upper bound
low001_20 = wilsonScore(count0_001_20, count0_001_20 + count1_001_20, -1.96) # upper bound
up001_25 = wilsonScore(count0_001_25, count0_001_25 + count1_001_25, 1.96) # upper bound
low001_25 = wilsonScore(count0_001_25, count0_001_25 + count1_001_25, -1.96) # upper bound
up001_30 = wilsonScore(count0_001_30, count0_001_30 + count1_001_30, 1.96) # upper bound
low001_30 = wilsonScore(count0_001_30, count0_001_30 + count1_001_30, -1.96) # upper bound
up001_35 = wilsonScore(count0_001_35, count0_001_35 + count1_001_35, 1.96) # upper bound
low001_35 = wilsonScore(count0_001_35, count0_001_35 + count1_001_35, -1.96) # upper bound
up001_45 = wilsonScore(count0_001_45, count0_001_45 + count1_001_45, 1.96) # upper bound
low001_45 = wilsonScore(count0_001_45, count0_001_45 + count1_001_45, -1.96) # upper bound
up001_55 = wilsonScore(count0_001_55, count0_001_55 + count1_001_55, 1.96) # upper bound
low001_55 = wilsonScore(count0_001_55, count0_001_55 + count1_001_55, -1.96) # upper bound

up0328_15 = wilsonScore(count0_0328_15, count0_0328_15 + count1_0328_15, 1.96) # upper bound
low0328_15 = wilsonScore(count0_0328_15, count0_0328_15 + count1_0328_15, -1.96) # upper bound
up0328_20 = wilsonScore(count0_0328_20, count0_0328_20 + count1_0328_20, 1.96) # upper bound
low0328_20 = wilsonScore(count0_0328_20, count0_0328_20 + count1_0328_20, -1.96) # upper bound
up0328_25 = wilsonScore(count0_0328_25, count0_0328_25 + count1_0328_25, 1.96) # upper bound
low0328_25 = wilsonScore(count0_0328_25, count0_0328_25 + count1_0328_25, -1.96) # upper bound
up0328_30 = wilsonScore(count0_0328_30, count0_0328_30 + count1_0328_30, 1.96) # upper bound
low0328_30 = wilsonScore(count0_0328_30, count0_0328_30 + count1_0328_30, -1.96) # upper bound
up0328_35 = wilsonScore(count0_0328_35, count0_0328_35 + count1_0328_35, 1.96) # upper bound
low0328_35 = wilsonScore(count0_0328_35, count0_0328_35 + count1_0328_35, -1.96) # upper bound
up0328_45 = wilsonScore(count0_0328_45, count0_0328_45 + count1_0328_45, 1.96) # upper bound
low0328_45 = wilsonScore(count0_0328_45, count0_0328_45 + count1_0328_45, -1.96) # upper bound
up0328_55 = wilsonScore(count0_0328_55, count0_0328_55 + count1_0328_55, 1.96) # upper bound
low0328_55 = wilsonScore(count0_0328_55, count0_0328_55 + count1_0328_55, -1.96) # upper bound

up0647_15 = wilsonScore(count0_0647_15, count0_0647_15 + count1_0647_15, 1.96) # upper bound
low0647_15 = wilsonScore(count0_0647_15, count0_0647_15 + count1_0647_15, -1.96) # upper bound
up0647_20 = wilsonScore(count0_0647_20, count0_0647_20 + count1_0647_20, 1.96) # upper bound
low0647_20 = wilsonScore(count0_0647_20, count0_0647_20 + count1_0647_20, -1.96) # upper bound
up0647_25 = wilsonScore(count0_0647_25, count0_0647_25 + count1_0647_25, 1.96) # upper bound
low0647_25 = wilsonScore(count0_0647_25, count0_0647_25 + count1_0647_25, -1.96) # upper bound
up0647_30 = wilsonScore(count0_0647_30, count0_0647_30 + count1_0647_30, 1.96) # upper bound
low0647_30 = wilsonScore(count0_0647_30, count0_0647_30 + count1_0647_30, -1.96) # upper bound
up0647_35 = wilsonScore(count0_0647_35, count0_0647_35 + count1_0647_35, 1.96) # upper bound
low0647_35 = wilsonScore(count0_0647_35, count0_0647_35 + count1_0647_35, -1.96) # upper bound
up0647_45 = wilsonScore(count0_0647_45, count0_0647_45 + count1_0647_45, 1.96) # upper bound
low0647_45 = wilsonScore(count0_0647_45, count0_0647_45 + count1_0647_45, -1.96) # upper bound
up0647_55 = wilsonScore(count0_0647_55, count0_0647_55 + count1_0647_55, 1.96) # upper bound
low0647_55 = wilsonScore(count0_0647_55, count0_0647_55 + count1_0647_55, -1.96) # upper bound

up0965_15 = wilsonScore(count0_0965_15, count0_0965_15 + count1_0965_15, 1.96) # upper bound
low0965_15 = wilsonScore(count0_0965_15, count0_0965_15 + count1_0965_15, -1.96) # upper bound
up0965_20 = wilsonScore(count0_0965_20, count0_0965_20 + count1_0965_20, 1.96) # upper bound
low0965_20 = wilsonScore(count0_0965_20, count0_0965_20 + count1_0965_20, -1.96) # upper bound
up0965_25 = wilsonScore(count0_0965_25, count0_0965_25 + count1_0965_25, 1.96) # upper bound
low0965_25 = wilsonScore(count0_0965_25, count0_0965_25 + count1_0965_25, -1.96) # upper bound
up0965_30 = wilsonScore(count0_0965_30, count0_0965_30 + count1_0965_30, 1.96) # upper bound
low0965_30 = wilsonScore(count0_0965_30, count0_0965_30 + count1_0965_30, -1.96) # upper bound
up0965_35 = wilsonScore(count0_0965_35, count0_0965_35 + count1_0965_35, 1.96) # upper bound
low0965_35 = wilsonScore(count0_0965_35, count0_0965_35 + count1_0965_35, -1.96) # upper bound
up0965_45 = wilsonScore(count0_0965_45, count0_0965_45 + count1_0965_45, 1.96) # upper bound
low0965_45 = wilsonScore(count0_0965_45, count0_0965_45 + count1_0965_45, -1.96) # upper bound
up0965_55 = wilsonScore(count0_0965_55, count0_0965_55 + count1_0965_55, 1.96) # upper bound
low0965_55 = wilsonScore(count0_0965_55, count0_0965_55 + count1_0965_55, -1.96) # upper bound


############# NOISE SIMULATOR: BIT-FLIP, PHASE-FLIP, DEPOLARISING #############

device = LocalSimulator(backend="braket_dm")
n_shots = 1000

def remapping_SIM(dictt):
    remapped_dict = {}

    for bitstring in dictt.keys():
        zero = bitstring[0]
        one = bitstring[1]
        two = bitstring[2]
        three = bitstring[3]
        four = bitstring[4]
        five = bitstring[5]

        new_sublist = three + two + one + five + zero + four

        remapped_dict[new_sublist] = dictt[bitstring]
    
    return remapped_dict

dpl_rate_list = np.array([0.06, 0.12, 0.18, 0.24, 0.30, 0.36, 0.42, 0.48])
theta0_SIM = np.array([0.01*pi, 0.328*pi, 0.647*pi, 0.965*pi])
plt.figure(figsize=(9, 5))

for kk in range(8):
    rho00_dpl_changeTheta0 = np.zeros(4)
    
    for ii in range(4):      
        circuit = Circuit().prx(3, 0.5 * pi, 1.5 * pi)\
                            .prx(4, 0.5 * pi, 1.5 * pi)\
                            .prx(8, 0.5 * pi, 1.5 * pi)\
                            .prx(9, 0.111111111111111 * pi, 0)\
                            .prx(14, 0.5 * pi, 1.5 * pi)\
                            .cz(9, 8)\
                                .depolarizing(9, dpl_rate_list[kk])\
                                .depolarizing(8, dpl_rate_list[kk])\
                            .cz(9, 4)\
                                .depolarizing(9, dpl_rate_list[kk])\
                                .depolarizing(4, dpl_rate_list[kk])\
                            .prx(8, 0.5 * pi, 0.5 * pi)\
                            .prx(4, 0.5 * pi, 0.5 * pi)\
                            .prx(9, theta0_SIM[ii], 0.5 * pi)\
                            .cz(9, 14)\
                            .cz(13, 14)\
                            .prx(13, 0.5 * pi, 1.5 * pi)\
                            .prx(14, 0.5 * pi, 0.5 * pi)\
                            .cz(14, 13)\
                            .prx(13, 0.5 * pi, 0.5 * pi)\
                            .prx(14, 0.5 * pi, 1.5 * pi)\
                            .cz(13, 14)\
                            .prx(13, 0.5 * pi, 1.5 * pi)\
                            .prx(14, 0.5 * pi, 0.5 * pi)\
                            .cz(8, 13)\
                            .cz(8, 3)\
                            .prx(13, 0.5 * pi, 0.5 * pi)\
                            .cz(4, 3)\
                            .prx(3, 0.5 * pi, 0.5 * pi)\
                    
        
        results4 = device.run(circuit, shots=n_shots).result()
        counts4 = results4.measurement_counts
        counts4 = remapping_SIM(counts4)

        count0 = counts4.get('000000', 0) + counts4.get('000001',0)\
              + counts4.get('100100',0) + counts4.get('100101',0)\
              + counts4.get('010110',0) + counts4.get('010111',0)\
              + counts4.get('001010',0) + counts4.get('001011',0)
        count1 = counts4.get('111000',0) + counts4.get('111001',0)\
              + counts4.get('011100',0) + counts4.get('011101',0)\
              + counts4.get('101110',0) + counts4.get('101111',0)\
              + counts4.get('110010',0) + counts4.get('110011',0)
        rho00sim = count0 / (count0 + count1) 
        rho11sim = count1 / (count0 + count1) 

        rho00_dpl_changeTheta0[ii] = rho00sim

    # plt.plot(theta0_SIM, rho00_dpl_changeTheta0, '.-', color='0.8', label = 'noise')
    

################################## PLOT #######################################

theta0_values = [0.01*pi, 0.328*pi, 0.647*pi, 0.965*pi]
reps_values = [15, 20, 25, 30, 35, 45, 55]

rho00_values = {
    0.01*pi: {15: rho00sim_001_15, 20: rho00sim_001_20, 25: rho00sim_001_25, 30: rho00sim_001_30, 35: rho00sim_001_35, 45: rho00sim_001_45, 55: rho00sim_001_55},
    0.328*pi: {15: rho00sim_0328_15, 20: rho00sim_0328_20, 25: rho00sim_0328_25, 30: rho00sim_0328_30, 35: rho00sim_0328_35, 45: rho00sim_0328_45, 55: rho00sim_0328_55},
    0.647*pi: {15: rho00sim_0647_15, 20: rho00sim_0647_20, 25: rho00sim_0647_25, 30: rho00sim_0647_30, 35: rho00sim_0647_35, 45: rho00sim_0647_45, 55: rho00sim_0647_55},
    0.965*pi: {15: rho00sim_0965_15, 20: rho00sim_0965_20, 25: rho00sim_0965_25, 30: rho00sim_0965_30, 35: rho00sim_0965_35, 45: rho00sim_0965_45, 55: rho00sim_0965_55},
}

upper_bounds = {
    0.01*pi: {15: up001_15, 20: up001_20, 25: up001_25, 30: up001_30, 35: up001_35, 45: up001_45, 55: up001_55},
    0.328*pi: {15: up0328_15, 20: up0328_20, 25: up0328_25, 30: up0328_30, 35: up0328_35, 45: up0328_45, 55: up0328_55},
    0.647*pi: {15: up0647_15, 20: up0647_20, 25: up0647_25, 30: up0647_30, 35: up0647_35, 45: up0647_45, 55: up0647_55},
    0.965*pi: {15: up0965_15, 20: up0965_20, 25: up0965_25, 30: up0965_30, 35: up0965_35, 45: up0965_45, 55: up0965_55},
}

lower_bounds = {
    0.01*pi: {15: low001_15, 20: low001_20, 25: low001_25, 30: low001_30, 35: low001_35, 45: low001_45, 55: low001_55},
    0.328*pi: {15: low0328_15, 20: low0328_20, 25: low0328_25, 30: low0328_30, 35: low0328_35, 45: low0328_45, 55: low0328_55},
    0.647*pi: {15: low0647_15, 20: low0647_20, 25: low0647_25, 30: low0647_30, 35: low0647_35, 45: low0647_45, 55: low0647_55},
    0.965*pi: {15: low0965_15, 20: low0965_20, 25: low0965_25, 30: low0965_30, 35: low0965_35, 45: low0965_45, 55: low0965_55},
}

marker_styles = ['<', 'o', '^', 's', 'v', 'D', '>']

for i, reps in enumerate(reps_values):
    rho00 = [rho00_values[theta][reps] for theta in theta0_values]
    upper = [upper_bounds[theta][reps] for theta in theta0_values]
    lower = [lower_bounds[theta][reps] for theta in theta0_values]
    
    plt.errorbar(theta0_values, rho00, 
                  yerr=[np.array(rho00) - np.array(lower), np.array(upper) - np.array(rho00)],
                  fmt=marker_styles[i], label=f'{reps} repetitions')


plt.xlabel(r'$\theta_0$')
plt.ylabel(r'$\rho_{00}$')
plt.xlim((-0.1, np.pi))  
plt.ylim((0.1, 1))  
plt.title('Analytical circuit-agnostic model of Eq. (4)')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
# plt.show()

################################# ANALYTICAL MODEL ############################
from qutip import *
from qutip.measurement import measure, measurement_statistics

bf_rate_list = np.array([0.154, 0.196, 0.266, 0.588, 0.7]) # to change, keep integer multiple of 0.014
# theta0_list = np.array([0.031415926535897934, 1.0314895879286488, \
#                    2.0315632493213993, 3.03163691071415])
theta0_list = np.linspace(0, np.pi-0.1, 50)
 
for jj in range(len(bf_rate_list)):   
    p = bf_rate_list[jj]
    rho00L = np.zeros(len(theta0_list))   
    rho01Re = np.zeros(len(theta0_list))
    rho01Im = np.zeros(len(theta0_list))
    for kk in range(len(theta0_list)):
        theta0 = theta0_list[kk]
       
        
        pi = np.pi
        # For the initial state in the code space.
        phi =  1 * pi / 9
        theta = 0 #no
        alpha = np.cos(phi / 2)
        beta = -1j * np.exp(1j * theta) * np.sin(phi / 2)
        
        # physical bit-flip error rate, can change.
        # p=(1-(-2*0.014+1)**14)/2
        
        dash_styles = ['-', '--', '-.', ':', (0, (3, 5, 1, 5)), (0, (5, 10))]
        
        phi = 0
        delta = 0
        R1 = Qobj([[np.exp(1j*phi), 0],[0, np.exp(-1j*phi)]])
        R2 = Qobj([[0, -np.exp(-1j*delta)],[np.exp(1j*delta), 0]])
        R3 = Qobj([[0, np.exp(1j*phi)],[np.exp(-1j*phi), 0]])
        R4 = Qobj([[-np.exp(-1j*delta), 0],[0, np.exp(1j*delta)]])
        R5 = Qobj([[np.exp(1j*delta), 0],[0, -np.exp(-1j*delta)]])
        R6 = Qobj([[0, np.exp(-1j*phi)],[np.exp(1j*phi), 0]])
        R7 = Qobj([[0, np.exp(1j*delta)],[-np.exp(-1j*delta), 0]])
        R8 = Qobj([[np.exp(-1j*phi), 0],[0, np.exp(1j*phi)]])
       
        lphys = (alpha * basis(2,0) + beta * basis(2,1)) / np.sqrt(alpha * np.conj(alpha) + beta * np.conj(beta))
        ini_rho_phys = ket2dm(lphys)
       
        final_22_state_ana_new = (1 + p) * ((1 - p) ** 2) * ((np.cos(theta0/2)) ** 2) * R1 * ini_rho_phys * R1.dag()\
            + (2 - p) * (1 - p) * p * ((np.sin(theta0/2)) ** 2) * R2 * ini_rho_phys * R2.dag()\
                + (2 - p) * (p ** 2) * ((np.cos(theta0/2)) ** 2) * R3 * ini_rho_phys * R3.dag()\
                    + p * (1 + p) * (1 - p) * ((np.sin(theta0/2)) ** 2) * R4 * ini_rho_phys * R4.dag()\
                        + ((1 - p) ** 3) * ((np.sin(theta0/2)) ** 2) * R5 * ini_rho_phys * R5.dag()\
                            + (p ** 2) * (1 - p) * ((np.cos(theta0/2)) ** 2) * R6 * ini_rho_phys * R6.dag()\
                                + (p ** 3) * ((np.sin(theta0/2)) ** 2) * R7 * ini_rho_phys * R7.dag()\
                                + p * (1 - p) ** 2 * (np.cos(theta0/2)) ** 2 * R8 * ini_rho_phys * R8.dag()
        temp = final_22_state_ana_new.full()
        rho00L[kk] = temp[0][0]
        rho01Re[kk] = np.real(temp[0][1])
        rho01Im[kk] = np.imag(temp[0][1])
        # print(temp[0][0])
    
    plt.plot(theta0_list, rho00L, linestyle=dash_styles[jj], label=bf_rate_list[jj])

       
# plt.plot(theta0_list, rho00L, '-', label=bf_rate_list[jj])
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.show()
    
################### TABLE WITH RHO, LOWER AND UPPER BOUNDS ####################
# theta0_list = []
# reps_list = []
# rho00_list = []
# upper_bound_list = []
# lower_bound_list = []

# for theta0 in theta0_values:
#     for reps in reps_values:
#         theta0_list.append(theta0)
#         reps_list.append(reps)
#         rho00_list.append(rho00_values[theta0][reps])
#         upper_bound_list.append(upper_bounds[theta0][reps])
#         lower_bound_list.append(lower_bounds[theta0][reps])

# data = {
#     'theta0': theta0_list,
#     'reps': reps_list,
#     'Upper Bound': upper_bound_list,
#     'rho00': rho00_list,
#     'Lower Bound': lower_bound_list
# }

# df = pd.DataFrame(data)
# print(df.to_string(index=False))
