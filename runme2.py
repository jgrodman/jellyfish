from GraphGenerator import GraphGenerator
from Pather import Pather
from Figure9 import Figure9
from YenKSP.graph import DiGraph
import os

def main():
  os.chdir("YenKSP")
  numSamples = 10
  kspAverages = []
  ecmpAverages = []
  for i in range(0,numSamples):
    numNodes = 35
    edgesPerNode = 5
    g = _generateGraph(numNodes, edgesPerNode)
    (kspPathCounts, ecmpPathCounts) = _countPaths(g)
    kspAverages.append(_listAverage(kspPathCounts.values()))
    ecmpAverages.append(_listAverage(ecmpPathCounts.values()))

    
  print "KSP averages: %s" % kspAverages
  print "ECMP averages: %s" % ecmpAverages
   
def _countPaths(g):
  print "Counting paths..."
  p = Pather(g)
  p.countPaths()
  print "Creating plot..."
  return (p.kspPathCounts, p.ecmpPathCounts)
  
def _generateGraph(numNodes, edgesPerNode):
  print "Generating graph..."
  g = GraphGenerator(numNodes, edgesPerNode)
  print "numNodes", numNodes
  print "edgesPerNode", edgesPerNode
  return g.generate()

def _createImage(g):
  paint = g.painter()
  g.export(False, paint)

def _listAverage(lst):
  return sum(lst) / len(lst)
  
if __name__ == "__main__":
    main()
