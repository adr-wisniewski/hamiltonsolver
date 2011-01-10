'''
Created on 2010-11-15

@author: Adrian
'''
from hamilton.Algorithm import Algorithm

class GreedyEdges(Algorithm):
    def getName(self):
        return "Greedy Edges Search"
    
    def solve(self, data):
        data = self._enrichData(data)
        edges = self._prepareEdges(data)
        vertices = len(data)
        cost = 0
        pathEdges = []
        pathBegins = {}
        pathEnds = {}

        #pick next edge
        for edge in sorted(edges):
            
            #edge is not usable
            if not edge[0][1]:
                continue
            
            pathBefore = pathEnds.get(edge[1])      #edge extends pathBefore
            pathAfter = pathBegins.get(edge[2])     #edge prepends pathB
            
            #do not allow edge to close a cycle
            if pathBefore and pathAfter and pathBefore is pathAfter:
                continue 
            
            #path can be used
            cost += edge[0][0]
            pathEdges.append(edge) 
            
            #merge paths
            if pathBefore and pathAfter:                #pbBef-peBef -> pbAft-peAft
                del pathEnds[edge[1]]                   #pbBef       ->       peAft
                del pathBegins[edge[2]] 
                pathBefore.extend(pathAfter)
                pathEnds[pathBefore[-1]] = pathBefore   #pbBef -------------- peAft 
            elif pathBefore:                     
                del pathEnds[edge[1]]                   #pbBef-peBef -> p
                pathBefore.append(edge[2])              #pbBef -------- p
                pathEnds[edge[2]] = pathBefore   
            elif pathAfter:
                del pathBegins[edge[2]]                 #            -> pbAft-peAft
                pathAfter.insert(0, edge[1])            #          p -------- peAft
                pathBegins[edge[1]] = pathAfter
            else:
                path = [edge[1], edge[2]]               #          p -> p
                pathEnds[edge[2]] = path                #          p -- p
                pathBegins[edge[1]] = path
            
            #discard edges originating or ending 
            for vertex in xrange(vertices):
                data[edge[1]][vertex][1] = False
                data[vertex][edge[2]][1] = False           
            
            #if path is ready, break the loop
            if len(pathEdges) == vertices - 1:
                break
        
        
        #add cost of closing vertex
        _, path = pathBegins.popitem()
        cost += data[path[-1]][path[0]][0]
        
        return (cost, path)
    
    def _enrichData(self, data):
        newData = [[[item, True] for item in row] for row in data]
        return newData
    
    def _prepareEdges(self, data):
        edges = []
        
        #enumerate both rows and columns to construct list of all edges
        for source, row in enumerate(data):
            for target, item in enumerate(row):
                if target != source:
                    edges.append((item, source, target)) 
                    
        return edges