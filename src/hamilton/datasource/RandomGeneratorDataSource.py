'''
Created on 2010-11-15

@author: Adrian
'''
import random
from hamilton.DataSource import DataSource

class RandomGeneratorDataSource(DataSource):
    
    _vertices = None
    _data = None
    
    _randMin = 1
    _randMax = 99
    _randDivisor = 10.0
    
    def __init__(self, vertices):
        self._vertices = vertices
        self._initData()
        
    def _initData(self):
        self._data = []
        
        for _ in xrange(self._vertices):
            row = [random.randint(self._randMin, self._randMax) / self._randDivisor for _ in xrange(self._vertices)]
            self._data.append(row)
        
    def getData(self):
        return self._data
        