from GraphGenerator import GraphGenerator
from Pather import Pather
from Figure9 import Figure9
from YenKSP.graph import DiGraph
from PlotVariability import plotVariability
import os
import shutil

def main():
  if os.path.exists("output"):
    shutil.rmtree("output")
  os.mkdir("output")
  numSamples = 10
  kspAverages = []
  ecmpAverages = []
  for i in range(0,numSamples):
    numNodes = 35
    edgesPerNode = 5
    os.chdir("YenKSP")
    graphName = "graph" + str(i)
    g = _generateGraph(numNodes, edgesPerNode, graphName)
    _createImage(g)
    os.chdir("..")
    _createFigure9(g, graphName)
    (kspPathCounts, ecmpPathCounts) = _countPaths(g)
    kspAverages.append(_listAverage(kspPathCounts.values()))
    ecmpAverages.append(_listAverage(ecmpPathCounts.values()))
  plotVariability(kspAverages, ecmpAverages,"output/variability.png")
    
  print "KSP averages: %s" % kspAverages
  print "ECMP averages: %s" % ecmpAverages
   
def _createFigure9(g, graphName):
  p = Pather(g)
  p.countPaths()
  Figure9(p.kspPathCounts, p.ecmpPathCounts).plot("output/" + graphName + "_figure9.png")


def _countPaths(g):
  p = Pather(g)
  p.countPaths()
  return (p.kspPathCounts, p.ecmpPathCounts)
  
def _generateGraph(numNodes, edgesPerNode, graphName):
  print "Generating graph..."
  g = GraphGenerator(numNodes, edgesPerNode, graphName)
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
