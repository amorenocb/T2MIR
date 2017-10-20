from pyflann import *
from dataLoaders import Dataset
import time
import csv
import sys

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
    with open(output_file_name, "w") as output:
        writer = csv.writer(output, lineterminator="\n")
        for (r, d) in results:
            writer.writerow([r, d])
        writer.writerow(["Build time", build_time])
        writer.writerow(["Query time", query_time])
        if trees:
            writer.writerow(["Checks", checks])
            writer.writerow(["Trees", trees])
        if branching:
            writer.writerow(["Checks", checks])
            writer.writerow(["Branching", branching])

def computeLinearIndexResults(r_data, q_data):

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


r_data_filename = sys.argv[1]
q_data_filename = sys.argv[2]
r_data = loadData(r_data_filename)
q_data = loadData(q_data_filename)

index = sys.argv[3]

if(len(sys.argv) > 4):
    checks = int(sys.argv[4])
    if(index == 'kdtree'):
        number_of_trees = int(sys.argv[5])
        computeKdTreeIndexResults(r_data.descriptors, q_data.descriptors, number_of_trees, checks)
    elif(index == 'kmeans'):
        branching = int(sys.argv[5])
        computeKmeansIndexResults(r_data.descriptors, q_data.descriptors, branching, checks)
elif(index == 'linear'):
    computeLinearIndexResults(r_data.descriptors, q_data.descriptors)


# "mega-2014_04_10T21_15_19-48000x128_4F.bin"
# "mega-2014_04_11T21_13_04-48000x128_4F.bin"




