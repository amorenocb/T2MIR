import pandas as pd
import csv
import os
import sys

# Returns what fraction of index2_results where
# actually in index1_results.
# Receives as inputs file names with the results.
def effectiveness(index1_results, index2_results):

    csv_index1 = csv.reader(open(index1_results))
    csv_index2 = csv.reader(open(index2_results))
    matches = 0
    lines = 0
    for row1, row2 in zip(csv_index1, csv_index2):
        if row1 == "Build time":
            break
        if row1 == row2:
            matches+=1
        lines+=1

    return matches/lines

# Returns how time-wise efficient  was index2 compared to index1
# for resolving all the query's.
# Receives as inputs file names with the results.
def efficiency(index1_results, index2_results):

    df_index1 = pd.read_csv(index1_results, header=None)
    df_index2 = pd.read_csv(index2_results, header=None)

    index1_query_time = float(df_index1.loc[df_index1[0] == 'Query time'][1])
    index2_query_time = float(df_index2.loc[df_index2[0] == 'Query time'][1])

    return index2_query_time/index1_query_time

with open("stats.csv", "w") as output:
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(["Features","Algoritmo", "Parametro" ,"Checks", "Eficiencia", "Efectividad"])
    for filename in os.listdir("."):
        if filename != "LinearResults.csv" and filename.endswith(".csv") and filename != "stats.csv":
            checks = filename.split("-")[1]
            alg = filename.split("-")[0]
            parameter = filename.split("-")[2].split(".")[0]
            writer.writerow([os.path.basename(os.getcwd()) ,alg, parameter ,checks, efficiency("LinearResults.csv", filename), effectiveness("LinearResults.csv", filename)])
