import matplotlib as m
m.use("Agg")
import matplotlib.pyplot as plt

class Figure9:
  def __init__(self, kspPathCounts, ecmpPathCounts):
    self.kspPathCounts = kspPathCounts
    self.ecmpPathCounts = ecmpPathCounts
    
  def plot(self, filename):
    kspValues = sorted(self.kspPathCounts.values())
    ecmpValues = sorted(self.ecmpPathCounts.values())
    xValues = range(0, max(len(kspValues),len(ecmpValues)))
    # plt.plot(xValues, kspValues)
    plt.step(xValues, kspValues, where='post', label="8 Shortest Paths")
    plt.step(xValues, ecmpValues, where='post', label="8-way ECMP")
    plt.xlabel('Rank of Link')
    plt.ylabel('# Distinct Paths Link is on')
    plt.xlim(0,max(xValues))
    plt.ylim(0,max(max(kspValues), max(ecmpValues)))
    plt.legend( ('8 Shortest Paths', '8-way ECMP'), loc='upper left')
    plt.savefig(filename)
    
  # def _prepareData(self):