import random
import json
import copy
from YenKSP.graph import DiGraph

# class for generating a random graph, as per Jellyfish algorithm
class GraphGenerator:
  def __init__(self, numNodes, edgesPerNode, graphName):
    self.edgesPerNode = edgesPerNode
    self.numNodes = numNodes
    self.open = []
    self.closed = []
    self.graph = DiGraph(graphName)
    for i in range(self.numNodes):
      self.graph.add_node(i+1)
      self.open.append(i+1)
      
  def generate(self):
    while True:
      # loop until there are no more connections within open to make
      self._linkNodes()
      
      # if no open nodes remain, or only one remains and it only has one open port, we are done
      if len(self.open) is 0 or (len(self.open) is 1 and (self.edgesPerNode - self.graph.num_edges(self.open[0])) is 1):
        return self.graph

      # choose a node from open, and link it with two nodes in closed
      node = random.choice(self.open)
      self._swapLinks(node)

  # move nodes around open, closed if necessary
  def _relocateNodes(self, nodes):
    for node in nodes:
      if self.graph.num_edges(node) < self.edgesPerNode and node in self.closed:
        self.closed.remove(node)
        self.open.append(node)
      elif self.graph.num_edges(node) == self.edgesPerNode and node in self.open:
        self.open.remove(node)
        self.closed.append(node)

  # link as many open nodes as possible
  def _linkNodes(self):
    random.shuffle(self.open)
    oldOpen = copy.deepcopy(self.open)
    for a in oldOpen:
      if not a in self.open:
        continue
      for b in oldOpen:
        if not b in self.open:
          continue
        if (not a is b) and (not self.graph.has_edge(a, b)):
          self.graph.add_edge(a, b, 1)
          self.graph.add_edge(b, a, 1)
          self._relocateNodes([a, b])

  # disconnect two closed nodes that are not linked to the given node, and link them to the given node
  def _swapLinks(self, node):
    # if the node only has one open link, create a second open link
    if (self.edgesPerNode - self.graph.num_edges(node)) is 1:
      toRemove = self.graph.get_nth_edge(node, random.randint(0, self.graph.num_edges(node) - 1))
      self.graph.delete_edge(node, toRemove)
      self.graph.delete_edge(toRemove, node)

    otherNode1 = random.choice(self.closed)
    while self.graph.has_edge(node, otherNode1):
      otherNode1 = random.choice(self.closed)

    otherNode2 = self.graph.get_nth_edge(otherNode1, random.randint(0, self.edgesPerNode - 1))
    while self.graph.has_edge(node, otherNode2):
      otherNode2 = self.graph.get_nth_edge(otherNode1, random.randint(0, self.edgesPerNode - 1))
      
    self.graph.delete_edge(otherNode1, otherNode2)
    self.graph.delete_edge(otherNode2, otherNode1)

    self.graph.add_edge(node, otherNode1, 1)
    self.graph.add_edge(otherNode1, node, 1)
    self.graph.add_edge(node, otherNode2, 1)
    self.graph.add_edge(otherNode2, node, 1)
    self._relocateNodes([node, otherNode1, otherNode2])
