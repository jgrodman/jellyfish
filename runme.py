from GraphGenerator import GraphGenerator
from Pather import Pather
from Figure9 import Figure9
from YenKSP.graph import DiGraph
import os

def main():
  os.chdir("YenKSP")
  g = _generateGraph()
  _createImage(g)
  os.chdir("..")
  _createFigure9(g)

def _createFigure9(g):
  print "Counting paths..."
  p = Pather(g)
  p.countPaths()
  print "Creating plot..."
  print len(p.kspPathCounts), len(p.ecmpPathCounts)
  Figure9(p.kspPathCounts, p.ecmpPathCounts).plot("output/figure9.png")
  
def _generateGraph():
  print "Generating graph..."
  numNodes = 35
  edgesPerNode = 5
  g = GraphGenerator(numNodes, edgesPerNode, "graph")
  print "numNodes", numNodes
  print "edgesPerNode", edgesPerNode
  
  return g.generate()

def _createImage(g):
  paint = g.painter()
  g.export(False, paint)

if __name__ == "__main__":
    main()
