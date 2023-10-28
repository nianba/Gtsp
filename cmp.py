import random
import numpy as np
from tabu_gtsp import TabuGtsp
from aco_gtsp import ACOGtsp
from common import PltResult, TestCaseGenerate, PltProcess
import time
# seed = 0
# random.seed(seed)
if __name__ == '__main__': 
    cityPosList, goodsTypes = TestCaseGenerate(citynum = 200, typenum = 150, 
                                               scaleMax = 20)
    time_tabu_begin = time.time()
    tabu = TabuGtsp(cityPosList,goodsTypes)
    bestSolution, bestValue, historyBestValues = tabu.findPath()
    print(bestSolution, bestValue)

    time_aco_begin = time.time()
    aco = ACOGtsp(cityPosList, goodsTypes)
    bestSolution, bestValue, historyBestValues = aco.findPath()
    print(bestSolution, bestValue)

    time_aco_end = time.time()
    print(time_aco_begin - time_tabu_begin, time_aco_end - time_aco_begin)