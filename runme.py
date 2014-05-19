from GraphGenerator import GraphGenerator
from YenKSP.graph import DiGraph
import os

def generateGraph():
  os.chdir("YenKSP")
  g = GraphGenerator(20, 5)
  g.generate()
  paint = g.graph.painter()
  g.graph.export(False, paint)


def main():
  generateGraph()

if __name__ == "__main__":
    main()