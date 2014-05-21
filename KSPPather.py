from YenKSP.graph import DiGraph
from YenKSP.algorithms import ksp_yen

class KSPPather:
  def __init__(self, graph, k=8):
    self.graph = graph
    self.k = k
    
  # Counts the number of paths each link is on under KSP
  # A link is represented as a tuple (firstNode, secondNode)
  # Each direction is considered a separate link
  # Returns a dictionary of link => pathCount
  def countPaths(self):
    pathCounts = {}
    
    for sourceNode in self.graph:
      for sinkNode in self.graph:
        if sourceNode is not sinkNode:
          # Calculate the paths between the nodes
          paths = ksp_yen(self.graph,sourceNode,sinkNode,self.k)
        
          for pathInfo in paths:
            self._incrementLinksOnPath(pathInfo["path"], pathCounts)
    return pathCounts
    
  # Increments the path count of each link on the given path
  # path = list of nodes forming a path
  # pathCounts = dictionary to update (modified in place)
  def _incrementLinksOnPath(self, path, pathCounts):
    previousNode = None
    for node in path:
      if previousNode == None:
        previousNode = node
        continue
      link = (previousNode, node)
      if link in pathCounts:
        pathCounts[link] = pathCounts[link] + 1
      else:
        pathCounts[link] = 1
      previousNode = node