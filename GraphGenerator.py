import random
import json
from YenKSP.graph import DiGraph

# class for generating a random graph, as per Jellyfish algorithm
class GraphGenerator:
  def __init__(self, numNodes, edgesPerNode):
    self.edgesPerNode = edgesPerNode
    self.numNodes = numNodes
    self._setup()

  def _setup(self):
    self.open = []
    self.closed = []
    self.graph = DiGraph("jesse")
    for i in range(self.numNodes):
      self.graph.add_node(i+1)
      self.open.append(i+1)
      
  # generates the graph, so that the underlying graph object can then be used
  def generate(self):
    previousOpenLen = 99999
    sameCount = 0
    while len(self.open) > 0:
      while self._linkNodes():
        pass
  
      # Special cases
      if len(self.open) == 1:
        if self.graph.num_edges(self.open[0]) > 1:
          self._linkSwap(self.open[0])
        return self.graph
        
      if self._isFullyConnected(self.open):
          self._linkSwap(random.choice(self.open))
          
      if len(self.open) == previousOpenLen:
        sameCount = sameCount + 1
        # print "Same count is %d" % sameCount
      else:
        sameCount = 0
      previousOpenLen = len(self.open)
      
      if sameCount > self.numNodes * 3:
          print "Abort!"
          self._setup()
          sameCount = 0
          previousOpen = 99999
          
    return self.graph

  # move nodes around open, closed if necessary
  def _relocateNodes(self, nodes):
    for node in nodes:
      if self.graph.num_edges(node) < self.edgesPerNode and node in self.closed:
        self.closed.remove(node)
        self.open.append(node)
      elif self.graph.num_edges(node) == self.edgesPerNode and node in self.open:
        self.open.remove(node)
        self.closed.append(node)

  # find a pair of unlinked nodes and link them
  def _linkNodes(self):
    random.shuffle(self.open)
    for a in self.open:
      for b in self.open:
        if (not a is b) and (not self.graph.has_edge(a, b)):
          self.graph.add_edge(a, b, 1)
          self.graph.add_edge(b, a, 1)
          self._relocateNodes([a, b])
          return True
    return False

  # find a pair of linked nodes and unlink them
  # link is selected uniformly at random from existing links
  def _unlinkNodes(self):
    removeNum = random.randint(0, self.graph.num_total_edges() - 1)
    for node in self.open + self.closed:
      if self.graph.num_edges(node) > removeNum:
        other = self.graph.get_nth_edge(node, removeNum)
        self.graph.delete_edge(node, other)
        self.graph.delete_edge(other, node)
        self._relocateNodes([node, other])
        return
      removeNum -= self.graph.num_edges(node)
      
  # Deals with an isolated open node 
  # Removes a random link and connects the endpoints to the isolated edge 
  def _linkSwap(self, node):
    while self.graph.num_edges(node) > 1 and self.graph.num_edges(node) < self.edgesPerNode:
      otherNode1 = random.choice(self.closed)
      otherNode2 = self.graph.get_nth_edge(otherNode1, 0)
      
      self.graph.delete_edge(otherNode1, otherNode2)
      self.graph.delete_edge(otherNode2, otherNode1)

      self.graph.add_edge(node, otherNode1, 1)
      self.graph.add_edge(otherNode1, node, 1)
      self.graph.add_edge(node, otherNode2, 1)
      self.graph.add_edge(otherNode2, node, 1)
      self._relocateNodes([node, otherNode1, otherNode2])
  
  # Checks if a list of nodes is fully connected
  def _isFullyConnected(self, nodes):
    if len(nodes) <= 1:
      return False
    print "isFullyConnected"
    for a in nodes:
        for b in nodes:
            if a is not b and not self.graph.has_edge(a, b):
                return False
    return True