from GraphGenerator import GraphGenerator
from Pather import Pather
from Figure9 import Figure9
from YenKSP.graph import DiGraph
import os

def main():
  g = _generateGraph()
  _createImage(g)
  _createFigure9(g)

def _createFigure9(g):
  print "Counting paths..."
  p = Pather(g)
  p.countPaths()
  print "Creating plot..."
  Figure9(p.kspPathCounts, p.ecmpPathCounts).plot("figure9.png")
  
def _generateGraph():
  print "Generating graph..."
  os.chdir("YenKSP")
  g = GraphGenerator(30, 5)
  return g.generate()

def _createImage(g):
  paint = g.painter()
  g.export(False, paint)

if __name__ == "__main__":
    main()
