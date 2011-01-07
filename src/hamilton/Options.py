import argparse
import random
from hamilton.datasource.FileDataSource import FileDataSource;
from hamilton.datasource.RandomGeneratorDataSource import RandomGeneratorDataSource;
from hamilton.algorithm.FullSearch import FullSearch
from hamilton.algorithm.GreedyEdges import GreedyEdges
from hamilton.algorithm.GreedyVertices import GreedyVertices
from hamilton.formatter.SimpleText import SimpleText
from hamilton.formatter.VerySimpleText import VerySimpleText
from hamilton.formatter.Simple3D import Simple3D

class Options(object):

    _parser = argparse.ArgumentParser(description='Simple hamilton solver')
    _knownAlgorithms = {'fs': FullSearch, 'ge': GreedyEdges, 'gv': GreedyVertices}
    _knownFormatters = {'text' : SimpleText, '3d': Simple3D,'vst':VerySimpleText}

    def __init__(self):
        #build parser options
        self._parser.add_argument('_algorithms', metavar='ALGORITHM', choices=self._knownAlgorithms.keys(), nargs='+', help='algorithm used for solving given problem (available options: %(choices)s)')
        self._parser.add_argument('-d', '--display', dest='_formatter', default='text', metavar='FORMATTER', choices=self._knownFormatters.keys(), help='formatter used to present results (available options: %(choices)s)')
        self._parser.add_argument('-l', '--loops', dest='_loops', default=1, metavar='N', type=int, help='number of loops for each algorithm')
        self._parser.add_argument('-s', '--seed', dest='_seed', default=1, metavar='SEED', type=int, help='seed to initialize random generator')
        self._parser.add_argument('-ism', '--increment', action='store_true', dest='_increment_seed', default=False, help='seed increment mode')

        datasources = self._parser.add_mutually_exclusive_group(required=True)
        datasources.add_argument('-f', '--file', dest='_dataSource', metavar='FILENAME', type=datasourceFile, help='read data from specified file')
        datasources.add_argument('-r', '--random', dest='_dataSource', metavar='VERTICES_COUNT', type=datasourceRandom, help='generate random data for specified vertices count')

        #do parse arguments
        self._parser.parse_args(namespace=self)

        #instantiate algorithms and formatters
        self._algorithms = [self._knownAlgorithms[algorithm]() for algorithm in self._algorithms]
        self._formatter = self._knownFormatters[self._formatter]()

    def getAlgorithms(self):
        return self._algorithms

    def getDataSource(self):
        return self._dataSource

    def getFormatter(self):
        return self._formatter

    def getLoops(self):
        return self._loops

    def getSeed(self):
        return self._seed

    def isIncrementSeedMode(self):
        return self._increment_seed

def setSeed(option):
    random.seed(option)

#datasource bindings
def datasourceFile(option):
    try:
        file = open(option, 'r')
    except IOError as (errno, strerror):
        raise argparse.ArgumentTypeError("Couldn't open file '{0}' for reading: [(1}] {2}".format(option, errno, strerror))

    return FileDataSource(file)

def datasourceRandom(option):
    try:
        vertices = int(option)
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid number of vertices: '{0}' is not a number".format(option))

    if(vertices < 4):
        raise argparse.ArgumentTypeError("Invalid number of vertices: at least 4 required (given: '{0}')".format(option))

    datasource = RandomGeneratorDataSource(vertices)
    return datasource