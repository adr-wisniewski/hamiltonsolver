import time
from hamilton.Options import Options

#read command line options
options = Options()
algorithms = options.getAlgorithms()
datasource = options.getDataSource()
formatter = options.getFormatter()
loops = options.getLoops()
isIncrementSeedMode = options.isIncrementSeedMode()
seed = options.getSeed()

if(seed):
    datasource.setSeed(seed)

#prepare and display data
data = datasource.getData()
formatter.displayData(data)

#solve problem and print results
for ordinal, algorithm in enumerate(algorithms):
    times = []
    solutions = []
    for loop in xrange(loops):
        if isIncrementSeedMode:
            datasource.setSeed(seed)
            seed=seed+1
            data=datasource.getData()
        start = time.clock()
        solution = algorithm.solve(data)
        end = time.clock()

        times.append(end - start)
        solutions.append(solution[0])


    minimal = min(times)
    maximal = max(times)
    average = sum(times) / len(times)

    if(isIncrementSeedMode):
        solution = (sum(solutions) / len(solutions), 0)

    formatter.display(ordinal, algorithm.getName(), solution, data, loops, average, minimal, maximal)


