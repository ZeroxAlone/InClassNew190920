# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:43:27 2019

@author: lisa_
"""

symbol = input("Enter a symbol: ")
while True:
    MaxNumberOfSymbols = int(input("Enter a max number of symbol: "))
    if MaxNumberOfSymbols % 2 == 1:
        break
NumberOfSpace = (MaxNumberOfSymbols - 1) // 2
NumberOfSymbols = 1
count = 0
c = 0
sc = -1
while True:
    for i in range(NumberOfSpace):
        print(" ", end = '')
    for i in range(NumberOfSymbols):
        print(symbol, end = '')
        if i == 0 and c == 0:
            print(" "*0, end = '')
        elif i == 0:
            print(" "*sc, end = '')
    c+=1
    print("\n", end = '')
    NumberOfSpace-=1
    NumberOfSymbols = 2
    count+=1
    sc+=2
    if count == 4:
        print(symbol*MaxNumberOfSymbols)
        break