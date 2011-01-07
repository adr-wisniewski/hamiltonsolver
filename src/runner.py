import os
vertices = range(4,30)
algorithms = ['ge','gv','fs']
for a in algorithms:
    print a
    for v in vertices:
        os.system("main.py -r {0} {1} -d vst -l 10".format(v,a))
