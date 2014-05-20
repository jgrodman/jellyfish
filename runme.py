from GraphGenerator import GraphGenerator
from YenKSP.graph import DiGraph
import os

def generateGraph():
  os.chdir("YenKSP")
  g = GraphGenerator(24, 5)
  g.generate()
  return g

def createImage(g):
  paint = g.graph.painter()
  g.graph.export(False, paint)

def main():
  g = generateGraph()
  createImage(g)

if __name__ == "__main__":
    main()
