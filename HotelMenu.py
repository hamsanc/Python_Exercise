#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 20:52:32 2020

@author: hamcy
"""

class menu():
    def __init__(self):
        self.menu = dict()    # creates a new empty dict for each dog

    def add(self, key,value):
        self.menu[key] = value
        
    def show(self):
        print('Hamsa Prasanna Hotel Menu:')
        for k in self.menu:
            print('1 Plate ',k,' - ',self.menu[k],'Rupees')
    
    
x=menu()
x.add("idly",10)
x.add("vada",20)
x.show()
