import matplotlib.pyplot as plt
import numpy as np
import math
# Plots a bar graph showing the distribution of average path counts of graphs
# x-axis: averages
# y-axis: number of graphs

def plotVariability(kspAverages, ecmpAverages, filename):
  # Group the values into buckets, bounded by the smallest and largest values 
  # present in either array
  # We only have a finite space for labels, so set the increment as needed
  # to support a fixed number of buckets
  numberOfBuckets = 10
  maxKSP = max(kspAverages)
  maxECMP = max(ecmpAverages)
  minKSP = min(kspAverages)
  minECMP = min(ecmpAverages)
  ranger = max(maxKSP, maxECMP) - min(minKSP, minECMP)
  increment = int(math.ceil(float(ranger) / numberOfBuckets))
  
  # Calculate the overall bounds and the number of items within each bucket
  upperBound = roundUpToNearestIncrement(max(maxKSP, maxECMP),increment)
  lowerBound = roundDownToNearestIncrement(min(minKSP, minECMP),increment)
  kspCounts = countValuesWithinIntervals(lowerBound, upperBound, increment, kspAverages)
  ecmpCounts = countValuesWithinIntervals(lowerBound, upperBound, increment, ecmpAverages)
  maxCount = max(max(kspCounts),max(ecmpCounts))
  
  # Draw the graphs, with one bar for each buckets 
  barWidth = 0.35
  xCoords = range(0, (upperBound - lowerBound) / increment)
  ecmpXCoords = map(lambda x: x + barWidth, xCoords)
  kspRects = plt.bar(xCoords, kspCounts, barWidth, color = 'r')
  ecmpRects = plt.bar(ecmpXCoords, ecmpCounts, barWidth, color = 'y') 

  # Labels
  plt.ylabel('Number of Graphs')
  plt.xlabel('Average # of distinct paths per node')
  plt.xticks(ecmpXCoords, generateLabels(lowerBound, upperBound, increment),fontsize=10)
  plt.yticks(range(0,maxCount + 1,2), fontsize=10)
  plt.legend( ('8 Shortest Paths', '8-way ECMP'), loc='upper right')
  plt.savefig(filename)
  plt.close()
  
def roundUpToNearestIncrement(num, increment):
  return int(math.ceil(float(num) / increment) * increment);

def roundDownToNearestIncrement(num, increment):
  return int(math.floor(num / increment) * increment);
  
# Counts the number of values in lst that fall within each subinterval of
# length increment between lower and upper bounds, 
# Returns results in array ordered by subinterval
# For example, fun(10,30,10, [13,14,22]) would return [0,2,1]
def countValuesWithinIntervals(lowerBound, upperBound, increment, lst):
  counts = []
  for i in range(lowerBound, upperBound, increment):
    counts.append(len(filter(lambda x: x >= i and x < i + increment, lst)))
  return counts
  
# Generates labels for each subinterval
def generateLabels(lowerBound, upperBound, increment):
  labels = []
  for i in range(lowerBound, upperBound, increment):
    labels.append("%d-%d" % (i, i + increment - 1))
  return labels