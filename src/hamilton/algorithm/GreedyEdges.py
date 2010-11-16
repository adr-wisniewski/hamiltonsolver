'''
Created on 2010-11-15

@author: Adrian
'''
from hamilton.Algorithm import Algorithm

class GreedyEdges(Algorithm):
    def getName(self):
        return "Greedy Edges Search"
    
    def solve(self, data):
        vertices = len(data)
        edges = self._prepareEdges(data)
        cost = 0
        pathEdges = []
        pathBegins = {}
        pathEnds = {}

        #pick next edge
        for edge in sorted(edges):
            
            #path already has edge originating from or pointing to same vertex
            for pathEdge in pathEdges:
                if edge[1] == pathEdge[1] or edge[2] == pathEdge[2]:
                    break
            else:
                pathA = pathEnds.get(edge[1])       #edge extends pathA
                pathB = pathBegins.get(edge[2])     #edge prepends pathB
                
                #do not allow edge to close a cycle
                if pathA and pathB and pathA is pathB:
                    continue 
                
                #path can be used
                cost += edge[0]
                pathEdges.append(edge) 
                
                #merge paths
                if pathA and pathB:             #pbA-peA -> pbB-peB
                    del pathEnds[edge[1]]       #pbA     ->     peB
                    del pathBegins[edge[2]] 
                    pathA.extend(pathB)
                    pathEnds[pathB[-1]] = pathA #pbA ---------- peA 
                elif pathA:                     
                    del pathEnds[edge[1]]       #pbA-peA ->
                    pathA.append(edge[2])       #pbA ------ peA
                    pathEnds[edge[2]] = pathA   
                elif pathB:
                    del pathBegins[edge[2]]     #        -> pbB-peB
                    pathB.insert(0, edge[1])    #    pbB ------ peB
                    pathBegins[edge[1]] = pathB
                else:
                    path = [edge[1], edge[2]]   #        ->
                    pathEnds[edge[2]] = path    #     pb -- pe
                    pathBegins[edge[1]] = path
                
                #if path is ready, break the loop
                if len(pathEdges) == vertices - 1:
                    break
        
        
        #add cost of closing vertex
        _, path = pathBegins.popitem()
        cost += data[path[-1]][path[0]]
        
        return (cost, path)
    
    def _prepareEdges(self, data):
        edges = []
        
        #enumerate both rows and columns to construct list of all edges
        for source, row in enumerate(data):
            for target, cost in enumerate(row):
                if target != source:
                    edges.append((cost, source, target)) 
                    
        return edges