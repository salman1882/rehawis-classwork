gnames = ["Amelia","Olivia","Isla","Emily","Poppy", "Ava","Isabella","Jessica","Lily","Sophie"]
def Linsearch(list,target):
    index = - 1
    found = False 
    i = 0
    while found == False and i < len(list):
       if list[i] == target:
        found = True
        return i  
        i = i + 1   
       else:
        return "-1" 
