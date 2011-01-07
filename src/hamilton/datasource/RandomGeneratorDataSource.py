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
        self._initData()

    def _initData(self):
        self._data = []
        #random.seed(0)
        for _ in xrange(self._vertices):
            row = [random.randint(self._randMin, self._randMax) / self._randDivisor for _ in xrange(self._vertices)]
            self._data.append(row)

    def getData(self):
        return self._data

    def setSeed(self,seed):
        self._seed = seed
        random.seed(self._seed)
        self._initData()
