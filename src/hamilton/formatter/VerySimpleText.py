from hamilton.Formatter import Formatter

class VerySimpleText(Formatter):
    def display(self, ordinal, name, solution, data, loops, averageSeconds, minimalSeconds, maximalSeconds):
        print "{0} {1}".format(
            averageSeconds * 1000, solution[0])
    def displayData(self, data):
        pass