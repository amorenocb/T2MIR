from pyflann import *
from dataLoaders import Dataset
import time
import csv

# algorithm - the algorithm to use for building the index.
# The possible val- ues are: ’linear’, ’kdtree’, ’kmeans’, ’composite’ or ’autotuned’.
# The ’linear’ option does not create any index, it uses brute-force search in the original dataset points.
# ’kdtree’ creates one or more randomized kd-trees.
# ’kmeans’ creates a hierarchical kmeans clustering tree.
# ’composite’ is a mix of both kdtree and kmeans trees and the ’autotuned’
#  automatically determines the best index and optimum parameters using a cross-validation technique.

def loadData(data_file):
    return Dataset(data_file)

def saveResults(output_file_name, results, build_time, query_time, checks = None, trees = None, branching = None):
    i = 0
    with open(output_file_name, "w") as output:
        writer = csv.writer(output, lineterminator="\n")
        for (r, d) in results:
            if (i % 1000 == 0):
                print(i)
            writer.writerow([r, d])
            i += 1
        writer.writerow(["Build time", build_time])
        if trees:
            writer.writerow(["Checks", checks])
            writer.writerow(["Trees", trees])
        if branching:
            writer.writerow(["Checks", checks])
            writer.writerow(["Branching", branching])

def computeLinearIndexResults(r_data, q_data, result_file):

    build_data = r_data
    query_data = q_data

    flann = FLANN()

    build_start_time = time.time()
    flann.build_index(build_data, algorithm="linear")
    build_end_time = time.time()
    build_time = build_end_time - build_start_time

    query_start_time = time.time()
    result, dist = flann.nn_index(query_data)
    query_end_time = time.time()
    query_time = query_end_time - query_start_time

    flann.save_index("linearIndex")
    saveResults("LinearResults.csv", zip(result,dist), build_time, query_time)

def computeKdTreeIndexResults(r_data, q_data, number_of_trees, checks):

    build_data = r_data
    query_data = q_data

    flann = FLANN()

    build_start_time = time.time()
    flann.build_index(build_data, algorithm="kdtree", trees=number_of_trees)
    build_end_time = time.time()
    build_time = build_end_time - build_start_time

    query_start_time = time.time()
    result, dist = flann.nn_index(query_data, checks=checks)
    query_end_time = time.time()
    query_time = query_end_time - query_start_time

    flann.save_index("kdTreeIndex-{}-{}".format(checks, number_of_trees))
    saveResults("kdTreeResults-{}-{}.csv".format(checks, number_of_trees), zip(result, dist), build_time, query_time, checks, number_of_trees)

def computeKmeansIndexResults(r_data, q_data, branching, checks):

    build_data = r_data
    query_data = q_data

    flann = FLANN()

    build_start_time = time.time()
    flann.build_index(build_data, algorithm="kmeans", branching=branching)
    build_end_time = time.time()
    build_time = build_end_time - build_start_time

    query_start_time = time.time()
    result, dist = flann.nn_index(query_data, checks=checks)
    query_end_time = time.time()
    query_time = query_end_time - query_start_time

    flann.save_index("KmeansIndex-{}-{}".format(checks, branching))
    saveResults("KmeansResults-{}-{}.csv".format(checks,branching), zip(result, dist), build_time, query_time, checks, branching)



r_data = loadData("mega-2014_04_10T21_15_19-48000x128_4F.bin")
q_data = loadData("mega-2014_04_11T21_13_04-48000x128_4F.bin")

computeLinearIndexResults(r_data.descriptors, q_data.descriptors, "linear_results.csv")


