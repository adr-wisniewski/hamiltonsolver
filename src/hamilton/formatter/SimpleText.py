'''
Created on 2010-11-15

@author: Adrian
'''
from hamilton.Formatter import Formatter

class SimpleText(Formatter):
    def display(self, ordinal, name, solution, data, loops, averageSeconds, minimalSeconds, maximalSeconds):
        print "Algorithm {0}: {1} (loops: {2} - avg: {3}ms, min: {4}ms, max: {5}ms)".format(
            ordinal, name, loops, averageSeconds * 1000, minimalSeconds * 1000, maximalSeconds * 1000)
        print 'Solution cost: {0}'.format(solution[0])
        print 'Solution path: {0}'.format(solution[1])
        print
        
    def displayData(self, data):
        print "Data ({0} vertices)".format(len(data))
        for index, row in enumerate(data):
            myrow = [] + row
            myrow[index] = 'x'
            print "%d: %s" % (index, myrow)
            
        print