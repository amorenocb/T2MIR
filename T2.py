from pyflann import *
from dataLoaders import Dataset
import numpy as np
import time

# algorithm - the algorithm to use for building the index.
# The possible val- ues are: ’linear’, ’kdtree’, ’kmeans’, ’composite’ or ’autotuned’.
# The ’linear’ option does not create any index, it uses brute-force search in the original dataset points.
# ’kdtree’ creates one or more randomized kd-trees.
# ’kmeans’ creates a hierarchical kmeans clustering tree.
# ’composite’ is a mix of both kdtree and kmeans trees and the ’autotuned’
#  automatically determines the best index and optimum parameters using a cross-validation technique.

def loadData(q_File, r_File):
    data = Dataset(q_File, r_File)

def computeLinearIndexResults(datasets):
    flann = FLANN()
    for dataset in datasets:
        build_data = dataset.R
        query_data = dataset.Q
        build_start_time = time.time()
        linear_scan_index = flann.build_index(build_data, algorithm="linear")
        build_end_time = time.time()
        build_time = build_start_time - build_end_time

        result, dist = flann.nn_index(query_data)


