a = [7,4,5,8,1,2,6]

def bubble1(array):
    for i in range(len(array) - 1 ):
      for j in range(len(array)-1):
       if a[j] > a[j + 1]:
          swap(a,j,(j+1))

    

def swap(arr,a,b):
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

swap(a,0,1)
bubble1(a)

for i in range(0,6):
   print(a[i])
