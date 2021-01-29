'''
  symmetry_preserving.py                                                          
                                                              
  This code is distributed under the constitution of GNU-GPL. 
  (c) PearCandy
                                                              
  Log of symmmetry_preserving.py                                                   
                                                              
  2021/01/06  Released by PearCandy 
                                                              
                                                           '''
#coding:utf-8
#-------------------------------------------------------------
from pennylane import numpy as np
from pennylane.templates import template  #import the decorator
from pennylane.ops import CNOT, RX, RY, RZ, Hadamard, CZ
import pennylane as qml


@template
def SymmetryPreserving(weights, wires, depth=1):
    # set HF state
    ref_state = [0 for i in range(len(wires))]
    for i in range(len(wires) // 2):
        ref_state[i] = 1
    qml.BasisState(np.array(ref_state), wires=wires)
    for d in range(depth):
        for i in range(len(wires) // 2):
            qml.CNOT(wires=[i * 2, i * 2 + 1])
            qml.RY(weights[i * 2 + (len(wires) - 1) * d] * (-1.0), wires=i * 2)
            qml.CNOT(wires=[i * 2 + 1, i * 2])
            qml.RY(weights[i * 2 + (len(wires) - 1) * d], wires=i * 2)
            qml.CNOT(wires=[i * 2, i * 2 + 1])
        for i in range(len(wires) // 2 - 1):
            qml.CNOT(wires=[i * 2 + 1, i * 2 + 2])
            qml.RY(weights[i * 2 + 1 + (len(wires) - 1) * d] * (-1.0),
                   wires=i * 2 + 1)
            qml.CNOT(wires=[i * 2 + 2, i * 2 + 1])
            qml.RY(weights[i * 2 + 1 + (len(wires) - 1) * d], wires=i * 2 + 1)
            qml.CNOT(wires=[i * 2 + 1, i * 2 + 2])
