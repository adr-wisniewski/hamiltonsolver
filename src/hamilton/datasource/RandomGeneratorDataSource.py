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
    _seed = None

    def __init__(self, vertices):
        self._vertices = vertices
        self._data = None

    def initialize(self):
        self._data = self.generateRandomData()

    def getData(self):
        return self._data
    
    def generateRandomData(self):
        data = []
        for _ in xrange(self._vertices):
            row = [random.randint(self._randMin, self._randMax) / self._randDivisor for _ in xrange(self._vertices)]
            data.append(row)
            
        return data