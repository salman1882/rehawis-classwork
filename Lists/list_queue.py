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

   def append(self,NewName):
      NewNode = NodeType(NewName) 
      tmp = self.headval
      while(tmp.pointer):
         tmp = tmp.pointer
      tmp.pointer=NewNode

list = LinkedList()
list.headval = NodeType("Mon")
D2 = NodeType("Tue")
D3 = NodeType("Wed")

list.headval.pointer = D2
D2.pointer = D3
list.append("Thu")

list.listprint()
