from YenKSP.graph import DiGraph
from YenKSP.algorithms import ksp_yen

class Pather:
  def __init__(self, graph, k=8):
    self.graph = graph
    self.k = k
    self.kspPathCounts = {}
    self.ecmpPathCounts = {}
    
  # Counts the number of paths each link is on under KSP and ECMP
  # A link is represented as a tuple (firstNode, secondNode)
  # Each direction is considered a separate link
  # Populates path count object properties; no return value
  def countPaths(self):
    for sourceNode in self.graph:
      for sinkNode in self.graph:
        if sinkNode >= sourceNode: # only traverse path in one direction
          continue
        paths = ksp_yen(self.graph,sourceNode,sinkNode,self.k)
        if len(paths) == 0:
          continue
            
        # Increment path counts for KSP (always), ECMP (if cost = cost of shortest path)
        minimumPathCost = paths[0]["cost"]  
        for pathInfo in paths:
          self._incrementLinksOnPath(pathInfo["path"], self.kspPathCounts)
          if pathInfo["cost"] == minimumPathCost:
            # EC
            self._incrementLinksOnPath(pathInfo["path"], self.ecmpPathCounts)
              
  # Increments the path count of each link on the given path
  # path = list of nodes forming a path
  def _incrementLinksOnPath(self, path, pathCounts):
    previousNode = None
    for node in path:
      if previousNode == None:
        previousNode = node
        continue

      # add both permutations since we only traverse each path in one direction, even though it is undirected
      link = (previousNode, node)
      if link in pathCounts:
        pathCounts[link] += 1 
      else:
        pathCounts[link] = 1

      link = (node, previousNode)
      if link in pathCounts:
        pathCounts[link] += 1
      else:
        pathCounts[link] = 1

      previousNode = node
