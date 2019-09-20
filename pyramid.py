# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:16:40 2019

@author: lisa_
"""

symbol = input("Enter a symbol: ")
while True:
    MaxNumberOfSymbols = int(input("Enter a max number of symbol: "))
    if MaxNumberOfSymbols % 2 == 1:
        break
NumberOfSpace = (MaxNumberOfSymbols - 1) // 2
NumberOfSymbols = 1
while True:
    for i in range(NumberOfSpace):
        print(" ", end = '')
    for i in range(NumberOfSymbols):
        print(symbol, end = '')
    print("\n", end = '')
    NumberOfSpace-=1
    NumberOfSymbols+=2
    if NumberOfSymbols > MaxNumberOfSymbols:
        break