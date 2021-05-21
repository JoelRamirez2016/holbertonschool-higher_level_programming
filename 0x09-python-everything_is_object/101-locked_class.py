#!/usr/bin/python3

class LockedClass(object):
    __isfrozen = False

    def __init__(self):
        self.first_name = ""
        self.__isfrozen = True

    def __setattr__(self, key, value):
        if self.__isfrozen and not hasattr(self, key):
            raise AttributeError("'{}' object has no attribute '{}'".format(
                type(self).__name__, key))
        object.__setattr__(self, key, value)
