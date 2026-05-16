#!/usr/bin/env python3
""" Abstract class for fishing """


class Fish():
    """represent a fish"""
    def swim(self):
        print("The fish is swimming")
    
    def habitat(self):
        print("The fish lives in water")
    

class Bird():
    """represent a bird"""
    def fly(self):
        print("The bird is flying")
    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """represent a flying fish """
    def fly(self):
        print("The flying fish is soaring!")
    def swim(self):
        print("The flying fish is swimming!")
    def habitat(self):
        print("The flying fish lives both in water and the sky!")
