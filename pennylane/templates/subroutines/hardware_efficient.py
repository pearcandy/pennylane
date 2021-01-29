'''
  hardware_efficient.py                                                          
                                                              
  This code is distributed under the constitution of GNU-GPL. 
  (c) PearCandy                              
                                                              
  Log of hardware_efficient                                                   
                                                              
  2021/01/06  Released by PearCandy                       
                                                              
                                                           '''
#coding:utf-8
#-------------------------------------------------------------
from pennylane import numpy as np
from pennylane.templates import template  #import the decorator
from pennylane.ops import CNOT, RX, RY, RZ, Hadamard, CZ


@template
def HardwareEfficient(weights, wires, depth=1):
    for d in range(depth):
        for i in range(len(wires)):
            RY(weights[2 * i + 2 * len(wires) * d], wires=i)
            RZ(weights[2 * i + 1 + 2 * len(wires) * d], wires=i)
        for i in range(len(wires) // 2):
            CZ(wires=[2 * i, 2 * i + 1])
        for i in range(len(wires) // 2 - 1):
            CZ(wires=[2 * i + 1, 2 * i + 2])
    for i in range(len(wires)):
        RY(weights[2 * i + 2 * len(wires) * depth], wires=i)
        RZ(weights[2 * i + 1 + 2 * len(wires) * depth], wires=i)
