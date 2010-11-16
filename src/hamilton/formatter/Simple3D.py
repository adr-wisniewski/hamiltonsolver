'''
Created on 2010-11-16

@author: Adrian
'''
import math
from visual import *
from hamilton.formatter.SimpleText import SimpleText

class Simple3D(SimpleText):
    def display(self, ordinal, name, solution, data, loops, averageSeconds, minimalSeconds, maximalSeconds):
        super(Simple3D, self).display(ordinal, name, solution, data, loops, averageSeconds, minimalSeconds, maximalSeconds)
        
        scene = display(title='Algorithm %s(%d) - %s' % (name, ordinal, solution), width=600, height=600)
        scene.select()
        
        #display vertices
        vertices = len(data)
        positions = {}
        for vertex in xrange(vertices):
            radian = math.pi * 2 * vertex / vertices
            position = vector(math.sin(radian),math.cos(radian),0) * vertices
            positions[vertex] = position                
            sphere(pos=position, radius=1, color=color.green)
            text(text ='%d' % vertex, pos=position+vector(0,-0.3,1), align='center')
        
        for edge in ((solution[1][vertex-1], solution[1][vertex]) if vertex > 0 else (solution[1][-1], solution[1][0]) for vertex in xrange(vertices)):
            direction = positions[edge[1]] - positions[edge[0]]
            distance = mag(direction)
            direction /= distance
            
            start = positions[edge[0]] + direction * 1.1
            end = positions[edge[1]] - + direction * 1.1
            
            arrow(pos=start, axis=end-start, color = color.yellow, shaftwidth=0.25, fixedwidth = True )
            

    def displayData(self, data):
        super(Simple3D, self).displayData(data)