import matplotlib as m
m.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import math
# Plots a bar graph showing the distribution of average path counts of graphs
# x-axis: averages
# y-axis: number of graphs

def plotVariability(kspAverages, ecmpAverages):
  # Group the values into groups of 10, bounded by the smallest and largest values 
  # present in either array
  upperBound = roundUpToNearest10(max(max(kspAverages), max(ecmpAverages)))
  lowerBound = roundDownToNearest10(min(kspAverages, min(ecmpAverages)))
  increment = 10
  kspCounts = countValuesWithinIntervals(lowerBound, upperBound, increment, kspAverages)
  ecmpCounts = countValuesWithinIntervals(lowerBound, upperBound, increment, ecmpAverages)
  
  # Draw the graphs, with one bar for each group 
  barWidth = 0.35
  xCoords = range(0, (upperBound - lowerBound) / increment)
  ecmpXCoords = map(lambda x: x + barWidth, xCoords)
  kspRects = plt.bar(xCoords, kspCounts, barWidth, color = 'r')
  ecmpRects = plt.bar(ecmpXCoords, ecmpCounts, barWidth, color = 'y') 

  # Labels
  plt.ylabel('Number of Graphs')
  plt.xlabel('Average # of distinct paths per node')
  plt.xticks(ecmpXCoords)
  # plt.xticklabels(generateLabels(lowerBound, upperBound, increment))
  
  plt.savefig("test.png")
  
def roundUpToNearest10(num):
  return int(math.ceil(float(num) / 10) * 10);

def roundDownToNearest10(num):
  return int(math.floor(num / 10) * 10);
  
# Counts the number of values in lst that fall within each subinterval of
# length increment between lower and upper bounds, 
# Returns results in array ordered by subinterval
# For example, fun(10,30,10, [13,14,22]) would return [0,2,1]
def countValuesWithinIntervals(lowerBound, upperBound, increment, lst):
  counts = []
  for i in range(lowerBound, upperBound, 10):
    counts.append(len(filter(lambda x: x >= i and x < i + 10, lst)))
  return counts
  
# Generates labels for each subinterval
def generateLabels(lowerBound, upperBound, increment):
  labels = []
  for i in range(lowerBound, upperBound, increment):
    labels.append("%d-%d", lowerBound, lowerBound + increment - 1)
  return labels