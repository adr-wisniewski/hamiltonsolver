import random
import time
from hamilton.Options import Options

#initialize random generator's seed
random.seed()

#read command line options
options = Options()
algorithms = options.getAlgorithms()
datasource = options.getDataSource()
formatter = options.getFormatter()
loops = options.getLoops()

#prepare and display data
data = datasource.getData()
formatter.displayData(data)

#solve problem and print results
for ordinal, algorithm in enumerate(algorithms):
    times = []
    for loop in xrange(loops):
        start = time.clock()
        solution = algorithm.solve(data)
        end = time.clock()
        
        times.append(end - start)

        
    minimal = min(times)
    maximal = max(times)
    average = sum(times) / len(times)
    formatter.display(ordinal, algorithm.getName(), solution, data, loops, average, minimal, maximal)


