'''
Created on 2010-11-15

@author: Adrian
'''
class Algorithm(object):
    def getName(self):
        raise NotImplementedError()
    
    def solve(self, data):
        raise NotImplementedError()
    
    