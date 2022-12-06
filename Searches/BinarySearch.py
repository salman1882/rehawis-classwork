Nums = ["1","5","8","11","12","14","16","21","26"]
found = False
def binSearch(name,target):
   mpoint = ((len(name) -1) // 2)
   print(mpoint)
   while found == False:
    if name[mpoint] == target:
      return(mpoint)
      found == True
      print(mpoint)
    elif int(name[mpoint]) > int(target):
     mpoint = mpoint // 2 
     print(mpoint)
    elif int(name[mpoint]) < int(target):
      mpoint = (len(name) - 1) - (mpoint // 2)
      print(mpoint)
