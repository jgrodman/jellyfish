from GraphGenerator import GraphGenerator
from YenKSP.graph import DiGraph
import os

def main():
  g = _generateGraph()
  _createImage(g)

def _generateGraph():
  os.chdir("YenKSP")
  g = GraphGenerator(24, 5)
  return g.generate()

def _createImage(g):
  paint = g.painter()
  g.export(False, paint)

if __name__ == "__main__":
    main()
