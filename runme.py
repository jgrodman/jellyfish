from GraphGenerator import GraphGenerator
from YenKSP.graph import DiGraph
import os

def generateGraph():
  os.chdir("YenKSP")
  g = GraphGenerator(24, 5)
  return g.generate()

def createImage(g):
  paint = g.painter()
  g.export(False, paint)

def main():
  g = generateGraph()
  createImage(g)

if __name__ == "__main__":
    main()