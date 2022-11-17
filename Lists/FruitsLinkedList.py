class NodeType:
   def __init__(self, name=None):
      self.name = name
      self.pointer = None

class LinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.name)
         printval = printval.pointer

list = LinkedList()
list.headval = NodeType("Banana")
D2 = NodeType("Lemon")
D3 = NodeType("Melon")
D4 = NodeType("Strawberry")

list.headval.pointer = D2
D2.pointer = D3
D3.pointer = D4

list.listprint()
