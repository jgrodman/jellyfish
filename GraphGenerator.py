import random
import json

# class for generating a random graph, as per Jellyfish algorithm
class GraphGenerator:
  def __init__(self, numNodes, edgesPerNode):
    self.numNodes = numNodes
    self.edgesPerNode = edgesPerNode
    self.open = [] # nodes that still have open links
    self.closed = [] # nodes that have no open links
    for i in range(numNodes):
      self.open.append(Node(i, edgesPerNode))

  # move nodes around open, closed if necessary
  def relocateNodes(self, nodes):
    for node in nodes:
      if node.isOpen() and node in self.closed:
        self.closed.remove(node)
        self.open.append(node)
      elif (not node.isOpen()) and node in self.open:
        self.open.remove(node)
        self.closed.append(node)

  # find a pair of unlinked nodes and link them
  def linkNodes(self):
    random.shuffle(self.open)
    for a in self.open:
      for b in self.open:
        if (not a is b) and (not a.isLinkedTo(b)):
          a.createLink(b)
          b.createLink(a)
          print a.id, "link", b.id
          self.relocateNodes([a, b])
          return True
    return False

  # count the number of total links in the graph
  def numLinks(self):
    n = 0
    for node in self.open + self.closed:
      n += node.numLinks()
    return n

  # find a pair of linked nodes and unlink them
  # link is selected uniformly at random from existing links
  def unlinkNodes(self):
    removeNum = random.randint(0, self.numLinks() - 1)
    for node in self.open + self.closed:
      if node.numLinks() > removeNum:
        other = node.linkedNodes[removeNum]
        node.removeLink(other)
        other.removeLink(node)
        self.relocateNodes([node, other])
        return
      removeNum -= node.numLinks()

  # generates the graph, so that export() can be called next
  def generate(self):
    while len(self.open) > 0:
      while self.linkNodes():
        pass
      if len(self.open) > 0:
        self.unlinkNodes()

  # write JSON representing graph to file
  def export(self, fileName):
    dump = {}
    for node in self.closed:
      linkedWeights = {}
      for linkedTo in node.linkedNodes:
        linkedWeights[linkedTo.id] = 1
      dump[node.id] = linkedWeights
    f = open(fileName, "w")
    f.write(json.dumps(dump))
    f.close()

class Node:
  def __init__(self, id, capacity):
    self.id = id
    self.capacity = capacity
    self.linkedNodes = []

  def createLink(self, node):
    self.linkedNodes.append(node)

  def removeLink(self, node):
    self.linkedNodes.remove(node)

  def isLinkedTo(self, node):
    return node in self.linkedNodes

  def numLinks(self):
    return len(self.linkedNodes)

  def isOpen(self):
    return self.numLinks() < self.capacity