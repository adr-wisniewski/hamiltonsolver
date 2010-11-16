'''
Created on 2010-11-15

@author: Adrian
'''
import sys
from hamilton.Algorithm import Algorithm
from itertools import count, izip 

class GreedyVertices(Algorithm):
    def getName(self):
        return "Greedy Vertices Search"
    
    def solve(self, data):
        self._data = data
        self._vertices = len(data)
        self._best = (sys.float_info.max, None)
        
        #start at each vertex
        for vertex in xrange(self._vertices):
            solution = self._solveFromVertex(vertex)
            
            if solution[0] < self._best[0]:
                self._best = solution
            
        return self._best
    
    def _solveFromVertex(self, start):
        tail = start
        path = [start]
        cost = 0
        
        #construct path vertex by vertex until it's complete
        while len(path) < self._vertices:
            ##print cost, path, filter(lambda v: v[1] not in path, izip(self._data[tail], count()))
            #pick cheapest edge to vertex that has not been visited yet
            minvalue, minindex = min(filter(lambda v: v[1] not in path, izip(self._data[tail], count())))
            tail = minindex
            path += [minindex]
            cost += minvalue
        
        #add cycle closing edge cost
        cost += self._data[tail][start]
        return (cost, path)

            
        
