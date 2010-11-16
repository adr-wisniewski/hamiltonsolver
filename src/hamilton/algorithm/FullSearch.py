from hamilton.Algorithm import Algorithm

'''
Created on 2010-11-15

@author: Adrian
'''
import sys

class FullSearch(Algorithm):
    
    def getName(self):
        return "Full Search"
    
    def solve(self, data):
        self._data = data
        self._vertices = len(data)
        self._best = (sys.float_info.max, None)
        
        #solve starting at each vertex
        for vertex in xrange(self._vertices):
            self._solveRecursive([vertex], 0)
            
        return self._best
        
    def _solveRecursive(self, accumulated_path, accumulated_cost):
        #end if path is complete
        if len(accumulated_path) == self._vertices:
            #add cycle closing egde cost
            accumulated_cost += self._data[accumulated_path[-1]][accumulated_path[0]]
            #print accumulated_path, accumulated_cost
            if accumulated_cost < self._best[0]:
                self._best = (accumulated_cost, accumulated_path)
            return
        
        #visit every already unvisited vertex and recursively repeat
        last_visited = accumulated_path[-1]
        for destination, cost in enumerate(self._data[last_visited]):
            if destination not in accumulated_path:
                self._solveRecursive(accumulated_path + [destination], accumulated_cost + cost)
        
        