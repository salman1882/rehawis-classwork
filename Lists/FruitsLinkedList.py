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
         global count
         count = count + 1
         print (printval.name)
         printval = printval.pointer    
         if printval is None:
            print(count)
                
list = LinkedList()
list.headval = NodeType("Banana")
D2 = NodeType("Lemon")
D3 = NodeType("Melon")
D4 = NodeType("Strawberry")

count = 0 
list.headval.pointer = D2
D2.pointer = D3
D3.pointer = D4

list.listprint()
