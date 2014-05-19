from GraphGenerator import GraphGenerator
from YenKSP.graph import DiGraph
import os

def generateGraph():
  g = GraphGenerator(12, 5)
  g.generate()
  os.chdir("YenKSP")
  g.export("data/json/jesse.json")
  G = DiGraph("jesse")
  paint = G.painter()
  G.export(False, paint)


def main():
  generateGraph()

if __name__ == "__main__":
    main()