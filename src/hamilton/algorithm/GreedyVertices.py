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
        availableVertices = [start != i for i in xrange(self._vertices)] 
        
        #construct path vertex by vertex until it's complete
        while len(path) < self._vertices:
            ##print cost, path, filter(lambda v: v[1] not in path, izip(self._data[tail], count()))
            #pick cheapest edge to vertex that has not been visited yet
            minvalue, minindex = (sys.float_info.max, None) 
            
            # find next vertex (minimize edge cost)
            for next_vertex in xrange(self._vertices):
                # skip already processed vertices
                if not availableVertices[next_vertex]:
                    continue
                
                if self._data[tail][next_vertex] < minvalue:
                    minvalue, minindex = (self._data[tail][next_vertex], next_vertex)
            
            tail = minindex
            path += [minindex]
            cost += minvalue
            availableVertices[minindex] = False
        
        #add cycle closing edge cost
        cost += self._data[tail][start]
        return (cost, path)

            
        
