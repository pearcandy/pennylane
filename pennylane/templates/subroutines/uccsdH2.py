'''
  uccsdH2.py                                                          
                                                              
  This code is distributed under the constitution of GNU-GPL. 
  (c) PearCandy                           
                                                              
  Log of uccsdH2.py                                                   
                                                              
  2021/01/06  Released by PearCandy  
                                                              
                                                           '''
#coding:utf-8
#-------------------------------------------------------------
from pennylane import numpy as np
from pennylane.templates import template  #import the decorator
from pennylane.ops import CNOT, RX, RY, RZ, Hadamard, CZ
import pennylane as qml


@template
def UCCSDH2(weights, wires):
    # set HF state
    ref_state = [0 for i in range(len(wires))]
    for i in range(len(wires) // 2):
        ref_state[i] = 1
    qml.BasisState(np.array(ref_state), wires=wires)

    # circuit
    RX(np.pi * (1.0) / 2.0, wires=0)
    Hadamard(wires=1)
    Hadamard(wires=2)
    Hadamard(wires=3)
    CNOT(wires=[0, 1])
    CNOT(wires=[1, 2])
    CNOT(wires=[2, 3])
    RZ(weights[0], wires=3)
    CNOT(wires=[2, 3])
    CNOT(wires=[1, 2])
    CNOT(wires=[0, 1])
    RX(-np.pi * (1.0) / 2.0, wires=0)
    Hadamard(wires=1)
    Hadamard(wires=2)
    Hadamard(wires=3)
