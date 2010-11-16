'''
Created on 2010-11-15

@author: Adrian
'''
class Formatter(object):
    def display(self, ordinal, name, solution, data, loops, averageSeconds, minimalSeconds, maximalSeconds):
        raise NotImplementedError()
    
    def displayData(self, data):
        raise NotImplementedError()